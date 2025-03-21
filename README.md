# MGT0L$

![MGT0L$ Banner](https://repository-images.githubusercontent.com/831577639/b5e872bf-e08e-4d85-823a-0d64f67fa893)

MGT0L$ is a powerful collection of cybersecurity tools designed for **penetration testing**, **doxing**, **malware development**, and **OSINT research**. It is tailored for **security professionals**, **ethical hackers**, and **researchers** looking to automate and simplify complex security-related tasks.

## 🚀 Features

### 🔍 **OSINT & Doxing Tools**
- **`seeker`** – Searches for usernames across 100+ platforms.
- **`findperson`** – Extracts personal data from public databases.
- **`iplocate`** – Provides geolocation data of an IP address.
- **`lopiapi`** – Queries Chilean phone numbers.
- **`eashi`** – Clones web pages using MHTML files.
- **`fireleak`** – Audits applications for hardcoded Firebase keys.

### 🌐 **Web & Network Analysis**
- **`webmap`** – Scans and maps website structures.
- **`webdumper`** – Finds hidden directories on web servers.
- **`wpscrap`** – Enumerates endpoints and performs brute force on WordPress plugins.
- **`reverhttp`** – Establishes remote channels using HTTP/POST requests.

### 💀 **Malware Development**
- **`macromaker`** – Generates malicious macros for Word documents.
- **`wordinfect`** – Injects macros into `.docm` files.
- **`sc4pk`** – Creates APKs for penetration testing.
- **`m4cware`** – Creates a malicious APK for tracking or infection.

### 🔥 **Attack Simulation & DDoS**
- **`icmpdos`** – Simulates ICMP-based DDoS attacks.
- **`httpflood`** – Overloads HTTP servers with multiple requests.

### 📂 **Brute Force & Exploitation**
- **`ftpbrute`** – Performs brute-force attacks on FTP servers.
- **`sshforce`** – Executes brute force attacks on SSH servers.
- **`unzipper`** – Cracks password-protected ZIP files.
- **`unlocker`** – Decrypts MD5 and SHA1 hashes using brute force.

### ✉️ **Temporary Email, Phishing & Social Engineering**
- **`tempmail`** – Generates temporary email addresses.
- **`urljump`** – Creates random invite links for social platforms.
- **`shorty`** – Generates shortened malicious links mimicking popular platforms.

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
pkg install python3 git
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
├── static/             # CSS & images files
├── templates/          # HTML files
└── assets/             # Extensions & resources
```

## ⚠️ Disclaimer
MGT0L$ is intended for **educational** and **research** purposes only. Unauthorized use of this tool for illegal activities is strictly prohibited. The authors are not responsible for any misuse.

## 📜 License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## ⭐ Support & Contributions
If you find MGT0L$ useful, give it a ⭐ on GitHub! Contributions are welcome.