---

# mgt0ls

## Description

`mgt0ls` is a powerful tool designed for a variety of uses in controlled and research environments. It provides a wide range of functions that can be useful for security testing, malware behavior analysis, and other controlled applications. **It is important to note that the misuse of this tool is strictly prohibited.**

## Features

`mgt0ls` offers the following functionalities:

- **Infecting Word documents**: Allows injecting malicious code into Word documents.
- **DDoS attacks**: Facilitates the simulation of distributed denial-of-service attacks for stress testing.
- **Temporary email**: Generates temporary email addresses for testing and privacy protection.
- **Doxing**: Tools for searching and tracking personal information on the internet.

## Installation Requirements

To use `mgt0ls`, you need to meet the following requirements:

- **Python**: Ensure Python is installed. `mgt0ls` requires Python along with several basic libraries to function properly. If Python 3 doesn't work, try Python 2.

### Installation on Linux Distributions and Similar (including Termux):

```bash
apt-get install python3
bash requeriments.txt
```

Run `Python3 Shell.py` from the `mgt0ls` directory to avoid errors.

### Installation on Windows:

1. **Download Python**: Download Python from the [official Python website](https://www.python.org/downloads/) and install the latest version.
   
2. **Download `mgt0ls`**: Download `mgt0ls` from your browser and extract it.

3. **Open CMD**: Open Command Prompt (CMD) from the `mgt0ls` folder.

4. **Install Required Libraries**:
   
   ```bash
   ./requeriments.txt
   ```

5. **Run `shell.py`**:

   ```bash
   python3 shell.py
   ```

## General Explanation

Once inside, you will have access to various commands and tools:

```
[MGT0LS.PY] VERSION 1.0

# [COMMANDS]

FINDTL     [KEYWORD] Search tools by keyword.
HELP       Display all available interactions in MGT0LS.
EXIT       Terminate the MGT0LS session.

# [TOOLS]

SEEKER     Gather information using usernames.
ICMPDOS    Perform a DDoS attack using ICMP protocol.
LOPIAPI    Test with a phone number [CL].
UNZIPPER   Perform dictionary attack on ZIP compressions.
TEMPMAIL   Temporary email based on Mailnesia.
WORDINFECT Inject infected macro into a Word document [DOCM].
MACROMAKER Create a Word macro based on your specifications [OFFICE].
```

## Some Incompatibility Errors

Enter the tool or command name to execute it. These scripts are still under development, so you may encounter the following issues:

1. Library incompatibility
2. Path handling
3. Compatibility issues with certain native Windows scripts

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

