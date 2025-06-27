# Welcome to ATOM

This space contains all the necessary scripts, libraries, and test suite supporting the ATOM testing framework.

## Prerequisites for changing the code:
- Python 3.8.10
- Pycharm 2023.1 or later
- or Visual Studio Code with extensions (Python, Pytest IntelliSense, Pytest BDD, Gherkin). Check .vscode\extensions.json
- Java in PATH in order to display Allure reports

- Disable checkbox "Keep my email addresses private" in "Emails" section of your GitHub account. This is for properly identifying changes in the repo after using the "Squash & Merge" option on pull requests.

- After cloning the repo, run the below command. This will help with branch naming convention checks and will prefix each commit with JIRA ticket id.
    Every user must apply local .gitconfig file by executing:
```
git config --local include.path ../.gitconfig
```

## Running atom.py

### Before test execution you need to:
- Create virtual env
  - by running `python -m venv venv`
  - or using embedded features of Pycharm or VS Code
- Activate venv:
   - Windows:  cmd `venv\Scripts\activate.bat` or in Powershell prompt `.\venv\Scripts\Activate.ps1`
   - Linux: `. venv/Scripts/activate`
- Install pip requirements:
  - `python -m pip install -r requirements/all_dependencies.txt`

#### Parameters to clone isym-interface on local environment
            Note: used only when developing new rest api tests, not for tests execution
   - --isym_interface_repo_password: isym-interface repository user token/password for the isym-interface
   - --isym_interface_version: Version (branch name/tag/commitId) of isym-interface to clone. If "auto" is provided, isym-interface module's commitId will be used from isym-application repository
   - --isym_interface_download_only: Only clone and build isym-interface, code will not be copied to host and tests execution will not be triggered. False by default

#### Parameters which could be used for any environment
   - --skip_atom_copying or simply -s: Executes the given tests on the host, skipping atom code copying (could be used if the code exists on host)
   - --delete: When set, atom remote folder will be deleted from the target host after test execution
   - --log-cli-level=INFO: Sets pytest cli log level, that can make pytest more verbose (log level can be different, ERROR, INFO, DEBUG, etc)
   - --timeout: Sets the overall test execution timeout. The default is 7200 seconds

### Executing isym\kiosk tests against Simulation environment:
Can be executed against an AWS VM created using Piper Core: http://gpsd-piper-core.rdeadmin.waters.com/aws/deploy/

```
python atom.py --environment=SIMULATION --host=<aws_vm_ip> --host_username=user --host_password=<user_password> --host_atom_folder=ATOM --test_filter="rest_api_get_state or kiosk_smoke_test_access"
```
Where:
   - --host: Host IP of the target machine where the tests will be executed
   - --host_username: User name for ssh connection to the target host machine
   - --host_password: Password for ssh connection to the target host machine
   - --port: Target ssh host port. Default to 22
   - --host_atom_folder: Folder name on target host machine to be used as atom source storage and working directory
   - --test_filter: filter that will be used to define test scope (tags from isym\kiosk feature files)

### Executing isym\kiosk tests against Real environment:
    In order to run tests on real system, atom code will be copied via a jump server (Empower machine) to the target real instrument.
    It will run the tests in a docker container on the ISPP board. It will use the internal network to access iSym board for logs.

```
python atom.py --environment=REAL --jump_server_host=<empower_machine_ip> --jump_server_username=user --jump_server_password=<user_password> \
--system_network_name=BPFSYS-011 --host_username=admin --host_password=<admin_password> --host_atom_folder=ATOM
--run_in_docker_image=atom:<custom_docker_image_name> --run_in_docker_password=<docker_artifactory_password> --test_filter="rest_api_get_state or kiosk_smoke_test_access"
```
Where:
   - --jump_server_host: Name or IP address of the ssh jump server (Empower machine)
   - --jump_server_username: Username of ssh jump server
   - --jump_server_password: Password of ssh jump server
   - --jump_server_port: Port of ssh jump server

   - --system_network_name: instrument system unit ISPP network name as it appears in Empower DHCP. Should not be used together with --host as the identified IP will be sent automatically as --host
   - --host: if the IP from Empower DHCP is known, then it can be sent directly without using also --system_network_name (but this IP can change after each instrument reboot)
   - --host_username: User name for ssh connection to the target host machine
   - --host_password: Password for ssh connection to the target host machine
   - --port: Target ssh host port. Default to 22
   - --host_atom_folder: Folder name on target host machine to be used as atom source storage and working directory

   - --run_in_docker_password: Password for Docker registry in Artifactory
   - --run_in_docker_registry: Configure docker registry name, 'waters-ics-lc-docker-local.jfrog.io' by default
   - --run_in_docker_image: Configure docker image name to run test, 'atom:latest' by default

   - --test_filter: filter that will be used to define test scope (tags from feature files designed to execute isym\kiosk tests on real instrument)


### Installing new system swu file on Real environment:
    In order to install a differet build on real system, atom code will be copied on the jump server (Empower machine) to trigger the updateof the system.

```
python atom.py --host=<empower_machine_ip> --host_atom_folder=ATOM --host_username=user --host_password=<user_password> --system_swu_version=<swu file version>
```
Where:
   - --host: IP of the Empower machine connected to the system. This needs to be a VM based on the atom template
   - --host_username: Username for Empower machine
   - --host_password: Password for Empower machine
   - --system_swu_version: swu file version. e.g:1.2.0-Eval.10


### Executing tests against CDS (Empower) environment:
```
python atom.py --environment=CDS --host=<empower_machine_ip> --host_username=user --host_password=<user_password> --host_atom_folder=ATOM --ics_version=OrionICS-1.0.0 --test_filter="ics_smoke_test"
```
Where:
   - --host: IP of the Empower machine where the tests will be executed. This needs to be a VM based on the atom template
   - --host_username: Username for Empower machine
   - --host_password: Password for Empower machine
   - --port: Target ssh host port. Default to 22
   - --host_atom_folder: Folder name on target host machine to be used as atom source storage and working directory
   - --ics_version: Version of ICS to download on the target host machine. If value is 'undefined' or if --skip_atom_copying is used, ICS will not be copied on the remote host. This is needed only if you are running an installation scenario
   - --test_filter: Filter that will be used to define test scope (tags from ICS feature files)

### Executing Kiosk tests from local machine against the SIMULATION env:
#### You need to have Chrome and related ChromeDriver installed on your machine. ChromeDriver executable folder should be added to PATH
```
python atom.py --ispp_hostname=<SIMULATION_env_ip> --run_on_local --environment=SIMULATION --test_filter="kiosk_smoke_test_access" --no-headless
```
Where:
   - --ispp_hostname: IP of the Simulation env where Kiosk is installed
   - --environment: Environment type (currently only SIMULATION is supported)
   - --no-headless: Disables headless mode for browser
   - --test_filter: Filter that will be used to define test scope (tags from Kiosk feature files)
### Generate single file allure report:

#### Windows
```
scripts\allureGenerateFile.bat
```

#### Linux
```
scripts/allureGenerateFile.sh
```

#### Single file report will always be saved to "results/allure-report/index.html" file.

## Configuring the project
### You can provide custom values for any property that is defined in "config/default_setting.toml" file by
- changing values in file directly (but please avoid this to eliminate situation of committing settings changes)
- set environment variable with "ATOM" prefix, e.g.: ATOM_ISYM_HOSTNAME for "isym_hostname" property

#### There is ability to store sensitive data like passwords in "config/.secrets.toml" file
- you need to create ".secrets.toml" (started with dot) in "config" folder because this file will be ignored during commit
- add property and value for specific scope and save, e.g.:
```
[DEFAULT]
isym_interface_repo_password = "isym token here"
[REAL]
instrument_username = "admin"
instrument_password = "admin password"
```