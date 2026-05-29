💰 Personal Finance Tracker

A desktop-based finance management application built using Python and Tkinter. This application provides a secure login system, tracks income and expenses, visualizes spending habits, and allows users to export data for deeper financial analysis.

📌 Project Overview

Managing personal finances shouldn't be complicated. The **Personal Finance Tracker** is designed to help users take control of their financial health. It provides a clean graphical user interface (GUI) to monitor daily transactions, visualizes spending through dynamic charts, gives smart automated budgeting suggestions, and supports robust data exporting. Mostly made for college students.

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

Launch the desktop application directly from your terminal
python main.py


🔧 Configuration & System Behavior

No `.env` or complex environment variable setup is required to run this app! The system automatically handles the following out of the box:

Authentication:** Generates and validates local user credentials securely.
Data Persistence:** Automatically manages database initialization and records local transactions.
File Exporting:** Automatically formats and structures the `transactions.csv` whenever the export action is triggered.

🤝 Contributing
Contributions are welcome! If you want to improve this project, feel free to fork the repository, create a new branch, and submit a pull request.
