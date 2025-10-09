# FastAPI + Streamlit Text File Demo

A simple demo showing how to send and retrieve data between **FastAPI** (backend) and **Streamlit** (frontend) using a text file for storage.

---

## 🚀 How It Works
- **FastAPI** exposes two endpoints:
  - `POST /add_data` → Add name & age to `data.txt`
  - `GET /get_data` → Read and return all data
- **Streamlit** provides a UI for adding and viewing entries.

---

## 🧰 Dependencies
Install required libraries:
```bash
pip install fastapi uvicorn streamlit requests

Step 1: Start FastAPI Backend

Open a terminal and navigate to the backend folder:

cd backend
Run the FastAPI server:

uvicorn main:app --reload
Step 2: Start Streamlit Frontend

Open another terminal (keep backend running).

Navigate to the frontend folder:

cd ../frontend


Run Streamlit:

streamlit run app.py
