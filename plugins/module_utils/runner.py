import subprocess


def creds():
    return dict(username=dict(type="str"), command=dict(type="str"), serveraddress=dict(type="str"), password=dict(type="str", no_log=True))


def run(module, server, query):
    username = module.params['credentials']['username']
    password = module.params['credentials']['password']
    serveraddress = module.params['credentials']['serveraddress']
    command = module.params['credentials']['command']
    process = subprocess.Popen(
        command + ["-commadelimited", "-dataonly=yes", "-id=%s" % username, "-password=%s" % password, "-se=%s" % serveraddress] + ["%s:%s" % (server, query)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True)
    inscript = False
    extra = []
    lescript = []
    lastline = ""
    while True:
        i = process.stdout.readline()
        if not i:
            break
        if inscript:
            if i.startswith("ANR1688I Output for command"):
                inscript = False
            elif i.startswith("ANR1627I The previous message was repeated 1 times"):
                lescript = lescript + [lastline]
            elif i.startswith("ANR"):
                raise NotImplementedError("Could not understand the output %s" % i)
            else:
                lescript = lescript + [i]
                lastline = i
        if not inscript:
            extra += [i]
        if i.startswith("ANR1687I"):
            inscript = True
    return lescript, extra
