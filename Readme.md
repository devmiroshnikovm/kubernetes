## Project description

Create docker image first:

```bash
./run_build.sh
```

### /playbok - Ansible section

Ansible playbook with ansible-vault to protect sensitive data.

#### Usage

```bash
ansible-playbook -i ./inventory.ini ./playbook.yaml \
-u "user" -k -K --ask-vault-pass
```

ansible-vault password: testpass

#### Tested

Tested on Ubuntu 22.04.3 LTS

### /app - application source

Web app, written on python.

#### API Endpoints

- /
- /hostname
- /author
- /id
- /healthz
- /readiness

### /manifest - kubernetes section

See deployment.yaml

#### Tested

Tested locally on Kubernetes cluster v1.26.5, deployed by kuberspray.

- srv01 (virtualized Ubuntu server on VMware Fusion) - control-plane
- srv02 (virtualized Ubuntu server on VMware Fusion) - worker

### /helm - helm section

Helm section.

## Contacts

Telegram: @miklemir
Github: devmiroshnikovm
