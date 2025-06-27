import subprocess


def get_dpkg_package_version(package: str) -> str:
    command = f"dpkg-query --showformat='${{Version}}' --show {package} 2>/dev/null"
    return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read().decode()


def get_browser_version(package: str) -> str:
    command = f"{package} --version"
    return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read().decode()
