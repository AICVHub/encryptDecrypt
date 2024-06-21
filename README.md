# File Encryption Tool
**中文说明见：[README_ZH-CN.md](https://github.com/AICVHub/encryptDecrypt/blob/main/README_ZH-CN.md)** 

## Introduction
A Python-based file encryption tool that provides a graphical user interface (GUI) for easy encryption and decryption of files.

## Download
No need to configure the environment, run directly： https://github.com/AICVHub/encryptDecrypt/releases

## System Requirements
- **Python Environment**: Ensure Python is installed; the tkinter library typically comes bundled with the Python environment.
- **cryptography Library**: Used for encryption operations. If not already installed, install it via the following command:
`pip install cryptography`


## Running Instructions
1. Open the command line interface and navigate to the directory containing the project.
2. Execute the following command to start the program:
`python main.py`

3. The program will display a GUI with the following functional buttons:
- **Encrypt File**: Select a file for encryption.
- **Decrypt File**: Select an encrypted file for decryption.
- **Load Key**: Load the key used for encryption or decryption.

## Usage Guide
- Use the **Encrypt File** feature to select a file you wish to encrypt; the program will apply the key for encryption.
- Use the **Decrypt File** feature to select an encrypted file and decrypt it using the corresponding key.
- Before using the **Load Key** feature, ensure the key file is accessible.

## Important Notes
- Ensure the correct key is loaded before encrypting or decrypting.
- Safeguard your key file; losing it may result in permanent loss of access to encrypted files.

## Contribution Guidelines
We welcome contributions in any form. If you wish to contribute to the project, please submit a Pull Request or create an Issue.

## License
This project is licensed under the [MIT License](LICENSE). Please adhere to the terms of the license when participating in the project.