# AI Resume & Job Matching Agent 🤖

A Python-based multi-agent workflow that analyzes a resume and job description, identifies matching and missing skills, calculates a job match score, and provides skill improvement recommendations.

## Features

- 📄 Resume analysis
- 💼 Job description analysis
- 🔍 Skill matching
- 📊 Match score calculation
- 💡 Skill improvement recommendations
- 🤖 Manager Agent to coordinate the workflow
- 🌐 Streamlit web interface

## Agents

- Resume Agent
- Job Agent
- Match Agent
- Recommendation Agent
- Manager Agent

## Technologies Used

- Python
- Jupyter Notebook
- Streamlit
- PyPDF
- ipywidgets

## How It Works

1. Upload a resume PDF.
2. Enter a job description.
3. Resume Agent identifies skills from the resume.
4. Job Agent identifies required skills.
5. Match Agent compares the skills.
6. A match score is calculated.
7. Recommendation Agent suggests skills to improve.

## How to Run

```bash
streamlit run app.py
