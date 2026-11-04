# Kubernetes Security

## ExaAiAgent surface

- Prompt module: `kubernetes_security` (select via `--prompt-modules`).
- Tool group: `exaaiagnt/tools/k8s_scanner/`.

## What to check (authorized clusters only)

1. **RBAC**: over-privileged service accounts, cluster-admin bindings,
   wildcard verbs/resources.
2. **Workload security**: privileged containers, hostPath/hostNetwork,
   writable root filesystems, dropped capabilities missing.
3. **Secrets**: Secrets mounted as env vars, hard-coded credentials,
   long-lived tokens, missing rotation.
4. **Network policy**: default-deny absent, overly broad ingress/egress.
5. **Admission**: no Pod Security Standards / admission control,
   unpinned images (`:latest`), mutable tags.
6. **API server**: anonymous auth, exposed kubelet, insecure ports.
7. **Supply chain**: untrusted registries, missing image signatures.

## Workflow

```bash
exaai -t <authorized-cluster-or-manifests> \
  --prompt-modules kubernetes_security -n \
  --output-format json --output-dir exaai_runs
```

Report manifest findings with file/line references; report live-cluster
findings with namespace/object names. Never exfiltrate Secrets content —
report presence and risk, redacting values.
