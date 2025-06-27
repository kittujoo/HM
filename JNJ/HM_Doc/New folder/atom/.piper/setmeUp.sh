#! /bin/bash

# Exit if command returns non-zero
set -e

# Needed variables
TempRepoFolder="${PWD}/.piper"
iacRepoFolder="${TempRepoFolder}/iac"
ansibleAgentPlaybookFolder="${iacRepoFolder}/build-agent"
iacRepoUrl="ssh://git@bitbucketprod1.waters.com:7999/devops/iac.git"
branch=$(git rev-parse --abbrev-ref HEAD)
echo "[INFO] Setting up the docker registry"
export username=$(curl -X GET http://10.9.3.22:8000/accounts/ | python3 -c 'import json,sys;obj=json.load(sys.stdin);print(obj[0]["account"])')
export password=$(curl -X GET http://10.9.3.22:8000/accounts/ | python3 -c 'import json,sys;obj=json.load(sys.stdin);print(obj[0]["password"])')
export docker_registry="gpsd-devops-docker.rdeidgart"

# set which cluster type to use based on the branch. Currently there's only one active cluster, so its always dev.
if [ "$branch" == "develop" ]; then
   export KUBE_CLUSTER_TYPE=dev
else
   export KUBE_CLUSTER_TYPE=dev
fi

kubeFolder="${HOME}/.kube"
kubectlCmd="kubectl config current-context"

# Change directory location into the folder this script is being run out of
echo "[INFO] Current folder is:  " `pwd`
echo "[INFO] Changing into folder script is being run out of..."
SCRIPT_PATH=${0%/*}
cd $SCRIPT_PATH
echo "[INFO] New current folder is:  " `pwd`

echo "[INFO] Setting the environment"

echo "[INFO] Install python3"
sudo apt install python3 python3-pip -y

echo "[INFO] Install pip requirements"
pip3 install -r Requirements.txt

echo "[INFO] Installing Curl"
sudo apt-get install curl --assume-yes

echo "[INFO] Configure Build Agent with Ansible..."

# Clone repository into temp repo folder
echo "[INFO] Cloning iac Repository into $iacRepoFolder..."
git clone $iacRepoUrl $iacRepoFolder

# Make sure ansible is installed
echo "[INFO] Checking for and installing ansible if necessary"
if ! apt list --installed | grep ansible
then
   echo "[INFO] Installing ansible"
   # Setup the official ansible repository to get the latest ansible
   sudo apt-add-repository ppa:ansible/ansible -y

   # Get the latest lists so the new ppa packages are listed
   sudo apt update

   # Install ansible from the new ppa
   sudo apt install ansible=2.8.5-1ppa~bionic -y # if the version here is used again elsewhere, this must be parameterized
fi

# Run the ansible script
echo "[INFO] Executing ansible..."
pushd $ansibleAgentPlaybookFolder
echo "   [INFO] Getting Vault Password..."
curl -X GET http://10.9.3.22:8000/accounts/ |python3 -c 'import json,sys;obj=json.load(sys.stdin);print(obj[1]["password"])' > $ansibleAgentPlaybookFolder/vault.txt
echo "   [INFO] Launching Playbook..."
ansible-playbook --vault-password-file=$ansibleAgentPlaybookFolder/vault.txt build-agent.yaml
echo "   [INFO] Cleaning up..."
rm -r $ansibleAgentPlaybookFolder/vault.txt
popd
echo "[INFO] Ansible Complete"


sudo chown ${USER}:${USER} -R ${PWD}
echo "[INFO] Done"
