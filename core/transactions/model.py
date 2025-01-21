from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class TransactionDataModel:
    """
    representation of the data from the file and
    """
    tran_id: int
    
    description: str
    amount: str
    tran_date: date
    raw_category: str
    notes: str

    post_date: date | None    
    upload_id: int
