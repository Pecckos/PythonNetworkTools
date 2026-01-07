## Banner Grabber

This banner grabber attempts to connect to common service ports on a target IP address and retrieve service banners, such as server responses or protocol information.

It is well suited for exercises in red teaming, CTF challenges, network analysis, or as a complement to port scanning.

The implementation is inspired by basic socket examples and extended for practical, real-world usage.

---

## Features

- Retrieves service banners using raw sockets (TCP / SOCK_STREAM)
- Scans a predefined list of common service ports
- CLI-based usage with user-provided IP input
- Graceful error handling for closed, silent, or timed-out ports
- Simple and readable Python code designed for further development
