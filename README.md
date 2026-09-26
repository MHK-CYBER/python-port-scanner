#  Python Port Scanner

A beginner-friendly Python port scanner built to understand how network scanning works internally.  
This project demonstrates the basics of TCP port scanning using Python sockets.

---

##  Features
- Scans a user-defined range of ports
- Identifies open TCP ports
- Uses socket timeouts to avoid freezing
- Handles user interruption gracefully (Ctrl + C)
- Clean and simple implementation for learning purposes
- Basic banner grabbing for service identification

---

##  What I Learned
- How port scanning works behind tools like Nmap
- Basics of socket programming in Python
- Difference between open, closed, and filtered ports
- Importance of timeouts and resource cleanup
- Ethical considerations of active reconnaissance
- How services may leak information through banners

---

##  How It Works
The scanner:
1. Takes a target IP address
2. Takes a start and end port
3. Attempts a TCP connection to each port
4. Reports ports that successfully accept connections

This is similar to a **TCP Connect Scan** (`nmap -sT`).

---

##  Usage

```bash
python scanner.py

Example Input : 
Enter target IP: 127.0.0.1
Enter start port: 1
Enter end port: 1024

## Disclaimer:

This tool is for educational purposes only.
Scan only systems you own or have explicit permission to test.

 Author:

Mehek (MHK-CYBER)
