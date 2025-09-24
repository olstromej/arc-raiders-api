# Arc Raiders Items API

A RESTful API built with FastAPI for serving **Arc Raiders** game items. This API provides detailed item information, supports filtering by category, and can be deployed locally or on AWS Lambda with API Gateway.  

---

## Table of Contents

- [Features](#features)  
- [Technologies](#technologies)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation](#installation)  
  - [Running Locally](#running-locally)  
- [API Endpoints](#api-endpoints)  
  - [Root Endpoint](#root-endpoint)  
  - [Get All Items](#get-all-items)  
  - [Get Items by Category](#get-items-by-category)  
- [Deployment](#deployment)  
  - [Deploying to AWS Lambda](#deploying-to-aws-lambda)  
  - [Testing API](#testing-api)  
- [Weekly Discord Poster](#weekly-discord-poster)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Features

- List all Arc Raiders items.
- Filter items by category (`Weapon`, `Medical`, `Material`, etc.).
- Deployable to AWS Lambda via SAM or API Gateway.
- Can be integrated with Discord webhooks for weekly item posts.

---

## Technologies

- **Python 3.13+**
- **FastAPI** – For the API server
- **Uvicorn** – ASGI server for local development
- **Mangum** – AWS Lambda adapter for FastAPI
- **Requests** – For HTTP requests (used in Discord poster)
- **Schedule** – For local scheduled tasks (weekly poster)
- **GitHub Actions** – Optional for automated weekly jobs

---

## Getting Started

### Prerequisites

- Python 3.13+ installed  
- `pip` for package management  
- Git  
- AWS CLI and SAM CLI (if deploying to AWS)  

---

### Installation

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/arc-raiders-api.git
cd arc-raiders-api


Create a virtual environment and activate it:

python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows


Install dependencies:

pip install -r requirements.txt

Running Locally

Start the API with Uvicorn:

uvicorn app:app --reload


Open your browser at http://127.0.0.1:8000
 to see the root endpoint.

The API docs are automatically generated at:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

API Endpoints
Root Endpoint
GET /


Response:

{
  "message": "Welcome to the Arc Raiders Items API"
}

Get All Items
GET /items


Response: JSON array of all items:

[
  {
    "name": "Anvil I",
    "category": "Weapon",
    "description": "Single-action hand cannon with high damage output and headshot damage, but slow handling."
  },
  {
    "name": "Medkit",
    "category": "Medical",
    "description": "Restores health fully."
  },
  ...
]

Get Items by Category
GET /items?category=<category>


Query Parameters:

category – Filter items by category (case-insensitive).

Example:

GET /items?category=Weapon


Response:

[
  {
    "name": "Anvil I",
    "category": "Weapon",
    "description": "Single-action hand cannon with high damage output and headshot damage, but slow handling."
  },
  {
    "name": "Pulse Rifle",
    "category": "Weapon",
    "description": "Energy-based assault rifle with precise shots."
  }
]


Errors:

404 Not Found if no items match the category.

Deployment
Deploying to AWS Lambda

Ensure you have SAM CLI installed.

Build the project:

sam build


Deploy to AWS:

sam deploy --guided


After deployment, note your API Gateway URL:

https://<api-id>.execute-api.<region>.amazonaws.com/Prod/items


Test with curl:

curl https://<api-id>.execute-api.us-east-1.amazonaws.com/Prod/items

Testing API

Locally:

curl http://127.0.0.1:8000/items


AWS-hosted:

curl https://<api-id>.execute-api.us-east-1.amazonaws.com/Prod/items

Weekly Discord Poster

Script: weekly_post.py

Posts a random Arc Raiders item to a Discord webhook every Monday at 10:00 AM.

Uses your deployed API to fetch items.

Run manually or schedule in GitHub Actions.

Example output in Discord:

Here is your weekly item, Raiders!

Renegade I
Category: Weapon
Lever-action rifle with high damage and range.


Run locally for testing:

python3 weekly_post.py

Contributing

Fork the repository

Create a branch: git checkout -b feature-name

Commit your changes: git commit -m "Description of feature"

Push: git push origin feature-name

Open a pull request