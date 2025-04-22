from sqlalchemy.orm import Session
from models.history import History

def log_request(url: str, result: bool, db: Session):
    entry = History(
        request=url,
        response=str(result)
    )
    db.add(entry)
    db.commit()
