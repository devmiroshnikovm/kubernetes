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

Kubernetes manifest. See deployment.yaml

#### Tested

Tested locally on Kubernetes cluster v1.26.5, deployed by kuberspray.

- srv01 (virtualazed Ubuntu server on VMware Fusion) - control-plane
- srv02 (virtualazed Ubuntu server on VMware Fusion) - worker

### /helm - helm section

Helm section.
Create namespace first:

```bash
kubectl create namespace my-app-namespace
helm install my-flask-app-release ./helm/ --namespace my-app-namespace
```

## Contacts

Telegram: @miklemir
Github: devmiroshnikovm