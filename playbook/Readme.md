## Usage/Examples

```bash
ansible-playbook -i ./inventory.ini ./playbook.yaml \
-u "user" -k -K --ask-vault-pass
```

### Encrypted data

```bash
ansible-vault view ./group_vars/users.yaml
```

ansible-vault password: testpass
