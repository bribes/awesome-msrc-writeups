# Awesome MSRC Writeups
🐛 A list of writeups from the MSRC Bug Bounty program

*\*writeups: **not just** writeups*

## Contributing:

If you know of any writeups/videos not listed in this repository, feel free to open a Pull Request.

To add a new writeup, simply add a new line to `writeups.csv`:
```
[YYYY-MM-DD],[bounty],[title],[url],[author-name],[author-url],[type],false,?
```
*If a value is not available, write `?`.*<br>
*The value of `type` can either be `blog` or `video`.*<br>
*If any of the fields include a `,`, please wrap the value in quotes.*<br>
*Please keep the last two fields set to `false` and `?`. The automation will modify these fields.*<br>
*If available, set `author-url` to the author's Twitter URL, so the automation can @mention the author.*

## Writeups:

### 2025:

- **[Jun 29 - $???]** [Triple Trouble: Bypassing Sanitization to Steal Microsoft Tokens](https://melotover.medium.com/triple-trouble-bypassing-sanitization-to-steal-microsoft-tokens-d89a68be7ab2)[*](#) by [Asem Eleraky](https://x.com/Melotover)
- **[Apr 20 - $???]** [Escalating Impact: Full Account Takeover in Microsoft via XSS in Login Flow](https://melotover.medium.com/escalating-impact-full-account-takeover-in-microsoft-via-xss-in-login-flow-f160fa79b008)[*](#) by [Asem Eleraky](https://x.com/Melotover)

### 2024:

- **[Oct 08 - $3,000]** [From 401 — Unauthorized Access to 3000 $ Bounty from Microsoft.](https://medium.com/@bashir69emceeaka5/from-401-unauthorized-access-to-3000-bounty-from-microsoft-53b086379a08)[*](#) by [Bashir Mohamed (BlackPanther87)](https://x.com/Panther82Black)
- **[Oct 08 - $5,000]** [How I got a 5000 $ Bounty from Microsoft](https://medium.com/@bashir69emceeaka5/how-i-got-a-5000-bounty-from-microsoft-fb2e27fd40f7)[*](#) by [Bashir Mohamed (BlackPanther87)](https://x.com/Panther82Black)
- **[Sep 13 - $???]** [Escalating from Reader to Contributor in Azure API Management](https://binarysecurity.no/posts/2024/09/apim-privilege-escalation)[*](#) by [Christian Håland](https://x.com/christianhland)
- **[Aug 07 - $3,000]** [Persistent XSS on Microsoft Bing.com by poisoning Bingbot indexing](https://infosecwriteups.com/persistent-xss-vulnerability-on-microsoft-bings-video-indexing-system-a46db992ac7b)[*](#) by [Supakiad S. (m3ez)](https://x.com/Supakiad_Mee)
- **[Jul 14 - $???]** [Discovering a CRLF Injection Vulnerability: My Journey into the MSRC Blog Website](https://xss0r.medium.com/discovering-a-crlf-injection-vulnerability-my-journey-into-the-msrc-blog-website-5285169adddb)[*](#) by [xss0r](https://x.com/xss0r)
- **[Jul 10 - $???]** [Dynamics 365 Business Central - A Journey With Ups and Downs](https://frycos.github.io/vulns4free/2024/07/10/dynamics-ups-and-downs.html)[*](#) by [Frycos](https://x.com/frycos)
- **[Jun 21 - $???]** [Microsoft Subdomain XSS Report — Published](https://xss0r.medium.com/microsoft-subdomain-xss-report-published-3e4f54eea93c)[*](#) by [xss0r](https://x.com/xss0r)
- **[Jun 14 - $???]** [Discovering a Reflected XSS Vulnerability: My Journey into Microsoft’s Xbox.com](https://xss0r.medium.com/discovering-a-reflected-xss-vulnerability-my-journey-into-microsofts-xbox-com-d607751be100)[*](#) by [xss0r](https://x.com/xss0r)
- **[Jun 14 - $???]** [Discovering 10 XSS Vulnerabilities: My Journey into Microsoft’s Support Platforms](https://xss0r.medium.com/discovering-10-xss-vulnerabilities-my-journey-into-microsofts-support-platforms-b19c4e520c90)[*](#) by [xss0r](https://x.com/xss0r)
- **[Jun 14 - $???]** [Discovering Critical Security Vulnerabilities: My Journey into Microsoft’s Tech Community Portal](https://xss0r.medium.com/discovering-critical-security-vulnerabilities-my-journey-into-microsofts-tech-community-portal-068505cd4316)[*](#) by [xss0r](https://x.com/xss0r)
- **[Jun 14 - $???]** [Discovering Critical Security Vulnerabilities: My Journey into Microsoft’s Power Apps Portal](https://xss0r.medium.com/discovering-critical-security-vulnerabilities-my-journey-into-microsofts-power-apps-portal-86e28311448e)[*](#) by [xss0r](https://x.com/xss0r)
- **[Jun 14 - $???]** [Discovering a Reflected XSS Filter Bypass: My Journey into Microsoft’s Support UAT Subdomain](https://xss0r.medium.com/discovering-a-reflected-xss-filter-bypass-my-journey-into-microsofts-support-uat-subdomain-f9be22d8d795)[*](#) by [xss0r](https://x.com/xss0r)
- **[Jun 14 - $???]** [Discovering a Critical Security Vulnerability: My Journey into Microsoft’s Lists Subdomain](https://xss0r.medium.com/discovering-a-critical-security-vulnerability-my-journey-into-microsofts-lists-subdomain-f3e95ce68929)[*](#) by [xss0r](https://x.com/xss0r)
- **[Jun 14 - $???]** [Discovering Critical Security Vulnerabilities: My Journey into Microsoft’s Release Plans Subdomain](https://xss0r.medium.com/discovering-critical-security-vulnerabilities-my-journey-into-microsofts-release-plans-subdomain-c47621b2da2d)[*](#) by [xss0r](https://x.com/xss0r)
- **[Jun 14 - $???]** [Discovering XSS Vulnerabilitie: My Journey into Microsoft’s Azure Infrastructure](https://xss0r.medium.com/discovering-xss-vulnerabilitie-my-journey-into-microsofts-azure-infrastructure-5cecd53593cd)[*](#) by [xss0r](https://x.com/xss0r)
- **[Jun 14 - $???]** [My Journey to Uncovering Reflected XSS and HTML Injection in 4 Microsoft Subdomains](https://xss0r.medium.com/my-journey-to-uncovering-reflected-xss-and-html-injection-in-4-microsoft-subdomains-a6edaec68299)[*](#) by [xss0r](https://x.com/xss0r)
- **[Jun 14 - $???]** [CVE-2024-20693: Windows cached code signature manipulation](https://sector7.computest.nl/post/2024-06-cve-2024-20693-windows-cached-code-signature-manipulation/)[*](#) by [Sector7](https://x.com/sector7_nl)
- **[Jun 03 - $???]** [These Services Shall Not Pass: Abusing Service Tags to Bypass Azure Firewall Rules (Customer Action Required)](https://www.tenable.com/blog/these-services-shall-not-pass-abusing-service-tags-to-bypass-azure-firewall-rules-customer)[*](#) by [Liv Matan](https://x.com/terminatorLM)
- **[May 28 - $???]** [Multiple vulnerabilities in Eclipse ThreadX](https://security.humanativaspa.it/multiple-vulnerabilities-in-eclipse-threadx/)[*](#) by [Marco Ivaldi](https://x.com/0xdea)
- **[May 11 - $???]** [My Hunt: Discovering Microsoft Bugs](https://c0d3x27.medium.com/my-hunt-discovering-microsoft-bugs-f6a9c790bec0)[*](#) by [c0d3x27](https://x.com/c0d3x27)
- **[May 07 - $???]** [Lethal Injection: How We Hacked Microsoft's Healthcare Chat Bot](https://www.breachproof.net/blog/lethal-injection-how-we-hacked-microsoft-ai-chat-bot)[*](#) by [Yanir Tsarimi](https://x.com/Yanir_)
- **[Jan 31 - $???]** [Azure Devops Zero-Click CI/CD Vulnerability](https://www.legitsecurity.com/blog/azure-devops-zero-click-ci/cd-vulnerability)[*](#) by [Nadav Noy](https://x.com/nadavnoy)

### 2023:

- **[Jun 27 - $???]** [How I found DOM XSS via postMessage on Bing.com - Microsoft Bug Bounty](https://namcoder.com/blog/how-i-found-dom-xss-on-bingcom-microsoft-bug-bounty-write-up/)[*](#) by [Nam Le](https://x.com/namcoder_com)
- **[Apr 20 - $???]** [2 XSS on Microsoft](https://medium.com/@nikouei_com/2-xss-on-microsoft-37b6a7efcc84)[*](#) by [Mohammad Nikouei](https://x.com/NikoueiMohammad)
- **[Feb 22 - $???]** [How I found DOM-Based XSS on Microsoft MSRC and How they fixed it](https://infosecwriteups.com/how-i-found-dom-based-xss-on-microsoft-msrc-and-how-they-fixed-it-8b71a6020c82)[*](#) by [Supakiad S. (m3ez)](https://x.com/Supakiad_Mee)
- **[Jan 21 - $3,000]** [Reflected XSS Leads to 3,000$ Bug Bounty Rewards from Microsoft Forms](https://infosecwriteups.com/reflected-xss-leads-to-3-000-bug-bounty-rewards-from-microsoft-forms-efe34fc6b261)[*](#) by [Supakiad S. (m3ez)](https://x.com/Supakiad_Mee)

### 2022:

- **[Dec 23 - $???]** [Microsoft bug reports lead to ranking on Microsoft MSRC Quarterly Leaderboard (Q3 2022)](https://infosecwriteups.com/microsoft-bug-reports-lead-to-ranking-on-microsoft-msrc-quarterly-leaderboard-q3-2022-c6c9f70e2ccd)[*](#) by [Supakiad S. (m3ez)](https://x.com/Supakiad_Mee)

### 2020:

- **[May 19 - $???]** [Reflected XSS on microsoft.com subdomains](https://infosecwriteups.com/reflected-xss-on-microsoft-com-subdomains-4bdfc2c716df)[*](#) by [Raimonds Liepins](https://raimonds-29140.medium.com)
- **[May 02 - $???]** [Reflected XSS on Microsoft.com via Angular Js template injection](https://infosecwriteups.com/reflected-xss-on-microsoft-com-via-angular-template-injection-2e26d80a7fd8)[*](#) by [Pratik Dabhi](https://x.com/impratikdabhi)
- **[Jan 21 - $???]** [Cross Site Request Forgery vulnerability Leads to User Profile Change in Microsoft Express Logic](https://ad3sh.medium.com/cross-site-request-forgery-vulnerability-leads-to-user-profile-change-in-microsoft-express-logic-dc3481ab47ba)[*](#) by [Adesh Kolte](https://x.com/AdeshKolte)

### 2019:

- **[May 09 - $???]** [Stored XSS on Techprofile Microsoft](https://medium.com/@kang_ali/stored-xss-on-techprofile-microsoft-d21757588cc1)[*](#) by [Mohammad Ali Syarief](https://medium.com/@kang_ali)

### 2018:

- **[Oct 12 - $500]** [Microsoft CSRF Vulnerability](https://ad3sh.medium.com/how-i-got-500-from-microsoft-for-csrf-vulnerability-700accaf48b9)[*](#) by [Adesh Kolte](https://x.com/AdeshKolte)
- **[Jul 13 - $???]** [XSS in Microsoft subdomain](https://sudhanshur705.medium.com/xss-in-microsoft-subdomain-81c4e46d6631)[*](#) by [Sudhanshu Rajbhar](https://twitter.com/sudhanshur705)
- **[May 18 - $???]** [Xss in Microsoft](https://medium.com/@hacker_eth/xss-in-microsoft-7a70416aee75)[*](#) by [hacker_eth](https://medium.com/@hacker_eth)

### 2017:

- **[Dec 21 - $???]** [Microsoft SharePoint’s `Follow` Feature XSS (CVE-2017–8514) -Adesh Kolte](https://ad3sh.medium.com/microsoft-sharepoints-follow-feature-xss-cve-2017-8514-adesh-kolte-d78d701cd064)[*](#) by [Adesh Kolte](https://x.com/AdeshKolte)
- **[Nov 06 - $???]** [Get your Microsoft account hijacked by simply clicking connect button -Adesh Kolte](https://ad3sh.medium.com/get-your-microsoft-account-hijacked-by-simply-clicking-connect-button-adesh-kolte-cc0b335b0221)[*](#) by [Adesh Kolte](https://x.com/AdeshKolte)
- **[Nov 05 - $???]** [Non-persistent XSS at Microsoft -Adesh Kolte](https://ad3sh.medium.com/non-persistent-xss-at-microsoft-adesh-kolte-ad36b1b4a325)[*](#) by [Adesh Kolte](https://x.com/AdeshKolte)

### 2016:

- **[May 18 - $???]** [Microsoft Yammer Clickjacking - Exploiting HTML5 Security Features](https://seekurity.com/blog/2016/05/18/admin/general/microsoft-yammer-clickjacking-exploiting-html5-security-features)[*](#) by [Mohamed A. Baset](https://seekurity.com/blog/author/admin)
