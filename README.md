## Getting Started

### **1. Clone the Repository**

```bash
git clone https://github.com/ridwan097/preqin-investments-insights.git
cd preqin-investments-insights
```

---

### **2. Set Up Environment Variables**

Copy the `.env.example` file in the `frontend` directory and name it `.env.local` or Create a `.env.local` file in the `frontend` directory and add the following:

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

## Prerequisites

Ensure you have one of the following installed:

- [OrbStack](https://orbstack.dev/) (Recommended for macOS users)
- [Docker](https://www.docker.com/) (Available on all platforms)
