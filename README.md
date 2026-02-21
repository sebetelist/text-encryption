# 🔐 GPG Encryption Tool (AES-256)

A simple CLI utility for encrypting and decrypting text using the **AES-256** symmetric algorithm via GnuPG.



## 📋 Requirements

To run this tool, ensure you have the following installed:

* **Python:** Version `3.11.2` or higher. [Download](https://www.python.org/downloads/)

* **Git:** For repository management. [Download](https://git-scm.com/downloads)

* **GnuPG:** Ensure the GnuPG binary is installed on your system.



## 🚀 Getting Started

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/sebetelist/encryption](https://github.com/sebetelist/encryption)
    ```

2.  **Navigate to the Directory:**
    Open your terminal and enter the project folder (where `gpg.py` is located).

    ```bash
    cd /path/to/encryption
    ```  

3.  **Install the required library:**

    ```bash
    pip3 install -r requirements.txt
    ```
    
4.  **Run the program:**
    ```bash
    python3 gpg.py
    ```



## 📖 Usage
1.  **Encryption: Enter text → Set Passphrase → Name file (e.g. secret).Saves as secret.key automatically.**

2.  **Decryption: Enter file name (without .key) → Enter Passphrase.**



## 🏗 Structure
* **gpg.py:** Logic

* **config.json:** Settings & Styles

* **requirements.txt:** Deps