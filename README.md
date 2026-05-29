 📌 Project Summary
The **Personal Finance Tracker** is a secure, dynamic, and modern desktop application engineered using **Python (CustomTkinter)** and an **SQLite3** relational database. The application is designed to help individuals log income, track specific category-wise expenses (Food, Travel, and Miscellaneous), visualize spending breakdowns through embedded analytics, and audit historical financial records.

The core highlight of this project is its robust **isolated multi-user architecture**. It allows multiple users to register and manage their finances on the same system without any risk of cross-user data exposure, mirroring real-world secure software standards.


🛠️ Key Technical Modules & Features

### 1. User Authentication Portal (`login.py`)

* Implements a standalone secure user gateway allowing new users to register unique credentials and existing users to authenticate.
* Managed via a structured relational database file (`users.db`) with constraint checks to prevent duplicate usernames.

### 2. Session Management & Data Isolation (`database.py`)

* Built with data integrity at its core. When a user logs in successfully, their unique username is captured as an active global session state variable.
* The application utilizes **Composite Primary Keys** `(username, category)` and parameterized SQL queries inside `finance.db`. This guarantees complete transactional isolation—users can *only* read, write, or update their personal financial data.

### 3. Embedded Live Visual Analytics (`main.py`)

* Integrates **Matplotlib** directly into the CustomTkinter GUI framework using the `FigureCanvasTkAgg` backend interface.
* Upon processing transactions, raw numerical float values are instantly processed, vectorized, and rendered into an interactive **Live Spending Breakdown Pie Chart**.

### 4. Automated Financial Intelligence Engine

* Features background algorithmic threshold evaluations. The system dynamically computes the balance percentage against total income.
* If expenses exceed critical saving margins (e.g., 50% or 70% threshold limits), the UI color codes change automatically, and the engine generates customized alert prompts like: *"Warning! Expenses exceeded income 🚨"*.

### 5. Data Serialization (`Export CSV`)

* Integrates Python’s native `csv` file handler to let users download their complete isolated historical transaction records into a clean, comma-separated spreadsheet named `[username]_transactions.csv` for advanced reporting in MS Excel or Power BI.


## 🏗️ Architecture Design Flow

```text
[ USER INTERACTION ]
        │
        ▼
 🔐 login.py (Tkinter GUI Portal) ──► Validates User ──► [ users.db ]
        │
 (If Session Authenticated)
        │
        ▼
 📊 main.py (Modern CustomTkinter Dashboard + Matplotlib Canvas)
        │
        ├──► Operations: Calculate, Render Plots, Load Isolated Logs, Export CSV
        │
        ▼
 ⚙️ database.py (SQL Queries Execution) ◄──────► [ finance.db ] (User-Isolated Ledgers)


 🚀 Key Features:
🔐 User Login & Authentication System:** Secure access to ensure your financial data remains private.
💰 Income & Expense Tracking:** Effortlessly add, modify, and categorize your cash flow.
📊 Visual Analytics:** View a real-time pie chart breakdown of your expenses powered by Matplotlib.
📋 Transaction History Viewer:** Scroll through a clean history log of past records.
🧠 Smart Financial Suggestions:** Receive rule-based, automated insights to help you budget better.
📁 Double Format Export:** Seamlessly export data into CSV file
💾 Persistent Storage:** Built-in local database storage ensures your data is saved between sessions.

 🛠️ Tech Stack

* **Language:** Python 🐍
* **GUI Framework:** Tkinter
* **Database:** SQLite / Custom Database Module
* **Data Visualization:** Matplotlib
* **Data Analysis & Export:** Pandas, OpenPyXL, CSV Module
* **Version Control:** Git & GitHub

📂 Project Structure
personal-finance-tracker/
│
├── main.py              # Main entry point (UI setup + core application logic)
├── database.py          # Database handling and persistent storage operations
├── login.py             # User authentication and login system interface
├── transactions.csv     # Exported CSV data file
└── README.md            # Project documentation

### 1. Prerequisites

Ensure you have **Python 3.x** installed on your system. You can check your version by running:
python --version

### 2. Installation

Clone the repository and install the required dependencies:

# Clone the repository
git clone <your-repository-link>

# Move into the project directory
cd personal-finance-tracker

# Install required external libraries
pip install matplotlib pandas openpyxl


 ▶️ How to Run the Project

Launch the desktop application directly from your terminal:
python login.py
eg: username :anant  password:1223

🔧 Configuration & System Behavior

No `.env` or complex environment variable setup is required to run this app! The system automatically handles the following out of the box:

Authentication:** Generates and validates local user credentials securely.
Data Persistence:** Automatically manages database initialization and records local transactions.
File Exporting:** Automatically formats and structures the `transactions.csv` whenever the export action is triggered.

🤝 Contributing
Contributions are welcome! If you want to improve this project, feel free to fork the repository, create a new branch, and submit a pull request.
