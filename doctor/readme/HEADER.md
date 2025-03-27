Lodestar
=========

Lodestar beacon node role

**Tests:**
* Ubuntu 22.04 (jammy)

How to run molecule tests
----------------------

```shell
python3 -m venv venv
pip install -r requirements.txt
source venv/bin/activate
make init
make test
```

Make
----

`make init` - Prepare environment
`make test` - Run molecule tests (`molecule -v test`)  
`make docs` - Auto-generate `README` (`ansible-doctor`)

Role install
--------------

You can install role by using `ansible-galaxy`:

```shell
ansible-galaxy role install git+git@github.com:keynodes-org/ansible_lodestar.git
```

For particular version of this role:
```shell
ansible-galaxy role install git+git@github.com:keynodes-org/ansible_lodestar.git,main
```

Update to latest version:
```shell
ansible-galaxy role install git+git@github.com:keynodes-org/ansible_lodestar.git --upgrade
```

Example of using in `requirements.yml`:
```yaml
---
roles:
  - name: lodestar
    src: git+git@github.com:keynodes-org/ansible_lodestar.git 
    version: main
```

How to use in playbook:
-------------------------

```yaml
- hosts: ansible_hostname
  roles:
    - role: ansible-lodestar
```

Variables
===============
