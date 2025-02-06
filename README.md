# Preqin Full-Stack Interview Task

This is a full-stack application built for the Preqin technical interview task. The project consists of a **FastAPI** backend and a **Next.js** frontend, working together to display investor commitments and their breakdown.

---

## Features

## Getting Started

### **1. Clone the Repository**

```bash
git clone https://github.com/ridwan097/preqin-investments-insights.git
cd preqin-investments-insights
```

---

### **2. Set Up Environment Variables**

Create a `.env.local` file in the `frontend` directory and add the following:

```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
```

Replace `http://localhost:8000` with the actual backend API URL if different.

---

### **3. Run with Docker Compose**

#### **Using Docker Compose**

1. Build and start the services:
   ```bash
   docker-compose up --build
   ```
2. Access the application:
   - **Backend (FastAPI)**: [http://localhost:8000](http://localhost:8000)
   - **API Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)
   - **Frontend (Next.js)**: [http://localhost:3000](http://localhost:3000)

#### **Using OrbStack**

OrbStack fully supports `docker-compose`, so the same commands can be used:

1. Ensure OrbStack is running.
2. Build and start the services:
   ```bash
   docker-compose up --build
   ```
3. Access the application as described above.

---

### **4. Stopping the Containers**

To stop and remove all running containers, use:

```bash
docker-compose down
```

---

## Running Locally Without Docker

If you prefer to run the application without Docker or OrbStack, follow these instructions:

### **Backend**

To run the backend as a standalone application, view the `README.md` in the `backend` directory.

### **Frontend**

To run the frontend as a standalone application, view the `README.md` in the `frontend` directory.

---

## Technologies Used

- **Backend**: FastAPI, SQLite, Uvicorn.
- **Frontend**: Next.js, React, TypeScript, Tailwind CSS, shadcn/ui.
- **State Management**: Redux Toolkit.
- **Charts**: Recharts.
- **Containerization**: Docker, OrbStack.

---

## Troubleshooting

### **1. Docker Errors**

- Ensure Docker or OrbStack is installed and running.
- Check for port conflicts (e.g., `8000` or `3000` already in use).

### **2. Database Issues**

- If the database is missing, ensure `backend/db/db.py` has run successfully.
- Verify that the `DATABASE_URL` environment variable in `docker-compose.yml` points to the correct SQLite file.

---

## License

This project is for the Preqin technical interview task and is not intended for production use.
