import os
import subprocess

from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))


def is_process_running(process_name):
    output = subprocess.Popen(['TASKLIST', '/FI', f"imagename eq {process_name}"], shell=True, stdout=subprocess.PIPE).stdout.readlines()
    result = process_name.lower() in output[-1].decode().lower() if output else False

    logger.debug(f"Process [{process_name}] is {'running' if result else 'not running'}")

    return result


def is_application_installed(package_name):
    output = subprocess.check_output(['psinfo', '-nobanner', '-s', '/accepteula']).decode().split('\r\n')
    output = output[output.index("Applications:") + 1:]
    return len([x for x in output if package_name in x]) > 0


def kill_application(executable: str) -> bool:
    output = subprocess.run(['taskkill', '/IM', executable.split('\\')[-1], '/F'])
    if output.returncode:
        return False
    return True


def uninstall_application(app_name: str) -> bool:
    command = ['winget', 'uninstall', '--name', app_name, '--accept-source-agreements']
    exit_code = subprocess.call(command, shell=True, stdout=subprocess.DEVNULL)
    return exit_code == 0
