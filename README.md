[Galaxy](https://galaxy.ansible.com/freedge/protect)

# Ansible Collection - freedge.protect

Current status: this is under development and not working yet.

An unofficial module to configure IBM Spectrum Protect. It connects to a server and shoot commands with dsmadmc.



# Prerequisite

You need a host having already dsmadmc installed with the opt and sys files, or container with dsmadmc. A Dockerfile is provided if you want to build a docker image.

This is inspired by https://spdocker.static.leenooks.net/client/. 


# Usage

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

