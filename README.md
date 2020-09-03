[![Build Status](https://dev.azure.com/freedge/freedge/_apis/build/status/freedge.protect?branchName=master)](https://dev.azure.com/freedge/freedge/_build/latest?definitionId=6&branchName=master)

[Galaxy](https://galaxy.ansible.com/freedge/protect)

# Ansible Collection - freedge.protect

Current status: this is under development and not working yet.

An unofficial module to configure IBM Spectrum Protect. It connects to a server and shoot commands with dsmadmc.


# Usage

```
    - name: configure script
      register: oldscript
      delegate_to: localhost
      configure_script:
        credentials: "{{ credentials }}"
        script: toto
        server: isp123
        content: "{{lookup('file', 'lescript')}}"

    - name: configure schedule
      delegate_to: localhost
      configure_schedule:
        credentials: "{{ credentials }}"
        server: isp124
        schedule:
        - name: CHANGE_AAAAAAAAAAAAAAA
          command: update admin *
        - name: N1234_FULL
          command: run n1234_ndmp full
        
``` 

# Prerequisite

You need a host having already dsmadmc installed with the opt and sys files, or container with dsmadmc. A Dockerfile is provided if you want to build a docker image.

This is inspired by https://spdocker.static.leenooks.net/client/. 



# Installation

## From galaxy 

```
ansible-galaxy collection install freedge.protect
```

## From sources
```
ansible-galaxy collection build
cd /myproject
ansible-galaxy collection install -p ./ ...freedge-protect-0.0.1.tar.gz
```


