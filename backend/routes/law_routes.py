from fastapi import APIRouter, Query
from backend.database import db
from typing import List, Optional
from backend.models.law_model import Law

router = APIRouter()

@router.get("/laws", response_model=List[Law])
def get_laws(
    category: Optional[str] = Query(None, description="Filter by category (e.g., criminal, civil)"),
    act: Optional[str] = Query(None, description="Filter by act name (e.g., IPC, Consumer Protection Act)"),
    section: Optional[str] = Query(None, description="Filter by section number (e.g., 420)"),
    keyword: Optional[str] = Query(None, description="Search by keyword (e.g., fraud, consumer rights)")
):
    """Fetch laws based on category, act, section, or keywords."""
    query = {}

    if category:
        query["category"] = category.lower()
    if act:
        query["act"] = {"$regex": act, "$options": "i"}  # Case-insensitive search
    if section:
        query["section"] = int(section) if section.isdigit() else section
    if keyword:
        query["keywords"] = {"$in": [keyword.lower()]}

    laws = list(db.laws.find(query, {"_id": 0}))
    return laws
