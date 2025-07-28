# Freelance Platform API

## Overview

This is a **FastAPI-based** freelance platform simulation that enables interaction between **clients** and **freelancers**, while also providing an **administrative panel** for platform management. The project includes **AI-powered features** for generating reports, analyzing statistics, and recommending budgets.

## Technologies Used

- **FastAPI** - API framework
- **PostgreSQL** - Database
- **SQLAlchemy** - ORM for database interactions
- **JWT Authentication** - Secure login system
- **Hugging Face AI Model via Llama.cpp** - AI-powered insights
<br>**Base LLM**: https://huggingface.co/ibm-granite/granite-3.1-2b-instruct
<br>**Llama.cpp 4-bit Quantized**: https://huggingface.co/bartowski/granite-3.1-2b-instruct-GGUF/blob/main/granite-3.1-2b-instruct-IQ4_XS.gguf

- **Logging** - Request, response, and error tracking
- **CORS** - Cross-Origin Resource Sharing
- **PEP8 Compliant** - Code follows best practices

## Features

### User Panel (Client)

- User **Registration & Authentication**
- **Create, Read, Update, Delete (CRUD)** their profile
- **Create, Read, Update, Delete (CRUD)** their requests
- View the **general list** of available job requests

### Admin Panel

- **Manage Users**
  - Read, Update, Delete any non-admin user
  - Block users temporarily or permanently
- **Manage Job Requests**
  - Read, Update, Delete any request
  - Block requests temporarily

### AI Features

- **Generate daily/monthly reports** based on user requests
- **Analyze request statistics** (trends, budget ranges, demand)
- **Suggest a price** for new job requests based on similar past jobs

---

## Installation & Setup

### 1. Clone the repository

```sh
git clone https://github.com/me1nyk/freelance-platform.git
cd freelance-platform
```

### 2. Create and activate a virtual environment

```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies

```sh
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a **.env** file in the root directory.
Use **.env.example** as a template and fill in the required values.

### 5. Setting up the database

#### 1. Install PostgreSQL (if not installed)
- **Linux/macOS:** `sudo apt install postgresql` or `brew install postgresql`
- **Windows:** Install via [official installer](https://www.postgresql.org/download/)

#### 2. Start and create required resources
- **Linux/macOS:** `sudo service postgresql start`
- **Windows:** Start the PostgreSQL service
- **Connect to the PostgreSQL shell**:
```sh
psql -h localhost -U postgres
```
- **Inside the PostgreSQL shell**, run the following commands:
```
CREATE USER urbanskyi WITH PASSWORD '12345Nazar';
ALTER ROLE urbanskyi CREATEDB;
CREATE DATABASE freelance_platform;
GRANT ALL PRIVILEGES ON DATABASE freelance_platform TO urbanskyi;
```

#### 3. Set up the database with test data
Run this script:
```sh
./setup_db.sh
```

### 6. Run database migrations

Use **alembic.ini.example** as a template to create **alembic.ini**.
Then, run the following command to apply migrations:

```sh
alembic upgrade head
```

### 7. Start the FastAPI server

```sh
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
**Note**: On first startup, the AI model will be downloaded from the specified MODEL_URL.
This process may take several minutes.

### 8. Access API Documentation

Once the server is running, open the browser and go to:

- **Interactive Docs:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Admin Credentials
To access the **Admin Panel**, log in with the following test credentials:
```json
{
    "email": "john.doe@example.com",
    "password": "Johndoe_567"
}
```
If the login is successful, you’ll receive a JWT token in the response.

---

## API Endpoints

### User Endpoints

| Method     | Endpoint         | Description           |
| ---------- | ---------------- | --------------------- |
| **POST**   | `/auth/register` | Register a new user   |
| **POST**   | `/auth/login`    | Login & get JWT token |
| **GET**    | `/user/profile`  | View user profile     |
| **PUT**    | `/user/profile`  | Update user profile   |
| **DELETE** | `/user/profile`  | Delete user account   |

### Job Request Endpoints

| Method     | Endpoint                 | Description              |
| ---------- | ------------------------ | ------------------------ |
| **POST**   | `/requests/`             | Create a new job request |
| **GET**    | `/requests/`             | Get all job requests     |
| **GET**    | `/requests/{request_id}` | Get request details      |
| **PUT**    | `/requests/{request_id}` | Update request           |
| **DELETE** | `/requests/{request_id}` | Delete request           |

### Admin Endpoints

| Method     | Endpoint                               | Description       |
| ---------- | -------------------------------------- | ----------------- |
| **GET**    | `/admin/users/{user_id}`               | View user info    |
| **PUT**    | `/admin/users/{user_id}`               | Update user       |
| **DELETE** | `/admin/users/{user_id}`               | Delete user       |
| **PUT**    | `/admin/users/block/{user_id}`         | Block user        |
| **PUT**    | `/admin/users/unblock/{user_id}`       | Unblock user      |
| **GET**    | `/admin/requests/{request_id}`         | View request info |
| **PUT**    | `/admin/requests/{request_id}`         | Update request    |
| **DELETE** | `/admin/requests/{request_id}`         | Delete request    |
| **PUT**    | `/admin/requests/block/{request_id}`   | Block request     |
| **PUT**    | `/admin/requests/unblock/{request_id}` | Unblock request   |

### AI Endpoints

| Method   | Endpoint          | Description                       |
| -------- | ----------------- | --------------------------------- |
| **GET**  | `/ai/reports/`    | Generate daily/monthly report     |
| **GET**  | `/ai/statistics/` | Analyze request statistics        |
| **POST** | `/ai/price/`      | Suggest a price for a new request |

---

### Generate Reports
Generate structured daily or monthly reports based on job requests to track trends, budgets, and skill demands.

#### Example Request:  
```bash
GET http://127.0.0.1:8000/ai/reports/?date=2025-01-16&report_type=daily
```
#### Example Output:
[AI Generated Daily Report](static/report_output.txt)
### Generate Statistics  
Get statistics based on job request titles, including trends, budget distribution, and competition.  

#### Example Request: 

```bash
GET http://127.0.0.1:8000/ai/statistics/?title=Data Engineer
```
#### Example Output:
[AI Generated Statistics](static/statistics_output.txt)

### Price Suggestion
This endpoint estimates a budget for a job request based on similar past requests.
```bash
POST http://127.0.0.1:8000/ai/price
```
#### Request Body:
```{
    "title": "Web Developer",
    "description": "Develop a website from scratch with a responsive design."
}
```

## Code Formatting & Linting

To ensure code quality and follow PEP8 standards:

```sh
flake8 app/ --max-line-length=100
isort .
```
## Additional Notes

- **Admin Access:** You must be an **admin** to access `/admin/*` routes.
- **CORS Enabled:** API allows requests from trusted domains.
- **Logging:**
  - **General Logs:** `logs/app.log`
  - **Admin Actions:** `logs/admin.log`
  - **Errors:** `logs/errors.log`

---

## Contributor

**Nazar Urbanskyi** – Python Developer

## License

This project is licensed under the MIT License. Feel free to use and modify!
