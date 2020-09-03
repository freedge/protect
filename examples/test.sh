#!/bin/sh
cd  `dirname $0`
ansible-galaxy collection install -p ./ ../freedge-protect-*.tar.gz
ansible-playbook isp.yml --check
ret=$?

exit $ret

