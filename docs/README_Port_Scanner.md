## Port Scanner

This port scanner scans a set of common ports on a target host and displays which ports are open.

It is well suited for exercises in red teaming, penetration testing, and network analysis.

The implementation is based on concepts from SuperFastPython by Jason Brownlee:  
https://superfastpython.com/threadpoolexecutor-port-scanner/



## Features

- Scans multiple ports in parallel using ThreadPoolExecutor
- Uses a predefined list of common ports (e.g. 22, 80, 443, 3306)
- Fast and efficient execution through multithreading
- Simple CLI usage via the menu in `main.py`
- Graceful error handling when a host is unreachable or ports are closed

## Note ⚠️ 
For deeper and more advanced analysis, tools such as `nmap` are recommended.  
Integration with nmap is planned for future versions of this project.
