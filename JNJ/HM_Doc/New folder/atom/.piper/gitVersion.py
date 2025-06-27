import subprocess
from utilities.logger import Logger
import shutil
logger = Logger(__name__)
import docker
import os
import re

def run_step(context):
    logger.debug("started")


    logger.debug(context)
    gitCmd = shutil.which("git")
    if not gitCmd:
        logger.error("Git should be installed on this system.")


    client = docker.from_env()

    dockerCmd = shutil.which("docker")
    if not gitCmd:
        logger.error("docker should be installed on this system.")

    cmd = [gitCmd, "rev-parse", "--show-toplevel"]

    src_root =subprocess.check_output(cmd, universal_newlines=True).rstrip()
    logger.info("Git Directory: " + src_root)


    volume_bindings = {
        src_root: {
            'bind': '/repo',
            'mode': 'rw',
        },
    }
    cmd ="/repo -output json -showvariable  SemVer"

    #run container and remove it

    container = client.containers.run(context['gitversion_docker_image'], volumes=volume_bindings, command=cmd, remove=True)
    #todo: add error handling

    semver = container.decode("utf-8").strip()
    if len(semver) > 60:
        logger.debug("[INFO] semver is larger than the required 60 chars. It will need to reformat...")

        regex = r".*INS-\d*-[a-z]*"
        test_semver = semver
        searchINS = re.search(regex, test_semver)
        if not searchINS:
            logger.debug("[ERROR] Unable to extract the INS number from the semver: ", test_semver)
            return -1
        versionString = searchINS.group()

        regex = r"[0-9]+$"
        buildNumberAtTheEndOfString = re.search(regex,test_semver)
        if not buildNumberAtTheEndOfString:
            logger.debug("[ERROR] Unable to extract the build number from the semver: ", test_semver)
            return 1

        buildNum= buildNumberAtTheEndOfString.group()

        semver = versionString+"."+buildNum

        logger.debug("[INFO] semver formatted succesfully to meet the limite requirements: ", semver)

    os.environ["semver"] = semver
    context['semver'] = semver
    print(semver)


def gitVersion_buildServer(context):
    logger.debug(context)
    gitCmd = shutil.which("git")
    if not gitCmd:
        logger.error("Git should be installed on this system.")


    client = docker.from_env()

    dockerCmd = shutil.which("docker")
    if not gitCmd:
        logger.error("docker should be installed on this system.")

    cmd = [gitCmd, "rev-parse", "--show-toplevel"]

    src_root =subprocess.check_output(cmd, universal_newlines=True).rstrip()

    logger.info(f"Git Directory: {src_root}")


    volume_bindings = {
        src_root: {
            'bind': '/repo',
            'mode': 'rw',
        },
    }
    cmd ="/repo -output buildserver"


    container = client.containers.run(context['gitversion_docker_image'], volumes=volume_bindings, command=cmd)







if __name__ == '__main__':

    context ={'gitversion_docker_image' : 'gpsd-devops-docker.rdeidgart/gitversion:5.0.0-linux-debian-9-netcoreapp2.2'}
    run_step(context)
    #gitVersion_buildServer(context)
