# CodeAlpha Python Programming Internship - Task 2: Stock Portfolio Tracker

## 📝 Project Overview
This repository contains an interactive **Stock Portfolio Tracker** CLI application developed in Python. It allows users to track their financial stock portfolios using standard real-time stock prices (hardcoded) for major blue-chip tech stocks. Users can add, update, or remove shares, view formatted totals, and generate professional reports.

## 🎯 Objective
This project demonstrates Python collections (dictionaries, lists), input sanitization, dynamic mathematical calculations, and built-in Python file-handling systems (`csv`, built-in file writers).

---

## ✨ Features
- **Stock Database**: Predefined pricing catalog containing key tickers:
  - `AAPL` ($180.00)
  - `TSLA` ($250.00)
  - `GOOGL` ($150.00)
  - `MSFT` ($420.00)
  - `AMZN` ($190.00)
- **Portfolio Operations**:
  - Add stocks and specify exact share counts.
  - Update quantities dynamically if the stock already exists.
  - Remove/reduce stocks with ownership limits validation.
- **Dynamic Summaries**: Real-time evaluation of shares multiplied by price, combined into a grand total portfolio valuation.
- **Multi-Format Export**:
  - Exports a stylized text report: `portfolio_report.txt`
  - Exports a spreadsheet-ready CSV sheet: `portfolio_report.csv`
- **Robust Validations**: Enforces uppercase symbol checking and validates that all stock share counts are positive integers.

---

## 🛠️ Technologies Used
- **Language**: Python 3
- **Core Modules**: `csv`, `os`

---

## 📂 Folder Structure
```text
CodeAlpha_StockPortfolioTracker/
│
├── portfolio_tracker.py       # Core Tracker Script (Execution Entrypoint)
├── README.md                  # Project Documentation
└── screenshots/               # Directory containing sample run previews
```

---

## 🚀 Installation & Getting Started

### Prerequisites
- **Python**: Verify Python 3.x is installed:
  ```bash
  python --version
  ```

### Installation Steps
1. Navigate into the Stock Tracker project directory:
   ```bash
   cd CodeAlpha_StockPortfolioTracker
   ```

---

## 🎮 How to Run
Run the interactive CLI program:
```bash
python portfolio_tracker.py
```

---

## 📊 Sample Output previews

### Dynamic Portfolio Terminal view
```text
=======================================================
               PORTFOLIO VALUE SUMMARY              
=======================================================
STOCK    | SHARES     | UNIT PRICE   | TOTAL VALUE    
-------------------------------------------------------
AAPL     | 10         | $180.00      | $1,800.00     
TSLA     | 5          | $250.00      | $1,250.00     
MSFT     | 2          | $420.00      | $840.00       
-------------------------------------------------------
GRAND TOTAL INVESTMENT VALUE:       | $3,890.00
=======================================================
```

### Generated File Output Example (`portfolio_report.txt`)
```text
=======================================================
           STOCK PORTFOLIO TRACKER REPORT          
=======================================================
STOCK    | SHARES     | UNIT PRICE   | TOTAL VALUE    
-------------------------------------------------------
AAPL     | 10         | $180.00      | $1,800.00     
TSLA     | 5          | $250.00      | $1,250.00     
MSFT     | 2          | $420.00      | $840.00       
-------------------------------------------------------
GRAND TOTAL INVESTMENT VALUE:       | $3,890.00
=======================================================
Report generated successfully.
```

---

## 📈 Future Improvements
- **Real-Time API Integration**: Integrate a live stock market API (like Alpha Vantage or Yahoo Finance) using the `requests` library to pull active global stock prices.
- **Interactive Visualizations**: Implement standard plotting libraries like `matplotlib` or `seaborn` to render colorful portfolio pie charts and line charts.
- **Multiple Portfolios**: Support saving and swapping between different portfolio profiles (e.g. Retirement, High-growth, Tech-only).
- **Persistent Database**: Transition from txt/csv files to a local database system like SQLite to store user portfolio states persistently.
