# 🛡️ Cybersecurity Portfolio — SACZN

🌐 [Español](./README.md) · **English**

Hands-on cybersecurity labs built during my technical training. Each folder documents an independent lab: objective, tools, methodology, findings, evidence and lessons learned. Lab write-ups are in Spanish; each one includes a PDF report with screenshots.

> **Profile:** cybersecurity student with hands-on experience in web auditing, mobile security, networking and Windows/Linux infrastructure. Training oriented to offensive auditing, defense and incident response.
>
> 📫 **Contact:** [GitHub @SacznMvp](https://github.com/SacznMvp) · 🎥 [YouTube channel](https://www.youtube.com/@SACZNCybersecurity) <!-- TODO: add LinkedIn / professional email -->

## 📂 Labs

| # | Lab | Technologies | Category |
|---|---|---|---|
| 14 | [Corporate network with Active Directory](./14-active-directory) | Windows Server 2016/2003, Windows 10, AD DS, VirtualBox | Windows infrastructure |
| 13 | [Apache II — SSL encryption and traffic analysis](./13-apache-ssl-wireshark) | Apache, OpenSSL, curl, Wireshark, Ubuntu | Networking & cryptography |
| 12 | [Apache — Virtual Hosts and backups](./12-apache-vhost) | Apache, Ubuntu Server, VirtualBox | Server administration |
| 11 | [Web security — OWASP Juice Shop](./11-owasp-juice-shop) | Nmap, Gobuster, Nikto, Burp Suite, Kali Linux | Web pentesting |
| 10 | [Android mobile security — Reverse engineering](./10-android-reversing) | InsecureBankv2, APKTool, JADX-GUI, Kali Linux | Mobile security |

## 🧰 Demonstrated skills

| Area | Evidence |
|---|---|
| Web pentesting (OWASP Top 10) | [Lab 11](./11-owasp-juice-shop): recon, enumeration, JWT analysis, SQL injection |
| Mobile security & reverse engineering | [Lab 10](./10-android-reversing): APK decompilation and static analysis |
| Network traffic analysis | [Lab 13](./13-apache-ssl-wireshark): HTTP vs HTTPS capture comparison in Wireshark |
| TLS and certificates | [Lab 13](./13-apache-ssl-wireshark): self-signed certificate with OpenSSL, TLS handshake |
| Web server administration | Labs [12](./12-apache-vhost) (Virtual Hosts and backups) and [13](./13-apache-ssl-wireshark) (HTTPS) |
| Active Directory & Windows environments | [Lab 14](./14-active-directory): domain, users, legacy machines |
| Technical writing | One PDF report per lab with methodology and screenshots |

## 🗺️ Roadmap

Planned labs (**not yet completed**):

| # | Lab | Goal |
|---|---|---|
| 15 | Attack and defense on Active Directory | Enumeration, Kerberoasting, Pass-the-Hash and their detection on the lab 14 domain ([guide](./15-ad-ataque-defensa)) |
| 16 | SIEM with Wazuh | Detect the attacks from labs 11 and 15 |
| 17 | Linux privilege escalation | Guided practice machine and mitigations |
| 18 | Forensics and incident response | Analysis with Autopsy / Volatility |
| 19 | IDS with Suricata | Detect Nmap scans and malicious web traffic |

## 📌 About this repository

All content is produced in isolated lab environments (VirtualBox) with no connection to production networks. Users, passwords and domain names are fictitious and used for educational purposes only.

Licensed under [MIT](./LICENSE).
