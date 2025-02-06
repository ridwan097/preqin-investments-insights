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

Copy the `.env.example` file or Create a `.env.local` or file in the `frontend` directory and add the following:

```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
```

Replace `http://localhost:8000` with the actual backend API URL if different or just.

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
