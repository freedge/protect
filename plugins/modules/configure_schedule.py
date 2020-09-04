#!/usr/bin/python

DOCUMENTATION = '''
---
module: freedge.protect
author: Freedge
short_description: Configure a schedule in tsm
'''

EXAMPLES = '''
- name: configure schedule
  configure_schedule:
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
from ansible_collections.freedge.protect.plugins.module_utils.runner import run
import csv


class Schedule(object):

    def __init__(self):
        self.name = ""
        self.cmd = ""

    def froms(self, s):
        self.fromo(s)

    def fromo(self, obj):
        self.name = obj["name"]
        self.cmd = obj["command"]

    def __eq__(self, other):
        return self.cmd == other.cmd


def main():
    argument_spec = dict(credentials=dict(type="dict"), schedule=dict(type="list"), server=dict(type="str"))
    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    server = module.params['server']
    changed = False
    lescript, extra = run(module, server, "query schedule type=administrative format=detailed")
    runningsched = {}
    configsched = {}
    missing = []

    for line in csv.DictReader(lescript, ["name", "description", "command"]):
        s = Schedule()
        s.froms(line)
        runningsched[s.name] = s
    for obj in module.params['schedule']:
        s = Schedule()
        s.fromo(obj)
        configsched[s.name] = s

    for i, j in configsched.items():
        if i in runningsched and j == runningsched[i]:
            pass
        else:
            changed = True
            missing = missing + [i]

    result = {'changed': changed, 'missing': missing}

    module.exit_json(**result)


if __name__ == '__main__':
    main()
