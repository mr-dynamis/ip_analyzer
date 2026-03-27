# IP Analyzer

A simple Python script to analyze IPv4 addresses and provide useful information about their class, type, and usability.

---

## Features
- Determines the **IP class** (A, B, C, D, E)  
- Shows the **default subnet mask**  
- Identifies whether the IP is **Private or Public**  
- Checks **usability**:
  - Usable  
  - Loopback address  
  - Broadcast address  
  - Invalid/default route  

---

## How to Use

1. **Download or clone the repository**:
   ```bash
   git clone https://github.com/mr-dynamis/ip-analyzer.git
   cd ip-analyzer
2. **Run the script with Python 3**:
   ```bash
    python3 ip_analyzer.py
3. **Enter an IP address when prompted**. Example:
   ```
    Enter an IP address: 192.168.1.1
**Example Output**
> - IP Address: 192.168.1.1
> - Class: Class C
> - Default Subnet Mask: 255.255.255.0
> - Type: Private IP
> - Usability: Usable

## Requirements
- Python 3.x
- Works on Linux, Windows, and macOS terminals
