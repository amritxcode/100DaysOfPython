# FastAPI Multi-Service API

A structured backend service built with FastAPI that integrates multiple external APIs (Identity and Weather) into a single, unified interface. This project demonstrates professional backend practices including environment variable management, functional service separation, and dependency tracking.

## Features
- Path-based routing for mathematical operations.
- Service-oriented architecture (separation of logic and routing).
- Environment variable configuration using python-dotenv.
- Automated API documentation via Swagger UI.

## Tech Stack
- Framework: FastAPI
- Server: Uvicorn
- Language: Python 3.x
- Environment Management: python-dotenv
- Dependency Management: pip (requirements.txt)

## Prerequisites
- Python 3.8+ installed.
- A virtual environment (venv) is highly recommended.

## Installation and Setup

1. Navigate to the project directory:
   cd Personal_Projects/fastapi_multi_add/

2. Create and activate a virtual environment:
   python -m venv venv
   # Windows:
   .\venv\Scripts\activate
   # Mac/Linux:
   source venv/bin/activate

3. Install required dependencies:
   pip install -r requirements.txt

4. Configure environment variables:
   Create a .env file in the root of this folder and add:
   APP_NAME="Multi-Service API"
   DEFAULT_CITY="London"

## Running the Application

Start the development server with auto-reload:
uvicorn main:app --reload

The API will be available at: http://127.0.0.1:8000

## API Documentation
Once the server is running, you can access the interactive documentation at:
- Swagger UI: http://127.0.0
- ReDoc: http://127.0.0

## Project Structure
- main.py: API entry point and route definitions.
- services.py: Core logic and external API communication.
- .env: Local configuration (ignored by git).
- requirements.txt: List of project dependencies.