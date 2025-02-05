from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
from typing import List, Optional
from models.commitment import Commitment
from models.investor import Investor

app = FastAPI()


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

# local run command is:uvicorn main:app --reload
