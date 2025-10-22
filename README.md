# FitRequest

I built and deployed a fullstack workout request platform where users can request workouts suitable for their needs. The application includes user authentication, a database for saving user and request data, and a modern React frontend.

## Live Demo

[**View the live site here**](https://www.fitrequest.dev/)

## Technologies Used

- React
- CSS3
- FastAPI for backend REST APIs
- SQLAlchemy ORM
- PostgreSQL
- Docker
- Neon for cloud database hosting
- Vercel for frontend deployment
- Fly.io for backend deployment
- CI/CD for automated builds and deployments

## What I learned

- Gained experience building and deploying a full-stack application from scratch.
- Learned how to design and structure RESTful APIs using FastAPI and SQLAlchemy.
- Implemented JWT authentication for secure login and user sessions.
- Practiced database schema design, migrations, and handling relationships in PostgreSQL.
- Used Docker to containerise backend.
- Set up CI/CD pipelines to automate testing and deployment with Vercel and Fly.io.
- Strengthened knowledge of frontend–backend integration and API communication.

## Preview

Here is a preview of the website

![Screenshot of my website](screenshots/s1.png)
![Screenshot of my website](screenshots/s2.png)
![Screenshot of my website](screenshots/s3.png)
![Screenshot of my website](screenshots/s4.png)
![Screenshot of my website](screenshots/s5.png)
![Screenshot of my website](screenshots/s6.png)

## Running locally 

### With Docker

1. Clone the repository:
```bash
git clone https://github.com/aimei60/fitrequest.git
cd fitrequest
```

2. Build and start the backend API:
```bash
docker compose up --build
```

3. Start the frontend:
```bash
cd frontend
npm install
npm run dev
```

### Without Docker

1. Clone the repository:
```bash
git clone https://github.com/aimei60/fitrequest.git
cd fitrequest/backend
```

2. Create and activate a virtual environment:
```bash python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the API:
```bash
uvicorn main:app --reload
```

## Credits

- [GreatStack - React sign up form](https://www.youtube.com/watch?v=8QgQKRcAUvM) - for signup/login styling inspiration.

- [Python API Development](https://www.youtube.com/watch?v=0sOvCWFmrtA) - for learning backend concepts such as CRUD operations, schemas, routers, JWT authentication, Docker, and CI/CD, which I adapted for my own project using Fly.io and Vercel instead of Heroku.
