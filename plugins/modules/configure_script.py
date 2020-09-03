#!/usr/bin/python

DOCUMENTATION = '''
---
module: freedge.protect
author: Freedge
short_description: Configure a script in tsm
'''

EXAMPLES = '''
- name: configure script
  configure_script:
    server: isp1
    name: toto
'''

RETURN = '''
output:
  description: todo
  returned: success
  type: dict
'''

from ansible.module_utils.basic import AnsibleModule
import subprocess


def main():
    argument_spec = dict(credentials=dict(type="dict"), script=dict(type="str"), server=dict(type="str"), content=dict(type="str"))
    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    username = module.params['credentials']['username']
    password = module.params['credentials']['password']
    serveraddress = module.params['credentials']['serveraddress']
    command = module.params['credentials']['command']

    script = module.params['script']
    server = module.params['server']
    content = module.params['content']
    changed = False
    if not module.check_mode:
        raise NotImplementedError("only check mode supported")

    process = subprocess.Popen(
        command + ["-id=%s" % username] + ["-password=%s" % password] + ["-se=%s" % serveraddress] + ["%s:q script %s format=raw" % (server, script)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True)
    lescript = []
    extra = []
    inscript = False
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

    lediff = []
    for i, j in enumerate(content.split("\n")):
        if i >= len(lescript) or j + "\n" != lescript[i]:
            lediff += [j]
    changed = len(lediff) > 0

    result = {'changed': changed, 'running': lescript, 'all': extra, 'lediff': lediff}

    module.exit_json(**result)


if __name__ == '__main__':
    main()
