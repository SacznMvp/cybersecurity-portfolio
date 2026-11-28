# Saúl Cabezas Guevara | Cybersecurity portfolio

**Junior SOC / Blue Team focus · Log analysis · Networking · Windows and Linux**

[Español](README.md) · [Learning roadmap (Spanish)](ROADMAP.md) · [GitHub](https://github.com/SacznMvp) · [YouTube](https://www.youtube.com/@SACZNCybersecurity)

I am a cybersecurity student focused on SOC and Blue Team work. Through **SACZN Cybersecurity**, I share detection, network analysis and identity labs with documented results and evidence.

**Portfolio:** seven case reports, one lab setup guide, and eleven planned labs.

## Featured SOC cases

| Case | What to review |
|---|---|
| [16 · Wazuh SOC investigation](16-siem-wazuh/README.md) | Linux sudo event, alert 5402 and index verification. The Windows agent is pending. |
| [14 · Active Directory](14-active-directory/README.md) | Domain, DNS and verified sessions, with links to proposed auditing and GPO work. |
| [13 · TLS and Wireshark](13-apache-ssl-wireshark/README.md) | HTTP and HTTPS captures and their implications for network visibility. |
| [17 · Linux permissions and privileges](17-linux-privesc/README.md) | UID and EUID evidence and a pending review of defensive controls. |

## Additional reports

- [11 · Web security with OWASP Juice Shop](11-owasp-juice-shop/README.md).
- [10 · Android static analysis](10-android-reversing/README.md).
- [12 · Apache operations and recovery](12-apache-vhost/README.md). The deployment is documented and tools are available. Recovery in the VM remains pending.

## Python tools

- [Apache log analyzer](tools/apache-log-analyzer/README.md): offline Python CLI, synthetic sample, JSON/CSV reports and automated tests. Indicators support triage, not automatic attribution or attack confirmation.
- [Apache backup helper](tools/apache-backup/README.md): archive plus file hashes; actual VM recovery remains untested.

## Pending work

- [Active Directory GPOs](14-active-directory/GPO-VALIDACION.md) and [Apache hardening](12-apache-vhost/VALIDACION.md): validation plans for the lab VMs.
- [Learning roadmap](ROADMAP.md): full list of planned labs.

## Supporting material

- [01 — VirtualBox and Kali setup](01-laboratorio-virtual/README.md). Base configuration and snapshot recovery. Guest network verification is pending.

License: [MIT](LICENSE).
