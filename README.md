## AI-Powered Document Query System**

### 🧾 Overview

This full-stack application allows users to upload documents (e.g., PDF, ppt, csv etc) and ask questions related to the content. The system utilizes **NLP (Natural Language Processing)** techniques to analyze documents and return context-aware answers, enabling a **Retrieval-Augmented Generation (RAG)** experience.

---

### 🛠 Tech Stack

| Layer    | Technology                     |
| -------- | ------------------------------ |
| Backend  | Python, FastAPI                |
| Frontend | HTML, JavaScript, Tailwind CSS |
| NLP      | spaCy (and custom logic)       |
| Parsing  | PyMuPDF (PDF document parsing) |

---

### 📁 Project Structure

```
ai-planet-assignment-main/
│
├── backend/                    # Backend (FastAPI)
│   ├── app/
│   │   ├── api/                # API route definitions
│   │   ├── core/               # Config settings
│   │   ├── db/                 # Database models & base setup
│   │   ├── schemas/            # Pydantic schemas
│   │   └── services/           # PDF & NLP logic
│   ├── run.py                  # Entry point for FastAPI
│   └── requirements.txt        # Python dependencies
│
├── frontend/                   # Frontend (HTML + Tailwind + JS)
│   ├── index.html              # Main HTML
│   ├── tailwind.config.js      # Tailwind config
│   └── package.json            # Frontend dependencies
│
└── Readme.md                   # Existing documentation
```

---

### ⚙️ Setup Instructions

#### 🔧 Backend (Python + FastAPI)

1. **Navigate to backend directory**

   ```bash
   cd backend
   ```

2. **Create virtual environment (optional but recommended)**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the backend server**

   ```bash
   python run.py
   ```

#### 🌐 Frontend (Tailwind + JS)

1. **Navigate to frontend directory**

   ```bash
   cd frontend
   ```

2. **Install Node.js dependencies**

   ```bash
   npm install
   ```

3. **Start the development server**

   ```bash
   npm run dev  # or equivalent script defined in package.json
   ```

---

### 🔍 Features

* Upload and parse PDF documents
* Natural language question answering over document contents
* Simple and clean frontend interface
* Modular backend service separation (NLP / PDF parsing)
* Typed schema validation with Pydantic

---

### 📌 API Endpoints

| Method | Endpoint  | Description                          |
| ------ | --------- | ------------------------------------ |
| POST   | `/upload` | Upload and parse a document (PDF)    |
| POST   | `/query`  | Ask a question related to a document |

> Full endpoint details are defined in `backend/app/api/endpoints.py`.

---

### 🚀 Deployment

For deployment:

* **Backend**: Can be hosted on services like [Render](https://render.com), [Heroku](https://www.heroku.com), or any cloud VM (e.g., AWS EC2).
* **Frontend**: Can be deployed using [Vercel](https://vercel.com), [Netlify](https://www.netlify.com/), or even GitHub Pages (with bundling).

---

### 👤 Author / Contributors

* Sandeep Kumar
* Contribution welcome via PRs or issue discussions.

---

### 🪪 License

This project is under the **MIT License** .
