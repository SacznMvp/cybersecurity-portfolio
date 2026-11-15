# 🛡️ Cybersecurity Portfolio — SACZN

🌐 [Español](./README.md) · **English**

Hands-on cybersecurity labs built during my technical training. Each folder documents an independent lab: objective, tools, methodology, findings, evidence and lessons learned. Lab write-ups are in Spanish; each one includes a PDF report with screenshots.

> **Profile:** cybersecurity student with hands-on experience in web auditing, mobile security, networking and Windows/Linux infrastructure. Training oriented to offensive auditing, defense and incident response.
>
> 📫 **Contact:** [GitHub @SacznMvp](https://github.com/SacznMvp) · 🎥 [YouTube channel](https://www.youtube.com/@SACZNCybersecurity) <!-- TODO: add LinkedIn / professional email -->

## 📂 Completed labs

| # | Lab | Technologies | Category | Level |
|---|---|---|---|---|
| 14 | [Corporate network with Active Directory](./14-active-directory) | Windows Server 2016/2003, Windows 10, AD DS, VirtualBox | Windows infrastructure | 🟠 |
| 13 | [Apache II — SSL encryption and traffic analysis](./13-apache-ssl-wireshark) | Apache, OpenSSL, curl, Wireshark, Ubuntu | Networking & TLS | 🟡 |
| 12 | [Apache — Virtual Hosts and backups](./12-apache-vhost) | Apache, Ubuntu Desktop, VirtualBox | Server administration | 🟢 |
| 11 | [Web security — OWASP Juice Shop](./11-owasp-juice-shop) | Nmap, Gobuster, Nikto, Burp Suite, Kali Linux | Web pentesting | 🟡 |
| 10 | [Android mobile security — Reverse engineering](./10-android-reversing) | InsecureBankv2, APKTool, JADX-GUI, Kali Linux | Mobile security | 🟡 |

**Level:** 🟢 basic · 🟡 intermediate · 🟠 upper-intermediate · 🔴 advanced. This is my own estimate of relative difficulty.

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

## 🗺️ Learning path

Planned labs, ordered by difficulty. They are **not yet** completed; each guide will be filled in with its own report.

| # | Topic | Level | Status |
|---|---|---|---|
| 1 | [Virtual lab with VirtualBox and Kali](./01-laboratorio-virtual) | 🟢 | Planned · basis already visible in lab 14 |
| 2 | [Linux command line and permissions](./02-linux-cli-permisos) | 🟢 | ✅ Done |
| 3 | [Networking and packet analysis](./03-redes-wireshark-tcpdump) | 🟢 | ✅ Done (with tcpdump, no Wireshark — see note in the lab) |
| 4 | [Reconnaissance with Nmap](./04-nmap-reconocimiento) | 🟡 | Planned · Nmap already used in lab 11 |
| 5 | [Firewall with iptables and ufw](./05-firewall-iptables-ufw) | 🟡 | Planned |
| 6 | Password cracking (Hashcat, John the Ripper) | 🟡 | Planned |
| 7 | [Cryptography with OpenSSL and GPG](./07-criptografia-openssl-gpg) | 🟡 | Planned · OpenSSL already used in lab 13 |
| 8 | Vulnerability scanning (OpenVAS) | 🟠 | Planned |
| 9 | Guided exploitation with Metasploit | 🔴 | Planned |
| 15 | [Attack and defense on Active Directory](./15-ad-ataque-defensa) | 🔴 | Planned · continues lab 14 |
| 16 | SIEM with Wazuh | 🟠 | Planned · detect the attacks from labs 11 and 15 |
| 17 | Linux privilege escalation | 🟠 | Planned |
| 18 | Forensics and incident response (Autopsy, Volatility) | 🔴 | Planned |
| 19 | IDS with Suricata | 🟠 | Planned |

## 📌 About this repository

All content is produced in isolated lab environments (VirtualBox) with no connection to production networks. Users, passwords and domain names are fictitious and used for educational purposes only.

Licensed under [MIT](./LICENSE).
