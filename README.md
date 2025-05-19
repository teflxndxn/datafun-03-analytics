# datafun-03-analytics

This project organizes a Python-based data analysis workspace.

## Setup Instructions

1. Clone this repository:
   ```bash
   git clone https://github.com/teflxndxn/datafun-03-analytics.git
   cd datafun-03-analytics

##Create and activate your virtual environment:
python3 -m venv .venv
source .venv/bin/activate  # Mac/Linux
# .venv\Scripts\activate   # Windows
Install required dependencies:
pip install -r requirements.txt

##Push to Github:
git add .
git commit -m "your message"
git push origin main

# 📦 Project Setup and Requirements

This project is configured with a professional Python development workflow. It includes a `requirements.txt` file listing all external dependencies needed for data analysis, visualization, scientific computing, and Jupyter support.


---

## Getting Started

Follow these steps to set up your environment and install all required packages.

### Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

Create and activate a virtual environment 
python -m venv venv

# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

Install dependencies from requirements.txt
pip install -r requirements.txt

#Included Dependencies

The requirements.txt file includes:

  NUMERICAL COMPUTING
numpy
  DATA ANALYSIS / DATAFRAMES
pandas
  STATISTICS / SCIENTIFIC COMPUTING
scipy
  VISUALIZATION
matplotlib
seaborn
 NETWORKING / HTTP
requests
  ENVIRONMENT VARIABLES
python-dotenv
 JUPYTER SUPPORT (If using notebooks)
jupyter
ipykernel

#Notes

Only external dependencies are listed in requirements.txt.
Standard Python libraries (like os, math, datetime) are part of the standard library and do not need to be listed.

If you're using Jupyter notebooks, make sure to run:python -m ipykernel install --user --name=venv

#Author
Blessing Aganaga
