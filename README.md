# E-Commerce AI Project

This project is enables visual search in e-commerce platforms using artificial intelligence.

## Project Summary

The E-Commerce AI Project is an innovative solution that allows users to search for similar products using images they upload. Developed using image processing and artificial intelligence technologies, this system provides search results based on visual similarity analysis.

## Setup Steps

### Requirements

- Python 3.7+
- Node.js 14+
- npm or yarn

### Backend Setup

```bash
# Navigate to the backend directory
cd ecommerce-ai/backend

# Create a Python virtual environment
python -m venv venv

# Activate the virtual environment
# For Windows:
venv\Scripts\activate
# For Linux/MacOS:
# source venv/bin/activate

# Install required packages
pip install -r requirements.txt
```

### Frontend Setup

```bash
# Navigate to the frontend directory
cd ecommerce-ai/frontend

# Install dependencies
npm install
```

## Running the Project

### Backend Server

```bash
cd ecommerce-ai/backend
# Virtual environment should be active
python app.py
```

### Frontend Application

```bash
cd ecommerce-ai/frontend
npm start
```

## System Architecture

The project consists of two main components:

1. **Backend (Flask)**: Image processing, AI model integration, and API services
2. **Frontend (React)**: User interface and interactive experience

## Features

- Find similar products with visual search technology
- Category-based filtering system
- AI-powered product recommendations
- User-friendly interface

## Contributing

For information on how to contribute, please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file.
