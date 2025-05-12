# Design Documentation

## Overview
This document explains the design decisions, setup process, and usage of the URL Shortener application. It includes details about the application's architecture, user interface design, and functionality.

---

## Design Decisions

### 1. **Application Architecture**
The application follows the **Flask Blueprint architecture** to separate concerns and promote modularity:
- **Blueprint**: All routes related to URL shortening are encapsulated in a dedicated `shortener` blueprint.
- **Extensions**: Database and migrations are initialized in a dedicated `extensions.py` file for reusability and scalability.
- **Factory Pattern**: The `create_app` function provides flexibility for initializing the app with various configurations, making it adaptable for different environments (e.g., development, testing, production).

### 2. **Database Design**
The application uses an SQLite database for simplicity:
- **Table Structure**:
  - `id`: Primary key for unique identification.
  - `original_url`: Stores the original long URL.
  - `short_url`: Stores the generated shortened URL.
  - `views`: Stores the number of visits to per shortened URL.
  - `date_created`: Records the creation date and time.
  - `expiration_days`: Stores how many days the shortened URL is valid.
- **Flexibility**: The design ensures support for both auto-generated and user-defined short URLs.

### 3. **User Interface Design**
The UI is built with **Bootstrap 5.3** for responsiveness and ease of use:
- **Minimalist Design**: Focused on clarity and functionality.
- **Interactive Elements**:
  - Form for submitting original URLs.
  - Buttons for regenerating links, viewing analytics, and navigating.
- **Feedback**: Success and error messages ensure users are informed about their actions.

### 4. **Analytics Feature**
An analytics feature was included to provide insights into the usage of shortened URLs:
- Tracks the number of clicks on each shortened URL.
- Displays a summary to the user upon request.

---

## Setup Instructions

### 1. **Prerequisites**
- Docker installed on your system.
- Python 3.9+ installed locally (for development).
- SQLite (built-in with Python).

### 2. **Docker Setup**

#### Build the Docker Image:
```bash
docker build -t url-shortener-app .
```

#### Run the Docker Container:
```bash
docker run -d -p 5000:5000 --name url-shortener url-shortener-app
```

### 3. **Local Development Setup**

#### Install Dependencies:
```bash
pip3 install -r requirements.txt
```

#### Run the Application Locally:
```bash
python3 main.py
```

---

## Usage Instructions

### 1. **Shortening a URL**
1. Enter a URL in the input field labeled "Original URL."
2. (Optional) Add a custom short ID in the "Custom Short ID" field.
3. Click the **Submit** button.
4. Copy the generated shortened URL or use it directly.

### 2. **Regenerating a Link**
Click the **Regenerate Link** button to generate a new short URL for the same original URL.

### 3. **Viewing Analytics**
Click the **View Analytics** button to see usage statistics for a specific shortened URL.


