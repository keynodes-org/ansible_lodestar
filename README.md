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
    - role: keynodes.ansible_lodestar
```

Variables
===============

Ansible role for deploying Lodestar Ethereum Beacon node

## Auto-generated

- [Defaults](#default-vars)
  - [lodestar_beacon_node_binary_download_url](#lodestar_beacon_node_binary_download_url)
  - [lodestar_beacon_node_binary_name](#lodestar_beacon_node_binary_name)
  - [lodestar_beacon_node_binary_version](#lodestar_beacon_node_binary_version)
  - [lodestar_beacon_node_custom_config](#lodestar_beacon_node_custom_config)
  - [lodestar_beacon_node_default_config](#lodestar_beacon_node_default_config)
  - [lodestar_beacon_node_dir_base](#lodestar_beacon_node_dir_base)
  - [lodestar_beacon_node_dir_base_config](#lodestar_beacon_node_dir_base_config)
  - [lodestar_beacon_node_dir_base_data](#lodestar_beacon_node_dir_base_data)
  - [lodestar_beacon_node_dir_base_log](#lodestar_beacon_node_dir_base_log)
  - [lodestar_beacon_node_dir_binary](#lodestar_beacon_node_dir_binary)
  - [lodestar_beacon_node_dir_config](#lodestar_beacon_node_dir_config)
  - [lodestar_beacon_node_dir_data](#lodestar_beacon_node_dir_data)
  - [lodestar_beacon_node_dir_log](#lodestar_beacon_node_dir_log)
  - [lodestar_beacon_node_dir_systemd](#lodestar_beacon_node_dir_systemd)
  - [lodestar_beacon_node_general_owner](#lodestar_beacon_node_general_owner)
  - [lodestar_beacon_node_group](#lodestar_beacon_node_group)
  - [lodestar_beacon_node_jwt_secret](#lodestar_beacon_node_jwt_secret)
  - [lodestar_beacon_node_launch_mode](#lodestar_beacon_node_launch_mode)
  - [lodestar_beacon_node_rc_config_path](#lodestar_beacon_node_rc_config_path)
  - [lodestar_beacon_node_reinstall](#lodestar_beacon_node_reinstall)
  - [lodestar_beacon_node_systemd_service_name](#lodestar_beacon_node_systemd_service_name)
  - [lodestar_beacon_node_user](#lodestar_beacon_node_user)
- [Tags](#tags)

- [Dependencies](#dependencies)

---

## Defaults

### lodestar_beacon_node_binary_download_url

URL to download the Lodestar binary (includes version).

#### Defaults

```YAML
lodestar_beacon_node_binary_download_url: https://github.com/ChainSafe/lodestar/releases/download/v{{
  lodestar_beacon_node_binary_version }}/lodestar-v{{ lodestar_beacon_node_binary_version
  }}-linux-amd64.tar.gz
```

### lodestar_beacon_node_binary_name

Name of the Lodestar binary executable.

#### Defaults

```YAML
lodestar_beacon_node_binary_name: lodestar
```

### lodestar_beacon_node_binary_version

Version of the Lodestar binary.

#### Defaults

```YAML
lodestar_beacon_node_binary_version: 1.28.1
```

### lodestar_beacon_node_custom_config

Custom configuration options for the Lodestar beacon node client.

#### Defaults

```YAML
lodestar_beacon_node_custom_config: {}
```

### lodestar_beacon_node_default_config

List of default CLI configuration options for the Lodestar beacon node.

#### Defaults

```YAML
lodestar_beacon_node_default_config:
  - name: dataDir
    description: Lodestar root data directory (string)
    value: '{{ lodestar_beacon_node_dir_data }}'
  - name: network
    description: Name of the Ethereum Consensus chain network to join (string)
    value: hoodi
  - name: forceCheckpointSync
    description: Force sync from checkpoint state even if DB is within WSS period
      (boolean)
    value: false
  - name: ignoreWeakSubjectivityCheck
    description: Ignore failing the weak subjectivity check (boolean)
    value: false
  - name: logLevel
    description: Logging verbosity for terminal output (string)
    value: info
  - name: logFileLevel
    description: Logging verbosity level for file (string)
    value: debug
  - name: logFileDailyRotate
    description: Number of log files to retain during daily rotation (number)
    value: 5
  - name: rest
    description: Enable/disable the HTTP API (boolean)
    value: true
  - name: rest.namespace
    description: Namespaces to expose for the HTTP API (string[])
    value:
      - beacon
      - config
      - debug
      - events
      - node
      - validator
      - lightclient
  - name: rest.cors
    description: CORS setting for the HTTP API (string)
    value: '*'
  - name: rest.address
    description: HTTP API host address (string)
    value: 127.0.0.1
  - name: rest.port
    description: HTTP API port (number)
    value: 9596
  - name: suggestedFeeRecipient
    description: Default EL block fee recipient (20-byte hex) (string)
    value: '0x0000000000000000000000000000000000000000'
  - name: emitPayloadAttributes
    description: Emit execution payload attributes via SSE (boolean)
    value: false
  - name: eth1
    description: Follow the eth1 chain (boolean)
    value: true
  - name: eth1.providerUrls
    description: List of ETH1 node RPC URLs (string[])
    value:
      - http://localhost:8545
  - name: execution.urls
    description: List of Execution client engine API URLs (string[])
    value:
      - http://localhost:8551
  - name: execution.timeout
    description: Timeout in ms for execution engine calls (number)
    value: 12000
  - name: execution.retries
    description: Number of retries for execution engine calls (number)
    value: 2
  - name: execution.retryDelay
    description: Delay in ms between execution engine retries (number)
    value: 2000
  - name: builder.url
    description: Builder API URL (string)
    value: http://localhost:8661
  - name: builder.timeout
    description: Timeout in ms for builder API (number)
    value: 12000
  - name: metrics.port
    description: Port for Prometheus metrics HTTP server (number)
    value: 8008
  - name: metrics.address
    description: HTTP server address for Prometheus metrics (string)
    value: 127.0.0.1
  - name: monitoring.interval
    description: Interval in ms between sending client stats (number)
    value: 60000
  - name: discv5
    description: Enable discv5 peer discovery (boolean)
    value: true
  - name: listenAddress
    description: IPv4 address for p2p communication (string)
    value: 0.0.0.0
  - name: port
    description: TCP/UDP port for IPv4 (number)
    value: 9000
  - name: port6
    description: TCP/UDP port for IPv6 (number)
    value: 9090
  - name: bootnodes
    description: List of bootnodes for discv5 discovery (string[])
    value:
      - enr:-Ku4QHqVeJ8PPICcWk1vSn_XcSkjOkNiTg6Fmii5j6vUQgvzMc9L1goFnLKgXqBJspJjIsB91LTOleFmyWWrFVATGngBh2F0dG5ldHOIAAAAAAAAAACEZXRoMpC1MD8qAAAAAP__________gmlkgnY0gmlwhAMRHkWJc2VjcDI1NmsxoQKLVXFOhp2uX6jeT0DvvDpPcU8FWMjQdR4wMuORMhpX24N1ZHCCIyg
      - enr:-Ku4QG-2_Md3sZIAUebGYT6g0SMskIml77l6yR-M_JXc-UdNHCmHQeOiMLbylPejyJsdAPsTHJyjJB2sYGDLe0dn8uYBh2F0dG5ldHOIAAAAAAAAAACEZXRoMpC1MD8qAAAAAP__________gmlkgnY0gmlwhBLY-NyJc2VjcDI1NmsxoQORcM6e19T1T9gi7jxEZjk_sjVLGFscUNqAY9obgZaxbIN1ZHCCIyg
      - enr:-Ku4QPn5eVhcoF1opaFEvg1b6JNFD2rqVkHQ8HApOKK61OIcIXD127bKWgAtbwI7pnxx6cDyk_nI88TrZKQaGMZj0q0Bh2F0dG5ldHOIAAAAAAAAAACEZXRoMpC1MD8qAAAAAP__________gmlkgnY0gmlwhDayLMaJc2VjcDI1NmsxoQK2sBOLGcUb4AwuYzFuAVCaNHA-dy24UuEKkeFNgCVCsIN1ZHCCIyg
      - enr:-Ku4QEWzdnVtXc2Q0ZVigfCGggOVB2Vc1ZCPEc6j21NIFLODSJbvNaef1g4PxhPwl_3kax86YPheFUSLXPRs98vvYsoBh2F0dG5ldHOIAAAAAAAAAACEZXRoMpC1MD8qAAAAAP__________gmlkgnY0gmlwhDZBrP2Jc2VjcDI1NmsxoQM6jr8Rb1ktLEsVcKAPa08wCsKUmvoQ8khiOl_SLozf9IN1ZHCCIyg
  - name: targetPeers
    description: Target number of connected peers (number)
    value: 100
  - name: subscribeAllSubnets
    description: Subscribe to all subnets (boolean)
    value: false
  - name: disablePeerScoring
    description: Disable peer scoring (boolean)
    value: false
  - name: mdns
    description: Enable mDNS local peer discovery (boolean)
    value: false
```

### lodestar_beacon_node_dir_base

Lodestar base directory.

#### Defaults

```YAML
lodestar_beacon_node_dir_base: /opt
```

### lodestar_beacon_node_dir_base_config

Base directory for Lodestar configuration files (derived from base directory).

#### Defaults

```YAML
lodestar_beacon_node_dir_base_config: '{{ lodestar_beacon_node_dir_base }}/config'
```

### lodestar_beacon_node_dir_base_data

Base directory for Lodestar data (derived from base directory).

#### Defaults

```YAML
lodestar_beacon_node_dir_base_data: '{{ lodestar_beacon_node_dir_base }}/data'
```

### lodestar_beacon_node_dir_base_log

Base directory for Lodestar log files.

#### Defaults

```YAML
lodestar_beacon_node_dir_base_log: '{{ lodestar_beacon_node_dir_base }}/log'
```

### lodestar_beacon_node_dir_binary

Directory for installing the Lodestar binary.

#### Defaults

```YAML
lodestar_beacon_node_dir_binary: /usr/local/bin
```

### lodestar_beacon_node_dir_config

Directory for Lodestar beacon node configuration files.

#### Defaults

```YAML
lodestar_beacon_node_dir_config: '{{ lodestar_beacon_node_dir_base_config }}/lodestar-beacon-node'
```

### lodestar_beacon_node_dir_data

Directory for Lodestar beacon node data.

#### Defaults

```YAML
lodestar_beacon_node_dir_data: '{{ lodestar_beacon_node_dir_base_data }}/lodestar-beacon-node'
```

### lodestar_beacon_node_dir_log

Directory for Lodestar beacon node log files.

#### Defaults

```YAML
lodestar_beacon_node_dir_log: '{{ lodestar_beacon_node_dir_base_log }}/lodestar-beacon-node'
```

### lodestar_beacon_node_dir_systemd

Directory where systemd service files are stored.

#### Defaults

```YAML
lodestar_beacon_node_dir_systemd: /lib/systemd/system
```

### lodestar_beacon_node_general_owner

General owner for Lodestar system files.

#### Defaults

```YAML
lodestar_beacon_node_general_owner: root
```

### lodestar_beacon_node_group

Group for running the Lodestar beacon node.

#### Defaults

```YAML
lodestar_beacon_node_group: lodestar
```

### lodestar_beacon_node_jwt_secret

File path to the JWT secret for engine API authentication.

#### Defaults

```YAML
lodestar_beacon_node_jwt_secret: '{{ lodestar_beacon_node_dir_config }}/jwt'
```

### lodestar_beacon_node_launch_mode

Launch mode for the Lodestar node (beacon, validator, lightclient, dev).

#### Defaults

```YAML
lodestar_beacon_node_launch_mode: beacon
```

### lodestar_beacon_node_rc_config_path

Path to the Lodestar runtime configuration file.

#### Defaults

```YAML
lodestar_beacon_node_rc_config_path: '{{ lodestar_beacon_node_dir_config }}/rc-config.yml'
```

### lodestar_beacon_node_reinstall

Flag to control reinstallation of the Lodestar beacon node.

#### Defaults

```YAML
lodestar_beacon_node_reinstall: false
```

### lodestar_beacon_node_systemd_service_name

Systemd service name for the Lodestar beacon node.

#### Defaults

```YAML
lodestar_beacon_node_systemd_service_name: lodestar-beacon-node
```

### lodestar_beacon_node_user

Username for the Lodestar beacon node.

#### Defaults

```YAML
lodestar_beacon_node_user: lodestar
```

## Tags

**_lodestar-config_**

**_lodestar-install_**

**_lodestar-prepare_**

## Dependencies

None.
