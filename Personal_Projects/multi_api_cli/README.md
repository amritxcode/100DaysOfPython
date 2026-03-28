# Multi-API CLI Tool (Name Analyzer + Weather)

A simple yet powerful **Python-based CLI application** that integrates multiple public APIs to fetch:

- Name-based insights (age, gender, country)
-  Weather information for any city

This project is built for learning **API integration, modular programming, and real-world CLI development**.

---

## Features

- Analyze name to get:
  - Estimated age
  - Gender prediction
  - Country prediction

- Get weather information:
  - Current temperature of any city

- Clean CLI interface with menu system
- Error handling for API failures
- Continuous usage with loop-based menu
- Modular and reusable code structure

---

## APIs Used

- https://api.agify.io → Age prediction  
- https://api.genderize.io → Gender prediction  
- https://api.nationalize.io → Country prediction  
- https://wttr.in → Weather API  

---

## Tech Stack

- Python
- Requests library
- REST APIs

---

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/multi-api-cli-tool.git
cd multi-api-cli-tool

### 2. Install dependencies
```bash
pip install requests

### 3. Run the program
```bash
python main.py

## Usage
--- Multi API CLI Tool ---
1. Analyze Name
2. Check Weather
3. Exit

Option 1: Name Analysis
Enter a name
Get age, gender, and country
Option 2: Weather Check
Enter a city
Get current temperature

Example Output

Result
------------------
Name: Appu
Age: 57
Gender: Male
Country: IN

Result
------------------
City: Delhi
Temperature: 32°C

Project Structure

multi-api-cli-tool/
│
├── main.py        # Main program
└── README.md      # Documentation
