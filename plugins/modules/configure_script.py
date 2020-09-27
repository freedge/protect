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
from ansible_collections.freedge.protect.plugins.module_utils.runner import run, creds


def main():
    argument_spec = dict(
        credentials=creds(),
        script=dict(type="str"),
        server=dict(type="str"),
        content=dict(type="str")
    )
    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    script = module.params['script']
    server = module.params['server']
    content = module.params['content']
    changed = False
    lescript, extra = run(module, server, "query script %s format=raw" % script)

    lediff = []
    for i, j in enumerate(content.split("\n")):
        if i >= len(lescript) or j + "\n" != lescript[i]:
            lediff += [j]
    changed = len(lediff) > 0

    result = {'changed': changed, 'running': lescript, 'all': extra, 'lediff': lediff}

    module.exit_json(**result)


if __name__ == '__main__':
    main()
