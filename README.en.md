# SACZN | Cybersecurity portfolio

**Junior SOC / Blue Team focus · Log analysis · Networking · Windows and Linux**

[Español](README.md) · [Learning roadmap (Spanish)](ROADMAP.md) · [GitHub](https://github.com/SacznMvp) · [YouTube](https://www.youtube.com/@SACZNCybersecurity)

I am a cybersecurity student building practical labs to understand systems, investigate risks and document defensive improvements. My career goal is a junior SOC / Blue Team role.

**Status:** five labs with historical reports, fourteen planned labs in the original roadmap, and one additional Python analysis tool.

## Featured work

| Project | Documented outcome | Defensive relevance |
|---|---|---|
| [Active Directory](14-active-directory/README.md) | Domain/DNS deployment, two domain clients and session evidence | Windows identity and authentication context |
| [HTTP versus HTTPS](13-apache-ssl-wireshark/README.md) | Wireshark comparison of readable HTTP and encrypted TLS records | Network visibility and its limitations |
| [OWASP Juice Shop](11-owasp-juice-shop/README.md) | Authentication bypass documented in a local vulnerable application | Understanding attack behavior for investigation |

## Documented labs

- [10 — Android static analysis](10-android-reversing/README.md): APKTool/JADX observations; exploitation claims require additional evidence.
- [11 — Web security](11-owasp-juice-shop/README.md): scoped assessment and an authentication bypass case study.
- [12 — Apache Virtual Hosts](12-apache-vhost/README.md): working local site; operational backup/restore validation is pending.
- [13 — Apache TLS](13-apache-ssl-wireshark/README.md): self-signed certificate and HTTP/HTTPS packet analysis.
- [14 — Active Directory](14-active-directory/README.md): internal network, domain and client enrollment.

Lab READMEs and reports are currently in Spanish. Screenshots are extracted from the original PDFs, which are preserved as historical evidence. Current qualifications and corrections are recorded in the READMEs and [technical review notes](docs/REVISION-TECNICA.md).

## Tools and work in progress

- [Apache log analyzer](tools/apache-log-analyzer/README.md): offline Python CLI, synthetic sample, JSON/CSV reports and automated tests. Indicators support triage, not automatic attribution or attack confirmation.
- [Apache backup helper](tools/apache-backup/README.md): archive plus file hashes; actual VM recovery remains untested.
- [Wazuh detection lab](16-siem-wazuh/README.md), [GPO validation](14-active-directory/GPO-VALIDACION.md), and [Apache hardening](12-apache-vhost/VALIDACION.md): prepared procedures, not completed deployments.

Documented results, proposed changes and pending validation are labeled separately. Synthetic data is never presented as a real incident. All practical work targets owned lab environments.

License: [MIT](LICENSE).
