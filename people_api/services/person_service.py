from sqlalchemy.orm import Session
from models.person import Person

def person_exists(firstname: str, db: Session) -> bool:
    if not firstname:
        return False
    person = db.query(Person).filter(Person.first_name.ilike(firstname.strip())).first()
    return bool(person)
