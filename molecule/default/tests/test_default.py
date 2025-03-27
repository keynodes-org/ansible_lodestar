import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


@pytest.mark.parametrize(
    "directory",
    [
        "/opt",
        "/opt/data",
        "/opt/config",
        "/opt/log",
    ]
)
def test_base_directories(host, directory):
    d = host.file(directory)
    assert d.exists
    assert d.is_directory
    assert d.user == "root"
    assert d.group == "root"

@pytest.mark.parametrize(
    "directory",
    [
        "/opt/data/lodestar-beacon-node",
        "/opt/config/lodestar-beacon-node",
        "/opt/log/lodestar-beacon-node"
    ]
)
def test_directories(host, directory):
    d = host.file(directory)
    assert d.exists
    assert d.is_directory
    assert d.user == "lodestar"
    assert d.group == "lodestar"

@pytest.mark.parametrize(
    "file",
    [
        "/usr/local/bin/lodestar",
        "/lib/systemd/system/lodestar-beacon-node.service",
        "/opt/config/lodestar-beacon-node/rc-config.yml"
    ],
)
def test_files(host, file):
    f = host.file(file)
    assert f.exists
    assert f.is_file


@pytest.mark.parametrize("service", ["lodestar-beacon-node"])
def test_service(host, service):
    s = host.service(service)
    assert s.is_running
    assert s.is_enabled


@pytest.mark.parametrize("socket", ["tcp://127.0.0.1:9596"])
def test_socket(host, socket):
    s = host.socket(socket)
    assert s.is_listening


@pytest.mark.parametrize("command", ["curl -s 127.0.0.1:9596"])
def test_get_metrics(host, command):
    c = host.run(command)
    assert c.stderr == ""
    assert c.succeeded
