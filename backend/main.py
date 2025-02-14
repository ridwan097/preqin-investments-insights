from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
from typing import List, Optional
from models.commitment import Commitment
from models.investor import Investor
from openai import OpenAI
import requests


app = FastAPI()
# openai.api_key = "YOUR_API_KEY"
DEEPSEEK_API_KEY=""



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_PATH = "investments_insights.db"

def get_db_connection():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


@app.get("/investors", response_model=List[Investor])
def get_investors():
    """Fetch all investors with their total commitments."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = """
    SELECT investors.id, investors.name, COALESCE(SUM(commitments.amount), 0) AS total_commitment
    FROM investors
    LEFT JOIN commitments ON investors.id = commitments.investor_id
    GROUP BY investors.id, investors.name
    """
    
    cursor.execute(query)
    investors = cursor.fetchall()
    conn.close()
    
    return [{"id": row["id"], "name": row["name"], "total_commitment": row["total_commitment"]} for row in investors]


@app.get("/investors/{investor_id}/commitments", response_model=List[Commitment])
def get_investor_commitments(investor_id: int, asset_class: Optional[str] = Query(None)):
    """Fetch commitments of a specific investor, optionally filtering by asset class."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = "SELECT asset_class, amount FROM commitments WHERE investor_id = ?"
    params = [investor_id]
    
    if asset_class:
        query += " AND asset_class = ?"
        params.append(asset_class)
    
    cursor.execute(query, params)
    commitments = cursor.fetchall()
    conn.close()
    
    if not commitments:
        return []
            # raise HTTPException(status_code=404, detail="No commitments found for this investor.")

    
    return [{"asset_class": row["asset_class"], "amount": row["amount"]} for row in commitments]


@app.post("/summarize")
def summarize_data(investor_id: int, asset_class: str = None):
    """Fetch investment data and generate an AI-powered summary using DeepSeek."""
    if not DEEPSEEK_API_KEY:
        raise HTTPException(status_code=500, detail="DeepSeek API key is missing.")

    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = """
    SELECT asset_class, SUM(amount) as total_amount
    FROM commitments
    WHERE investor_id = ?
    """
    params = [investor_id]

    if asset_class:
        query += " AND asset_class = ?"
        params.append(asset_class)

    query += " GROUP BY asset_class"
    cursor.execute(query, params)
    commitments = cursor.fetchall()
    conn.close()

    # Convert data to a readable format
    investment_summary = "\n".join([
        f"{row['asset_class']}: £{row['total_amount']:,}" for row in commitments
    ])

    if not investment_summary:
        investment_summary = "No data available for this investor."

    # Send formatted data to DeepSeek API
    deepseek_url = "https://api.deepseek.com/v1/chat/completions"
    headers = {"Authorization": f"Bearer {DEEPSEEK_API_KEY}"}
    payload = {
        "model": "deepseek-chat",
        "messages": [{"role": "system", "content": f"Summarize the investment commitments:\n{investment_summary}"}]
    }

    response = requests.post(deepseek_url, json=payload, headers=headers)

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to get response from DeepSeek API")

    return {"summary": response.json()["choices"][0]["message"]["content"]}


# @app.post("/summarize-open-ai")
# def summarize_data(investor_id: int, asset_class: str = None):
#     """Fetch investment data and generate an AI-powered summary."""
#     conn = get_db_connection()
#     cursor = conn.cursor()

#     # Query to get commitments
#     query = """
#     SELECT asset_class, SUM(amount) as total_amount
#     FROM commitments
#     WHERE investor_id = ?
#     """
#     params = [investor_id]

#     if asset_class:
#         query += " AND asset_class = ?"
#         params.append(asset_class)

#     query += " GROUP BY asset_class"
#     cursor.execute(query, params)
#     commitments = cursor.fetchall()
#     conn.close()

#     # Convert data to a readable format
#     investment_summary = "\n".join([
#         f"{row['asset_class']}: £{row['total_amount']:,}" for row in commitments
#     ])

#     if not investment_summary:
#         investment_summary = "No data available for this investor."

#     # Send formatted data to LLM
#     prompt = f"""
#     The following are the investment commitments for Investor ID {investor_id}:
#     {investment_summary}
    
#     Summarize the key insights from this data.
#     """
    
#     response = client.chat.completions.create(
#         model="gpt-4",
#         messages=[{"role": "system", "content": prompt}]
#     )
    
#     return {"summary": response.choices[0].message["content"]}

# # local run command is:uvicorn main:app --reload
