````markdown
# Frontend Application

This is the frontend application for the Preqin Full-Stack Interview Task. It is built using **Next.js**, **TypeScript**, **Tailwind CSS**, and **shadcn/ui** for styling and components. The application interacts with the backend API to fetch and display investor commitments and their breakdown.

---

## Features

- Displays total commitments for all investors.
- Allows users to filter commitments by investor.
- Provides additional filtering by asset class for a selected investor.
- Charts for visualizing data:
  - **Total Commitments by Investor**.
  - **Commitments Breakdown**.
  - **Commitments Grouped by Asset Class**.

---

## Prerequisites

Ensure you have the following installed on your system:

- [Node.js](https://nodejs.org/) (v16 or higher)
- [npm](https://www.npmjs.com/) or [Yarn](https://yarnpkg.com/)

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ridwan097/preqin-investments-insights.git
   cd preqin-investments-insights/frontend
   ```
````

2. **Install Dependencies**:
   Using npm:

   ```bash
   npm install
   ```

   Or using Yarn:

   ```bash
   yarn install
   ```

3. **Environment Variables**:
   Create a `.env.local` file in the `frontend` directory and add the following:
   ```env
   NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
   ```
   Replace `http://localhost:8000` with the actual backend API URL if different.

---

## Running the Application

### Locally

Start the development server:

```bash
npm run dev
```

Or using Yarn:

```bash
yarn dev
```

Access the application at [http://localhost:3000](http://localhost:3000).

### With Docker

1. Ensure you are in the root directory of the project (where `docker-compose.yml` is located).
2. Run the following command:
   ```bash
   docker-compose up --build
   ```
3. Access the frontend at [http://localhost:3000](http://localhost:3000).

---

## Available Scripts

Here are the commonly used scripts for this project:

### `npm run dev`

Starts the development server.

### `npm run build`

Builds the production-ready application.

### `npm start`

Starts the production server after building the application.

---

## Technologies Used

- **[Next.js](https://nextjs.org/):** React framework for building the frontend.
- **[TypeScript](https://www.typescriptlang.org/):** Type-safe JavaScript.
- **[Tailwind CSS](https://tailwindcss.com/):** Utility-first CSS framework.
- **[shadcn/ui](https://shadcn.dev/):** Styled components library.
- **[Redux Toolkit](https://redux-toolkit.js.org/):** State management for handling API calls and global state.
- **[Recharts](https://recharts.org/):** Charting library for visualizing data.
