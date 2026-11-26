# SACZN | Cybersecurity portfolio

**Junior SOC / Blue Team focus · Log analysis · Networking · Windows and Linux**

[Español](README.md) · [Learning roadmap (Spanish)](ROADMAP.md) · [GitHub](https://github.com/SacznMvp) · [YouTube](https://www.youtube.com/@SACZNCybersecurity)

I am a cybersecurity student building practical labs to understand systems, investigate risks and document defensive improvements. My career goal is a junior SOC / Blue Team role.

**Status:** seven labs with reports and twelve planned labs.

## Documented labs

- [01 — VirtualBox and Kali lab](01-laboratorio-virtual/README.md): boot, internal network configuration and snapshot recovery.
- [10 — Android static analysis](10-android-reversing/README.md): APKTool/JADX observations; exploitation claims require additional evidence.
- [11 — Web security](11-owasp-juice-shop/README.md): scoped assessment and an authentication bypass case study.
- [12 — Apache Virtual Hosts](12-apache-vhost/README.md): working local site; operational backup/restore validation is pending.
- [13 — Apache TLS](13-apache-ssl-wireshark/README.md): self-signed certificate and HTTP/HTTPS packet analysis.
- [14 — Active Directory](14-active-directory/README.md): internal network, domain and client enrollment.
- [17 — Linux privilege escalation](17-linux-privesc/README.md): SUID, cron and weak file permissions in Metasploitable 2; remediation and retesting remain pending.

Each lab links to its report, screenshots and results in Spanish. See the lab READMEs and [technical review notes](docs/REVISION-TECNICA.md) for details.

## Python tools

- [Apache log analyzer](tools/apache-log-analyzer/README.md): offline Python CLI, synthetic sample, JSON/CSV reports and automated tests. Indicators support triage, not automatic attribution or attack confirmation.
- [Apache backup helper](tools/apache-backup/README.md): archive plus file hashes; actual VM recovery remains untested.

## Pending work

- [Wazuh](16-siem-wazuh/README.md): the guide is ready. Setup, event collection and alert investigation are pending.
- [Active Directory GPOs](14-active-directory/GPO-VALIDACION.md) and [Apache hardening](12-apache-vhost/VALIDACION.md): validation plans for the lab VMs.
- [Learning roadmap](ROADMAP.md): full list of planned labs.

License: [MIT](LICENSE).
