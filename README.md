# MGT0L$

**MGT0L$** is a powerful collection of security and analysis tools designed for advanced tasks like **doxing**, **malware crafting**, and **penetration testing**. This project is aimed at researchers, developers, and cybersecurity enthusiasts who want to automate and simplify complex processes.

---

## **Features**

### **Doxing Tools**
- **`seeker`**: Searches for information based on usernames across over 100 platforms.
- **`findperson`**: Investigates personal information using public databases.
- **`iplocate`**: Geolocates an IP address with advanced details.
- **`lopiapi`**: Queries data related to phone numbers in **Chile**.

### **Scam Tools**
- **`sc4pk`**: Generates APK applications for security testing purposes.
  
### **Malware Tools**
- **`macromaker`**: Creates malicious macros for Word documents.
- **`wordinfect`**: Embeds macros into existing `.docm` documents for testing.

### **DDoS Tools**
- **`icmpdos`**: Performs basic DDoS attacks using the ICMP protocol.
- **`httpflood`**: Overloads HTTP servers with fake requests.

### **Vector Tools**
- **`webdumper`**: Finds hidden directories on web servers.
- **`ftpbrute`**: Performs brute force attacks on FTP servers.
- **`unzipper`**: Cracks password-protected ZIP files using dictionaries.
- **`tempmail`**: Generates temporary email addresses using **Mailnesia**.

---

## **Installation**

### **Requirements**
Before installing, ensure the following prerequisites are met:
1. **Operating System**: Windows, Linux, or Termux (Android).
2. **Python**: Version 3.8 or higher.
3. **Required Libraries**:
   - `requests`
   - `beautifulsoup4`
   - `aspose-words`
   - `tabulate`

You can automatically install these dependencies using the `requirements.txt` file.

---

### **Installation on Windows**
1. Clone or download the repository from GitHub:
   ```powershell
   git clone https://github.com/IND4RKHK/mgt0ls.git
   cd mgt0ls
   ```

2. Install the required dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

3. Run the main script:
   ```powershell
   python3 shell.py
   ```

---

### **Installation on Linux**
1. Clone the repository using Git:
   ```bash
   git clone https://github.com/IND4RKHK/mgt0ls.git
   cd mgt0ls
   ```

2. Install the required dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```

3. Grant execution permissions to the main script:
   ```bash
   chmod +x shell.py
   ```

4. Execute the tool:
   ```bash
   ./shell.py
   ```

---

### **Installation on Termux**
1. Update Termux:
   ```bash
   pkg update && pkg upgrade
   ```

2. Install Python and Git:
   ```bash
   pkg install python3 git
   ```

3. Clone the repository:
   ```bash
   git clone https://github.com/IND4RKHK/mgt0ls.git
   cd mgt0ls
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the main script:
   ```bash
   python3 shell.py
   ```

---

## **Usage**

### **Starting the Program**
Run the main script to access the interactive menu:
```bash
python3 shell.py
```

### **Main Commands**
Below are some of the commands available in the tool:

#### **Basic Commands**
- `help`: Displays all available tools and their descriptions.
- `update`: Checks for updates for the project.
- `exit`: Terminates the program.

#### **Doxing Tools**
```plaintext
> seeker       Collects information based on usernames from social networks and public platforms.
> findperson   Searches personal information using public databases.
> iplocate     Geolocates an IP address.
```

#### **Vector Tools**
```plaintext
> webdumper    Finds hidden directories and files on web servers.
> ftpbrute     Performs brute force attacks on FTP servers.
> unzipper     Cracks password-protected ZIP files using dictionaries.
```

### **Example Usage**
```plaintext
mgt0l$->> help
[DOXING TOOLS]
> seeker      Collects information based on usernames.
> findperson  Searches for information about people by their names [genealog].
> iplocate    Geolocates IP addresses with detailed data.
...
```

---

## **Project Structure**
```plaintext
mgt0ls/
│
├── shell.py            # Main script managing the interactive menu.
├── __prog__.py         # Module containing the implemented tools.
├── requirements.txt    # List of dependencies needed for the project.
├── README.md           # Project documentation.
└── .scripts/           # Optional directory for future extensions.
```

---

## **Disclaimer**
The use of this software should be limited to **educational** or **research** purposes in controlled environments. **Do not use these tools for illegal activities.** The author is not responsible for misuse of the code.

---

## **License**
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the `LICENSE` file for more details.