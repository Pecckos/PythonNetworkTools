## DNS Lookup Tool (Future Function)

This DNS lookup tool is designed to resolve domain names and inspect DNS records in order to reveal what exists behind a hostname.

It provides insight into how domain names are translated into IP addresses and how services such as email and name servers are configured.

The tool is intended for learning, reconnaissance, and defensive security analysis, 

and serves as a foundational component for understanding network infrastructure.

---

## Planned Features

Resolves domain names to IP addresses (A / AAAA records)

Performs reverse DNS lookups (PTR records)

Retrieves common DNS record types (MX, NS, TXT)

Identifies misconfigurations or unexpected DNS responses

CLI-compatible for automation and scripting

Clean and modular Python implementation for further expansion

---

## Output Example 

=== DNS Lookup Tool ===
Target Domain: example.com

[+] A Records (IPv4)  
    93.184.216.34

[+] AAAA Records (IPv6) -- show which IP addresses a domain points to  
    2606:2800:220:1:248:1893:25c8:1946

[+] MX Records (Mail Servers) -- show where email for the domain is deliverd  
    Priority: 10  Mail Server: mail.example.com
    
[+] NS Records (Name Servers) -- show which name servers manage the domain  
    ns1.example.net
    ns2.example.net

[+] TXT Records -- for security and verification  
    "v=spf1 include:_spf.example.com ~all"

[+] Reverse DNS -- shows which domain name is linked to an IP address  
    93.184.216.34 -> example.com

[✓] DNS lookup completed successfully
