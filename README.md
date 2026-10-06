# Indonesian Language Learning App

A web app for learning Indonesian vocabulary, built with React, Flask, and MySQL.

## Tech Stack

- **Frontend:** React (Vite)
- **Backend:** Python / Flask
- **Database:** MySQL
- **Deployment:** AWS (planned)

## Running Locally

**Backend:**
```bash
cd backend
venv\Scripts\activate
python app.py
```

**Frontend:**
```bash
cd frontend
npm run dev
```

## Current Features

- Vocabulary organized by category: basic phrases, numbers, colors, grammar particles, and pronouns
- List view and flashcard mode for each category
- REST API endpoints for fetching all words or by category

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/health` | Health check |
| GET | `/api/words` | Fetch all words |
| GET | `/api/words/<category>` | Fetch words by category |

## Testing

**Backend:**
```bash
cd backend
venv\Scripts\activate
pytest test_app.py -v
```

**Frontend:**
```bash
cd frontend
npx vitest
```

## Database Setup

Create the database in MySQL, then seed it with:
```bash
cd backend
python seed.py
```
