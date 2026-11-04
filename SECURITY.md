# Security Policy

## Scope

This policy covers the ExaAiAgent-Skill package (docs, scripts, templates,
schemas, tests). It does **not** cover upstream ExaAiAgent vulnerabilities —
report those to https://github.com/hleliofficiel/ExaAiAgent.

## Authorized testing only

ExaAiAgent is a penetration-testing tool. Use it only against systems you
own or have explicit authorization to test. See `references/safety-policy.md`.

## Reporting a vulnerability in this skill package

- Open a private security advisory on the skill repository, or contact the
  maintainers directly. Do not open a public issue for a vulnerability.
- Include: affected file/version, reproduction steps, and impact.
- We aim to acknowledge within 3 business days and ship a fix or mitigation
  as soon as practical.

## Safe handling

- Never commit secrets, API keys, or credentials.
- Scripts must not use `shell=True`, `eval`, or unsafe deserialization.
- Reports generated from real runs may contain sensitive target data —
  handle them as confidential and redact secrets before sharing.
