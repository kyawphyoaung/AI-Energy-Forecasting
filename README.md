# ⚡ AI-Powered Energy Forecaster

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25%2B-FF4B4B)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A web application built for the **AI & Sustainability Hackathon 2025**. This project forecasts household energy consumption using a time-series model and provides AI-generated, actionable tips to promote energy efficiency and sustainable living, directly contributing to **SDG 7 (Affordable and Clean Energy)**.

## 🎯 Key Features

- 📈 **Historical Data Visualization:** Displays past energy usage with an interactive chart.
- 🔮 **24-Hour Forecasting:** Predicts the energy consumption for the next 24 hours using the Prophet model.
- 🔍 **Automated Peak Hour Detection:** Automatically identifies and highlights the user's daily peak consumption hours.
- 💡 **AI-Generated Eco-Advice:** Uses a Large Language Model (LLM) to generate personalized, human-friendly tips for energy saving.

## 🛠️ Technology Stack

- **Core Language:** Python
- **Web Framework:** Streamlit
- **Data Manipulation:** Pandas
- **Time-Series Forecasting:** Prophet (by Meta)
- **AI Advisory Layer:** Google Gemini

## 🚀 Getting Started: Setup & Installation

Follow these steps to set up the project on your local machine.

### 1. Clone the Repository

First, clone the project repository to your local machine.

```bash
git clone [https://github.com/YOUR_USERNAME/energy-forecaster.git](https://github.com/YOUR_USERNAME/energy-forecaster.git)
cd energy-forecaster
```

## 2. Create and Activate the Virtual Environment

Create and activate a dedicated virtual environment for the project.

### On macOS / Linux
```Bash
python3 -m venv venv
source venv/bin/activate
```

### On Windows

```bash
python -m venv venv
venv\Scripts\activate
Note: If VS Code prompts you to select the new (venv) as the workspace interpreter, choose "Yes".
````

# 3. Install Dependencies

Install all the required libraries from the requirements.txt file.

```Bash
pip install -r requirements.txt
This single command ensures that every team member has an identical environment.
```

# ▶️ How to Run the App
To run the app on your local server, use the following command:

Bash
streamlit run app.py
Your web browser will automatically open a new tab at http://localhost:8501.

# 🤝 Team Workflow & Contributing
To ensure a smooth collaboration, please follow the workflow below.

### Adding a New Library

If any team member needs to add a new library, please follow these three steps every time:

1. Install the library:

```Bash
pip install <new-library-name>
```

2. Update requirements.txt:
```Bash
pip freeze > requirements.txt
```

3. Commit and Push: Commit the updated requirements.txt file and push it to the repository.
```Bash
git add requirements.txt
git commit -m "feat: Add <new-library-name> for X feature"
git push
Important: Always run git pull to get the latest updates before you start working.
```

# ☁️ Deployment
This application is deployed on Streamlit Community Cloud.

**Live App URL**: [Link will be added here once deployed]

Note: The live app will automatically update whenever new changes are pushed to the main branch.