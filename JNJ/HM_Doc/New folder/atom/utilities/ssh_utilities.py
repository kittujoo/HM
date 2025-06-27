from utilities.ssh_connection import SSh


def get_remote_dpkg_package_version(package: str, hostname: str, username: str, password: str) -> str:
    command = f"dpkg-query --showformat='${{Version}}' --show {package} 2>/dev/null"
    with SSh(address=hostname, username=username, password=password) as ssh:
        _, command_output = ssh.send_command(command)
        return command_output
