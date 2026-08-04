# Financial_Dashboard

A web based budget management dashboard built with Python and Streamlit that provides an interactive overview of organizational budgets and spending. The application uses a sample financial dataset to demonstrate how budget information can be analyzed and visualized through a dashboard.

> **Note:** All financial data included in this project is sample data created for demonstration purposes only. It does not represent any real organization or financial records.

## Technologies Used

* Python
* Streamlit
* Pandas
* Plotly
* OpenPyXL

## Project Structure

Financial_Dashboard/
│
├── backend/
│   ├── dashboard.py      # Streamlit dashboard
│   ├── data.py           # Data loading and processing
│   └── main.py           # API endpoints
│
├── data/
│   └── Budget2026.xlsx   # Sample dataset
│
├── requirements.txt
└── README.md

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Financial_Dashboard.git
```

Navigate to the project:

```bash
cd Financial_Dashboard
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Running the Dashboard

Start the Streamlit application:

```bash
streamlit run backend/dashboard.py
```

## Purpose

This project was created to demonstrate practical software engineering skills, including data processing, API integration, dashboard development, and data visualization. It is a project that was used and tested on real hospital data .
