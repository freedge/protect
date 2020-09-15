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

    def __init__(self, obj):
        self.name = obj["name"]
        self.domain = obj["domain"]
        self.options = obj["options"]

    def __eq__(self, other):
        return self.options == other.options


def main():
    argument_spec = dict(credentials=dict(type="dict"), schedule=dict(type="list"), server=dict(type="str"))
    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    server = module.params['server']
    changed = False
    lescript, extra = run(module, server, "query schedule format=detailed")
    runningsched = {}
    configsched = {}
    missing = []

    for line in csv.DictReader(lescript, ["domain", "name", "description", "action", "subaction", "options"]):
        s = Schedule(line)
        runningsched[(s.domain, s.name)] = s
    for obj in module.params['schedule']:
        s = Schedule(obj)
        configsched[(s.domain, s.name)] = s

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
