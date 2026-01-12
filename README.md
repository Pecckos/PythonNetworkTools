## PythonNetworkTools

PythonNetworkTools is a modular, automated cybersecurity toolkit designed to perform network reconnaissance and basic security analysis in Linux environments.
Developed as part of the “Applied Scripting” course, the project demonstrates how multiple security-focused scripts can be combined into a single, robust and user-friendly tool.

The toolkit integrates IP intelligence gathering, port scanning, and banner grabbing into an interactive menu-driven application.

---

## 📋 Table of Contents

-- Project Overview

-- Key Features

-- System Requirements

-- Installation

-- Usage

-- Logging

---

## 🔭 Project Overview

The primary goal of PythonNetworkTools is to automate common reconnaissance tasks used in defensive security, incident response, and learning environments.

Instead of running isolated scripts, this project provides a modular architecture where each security function is implemented as a reusable module and orchestrated through a central interface.

The application focuses on:

controlled execution

clear user interaction

safe error handling

educational and defensive use cases

---

## ✨ Key Features

IP Tracker
Retrieves public information about an IP address using external APIs and optionally generates a geolocation map.

Port Scanner
Performs multi-threaded TCP port scanning to identify open services on a target host.

Banner Grabber
Connects to common service ports and attempts to retrieve service banners for basic fingerprinting.

Modular Architecture
Each tool is implemented as a separate module, enabling reuse and future expansion.

User-Friendly Interface
Menu-based interaction with clear prompts and error handling.

Defensive Programming
Timeouts, exception handling, and controlled exits prevent crashes during execution.

---

## 💻 System Requirements

This project is intended to run in Linux environments.

OS: Linux (tested on Kali Linux)

Python: Version 3.9 or higher

Privileges:
Some features (port scanning and banner grabbing) may require root privileges.

Reason:
Low-level network operations may be restricted for non-privileged users. The script will still run but results may vary depending on permissions.

---

## ⚙️ Installation

Clone the Repository
```

git clone https://github.com/Pecckos/PythonNetworkTools.git
cd PythonNetworkTools

```

Create a Virtual Environment
```

python3 -m venv venv
source venv/bin/activate

```

Install Dependencies
```

pip install -r requirements.txt

```

---

## 🚀 Usage

Run the main application:
```

python3 main.py

```


For full functionality (recommended):

sudo python3 main.py

## Available Options

The interactive menu allows you to:

1. Track IP information

2. Scan open ports

3. Perform banner grabbing

4. Exit the program

## Command-Line Flags

The script supports basic CLI arguments:
```

python3 main.py --help
python3 main.py --version

```

---

## 📝 Logging

PythonNetworkTools is designed to handle errors gracefully and provide clear runtime feedback.

All errors and exceptional conditions are handled without crashing the program.

Network timeouts and unreachable hosts are reported clearly to the user.

The modular structure allows logging to be extended easily in future versions.

(Logging to file can be added as a planned enhancement.)

---

## 🛣️ Roadmap (Future Development)

- Add DNS lookup tool to reveal underlying IP addresses and DNS records

- Add Network Validator to verify and classify IP addresses and networks before scanning

- Add CLI-only mode (no interactive menu)

- Add Password_Cracker function (educational and controlled use only)

- Add IPv6 support for modern network environments

---

## ⚠️ Disclaimer

This project is intended for educational and defensive security purposes only.
Do not scan systems you do not own or have explicit permission to test.
