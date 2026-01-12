## Network Validator (Future Function)

The Network Validator is a defensive tool that validates and classifies network input before any active operations are performed.

Its purpose is to ensure that IP addresses and network ranges are valid, correctly formatted, and suitable for scanning or analysis, reducing errors and unintended behavior.

This tool is especially useful for safe scripting practices and as a preparatory step before performing network reconnaissance.

---

## Planned Features

Validates IPv4 and IPv6 addresses

Identifies private, public, loopback, and reserved addresses

Detects invalid or malformed network input

Classifies network types before scanning

Prevents accidental scanning of local or restricted networks

Designed as a reusable module for other tools in the project

## Example Output 

=== Network Validator ===
Input: 192.168.1.10

[✓] Valid IP address

[✓] IP version: IPv4

[!] Address type: Private network

[!] Not routable on the public internet

Recommendation:
This address belongs to a private network and should not be scanned externally.

Status: Validation completed