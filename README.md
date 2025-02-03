# MGT0L$

![MGT0L$ Banner](https://github.com/IND4RKHK/mgt0ls/assets/banner.png)

MGT0L$ is a powerful collection of cybersecurity tools designed for **penetration testing**, **doxing**, **malware crafting**, and **OSINT research**. It is tailored for **security professionals**, **ethical hackers**, and **researchers** looking to automate and simplify complex security-related tasks.

## 🚀 Features

### 🔍 **OSINT & Doxing Tools**
- **`seeker`** – Searches for usernames across 100+ platforms.
- **`findperson`** – Extracts personal data from public databases.
- **`iplocate`** – Provides geolocation data of an IP address.
- **`lopiapi`** – Queries Chilean phone numbers.

### 💀 **Malware Development**
- **`macromaker`** – Generates malicious macros for Word documents.
- **`wordinfect`** – Injects macros into `.docm` files.
- **`sc4pk`** – Creates APK files for penetration testing.
- **`m4cware`** – Generates malicious APKs for tracking and exploitation.

### 🔥 **DDoS & Attack Simulation**
- **`icmpdos`** – Simulates ICMP-based DDoS attacks.
- **`httpflood`** – Overloads HTTP servers with requests.

### 📂 **Brute Force & Exploitation**
- **`webdumper`** – Finds hidden directories on web servers.
- **`ftpbrute`** – Performs brute-force attacks on FTP servers.
- **`unzipper`** – Cracks password-protected ZIP files.
- **`unlocker`** – Decrypts MD5 and SHA1 hashes using brute force.
- **`sshforce`** – Executes brute force attacks on SSH servers.

### ✉️ **Temporary Email & Social Engineering**
- **`tempmail`** – Generates temporary email addresses.
- **`urljump`** – Creates random invite links for social platforms.
- **`shorty`** – Generates shortened malicious links mimicking popular platforms.

### 🌐 **Web & Network Analysis**
- **`webmap`** – Scans and maps website structures.
- **`reverhttp`** – Establishes remote channels using HTTP/POST requests.

## 🛠 Installation

### ✅ **Requirements**
Ensure your system meets the following requirements:
- **OS**: Windows, Linux, or Termux (Android)
- **Python**: Version 3.8+
- **Dependencies**: Installed automatically via `setup.py`

### 💻 **Windows Installation**
```powershell
git clone https://github.com/IND4RKHK/mgt0ls.git
cd mgt0ls
python setup.py
python fsh.py --h
```

### 🐧 **Linux Installation**
```bash
sudo su
git clone https://github.com/IND4RKHK/mgt0ls.git
cd mgt0ls
python3 setup.py
chmod +x fsh.py
```

### 📱 **Termux Installation**
```bash
pkg update && pkg upgrade
pkg install python git
cd mgt0ls
python3 setup.py
```

## 🔧 Usage

### 🏁 **Run MGT0L$**
```bash
python3 fsh.py --h
```

### ⚙ **Common Commands**
- Display all available tools:
  ```bash
  python3 fsh.py help
  ```
- Search for a username:
  ```bash
  python3 fsh.py seeker --a johndoe
  ```
- Find IP location:
  ```bash
  python3 fsh.py iplocate --a 8.8.8.8
  ```

## 📂 Project Structure
```plaintext
mgt0ls/
├── fsh.py              # Main script
├── setup.py            # Installer
├── __prog__fast__.py   # Core module
├── README.md           # Documentation
├── LICENSE             # License file
└── assets/             # Extensions & resources
```

## ⚠️ Disclaimer
MGT0L$ is intended for **educational** and **research** purposes only. Unauthorized use of this tool for illegal activities is strictly prohibited. The authors are not responsible for any misuse.

## 📜 License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## ⭐ Support & Contributions
If you find MGT0L$ useful, give it a ⭐ on GitHub! Contributions are welcome.

