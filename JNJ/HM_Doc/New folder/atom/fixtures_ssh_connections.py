import time

import pytest
import sshtunnel


@pytest.fixture(scope='session')
def isym_port_forwarder(isym_config):

    tunnels = []

    def port_forward(host: str, port: int):
        tunnel = sshtunnel.open_tunnel(
            ssh_address_or_host=(isym_config.hostname, 22),
            remote_bind_address=(host, port),
            ssh_username=isym_config.username,
            ssh_password=isym_config.password
        )
        tunnel.start()
        time.sleep(2)
        tunnels.append(tunnel)
        return tunnel.local_bind_port

    yield port_forward
    for item in tunnels:
        item.close()
