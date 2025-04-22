import os
from dotenv import load_dotenv
from fastapi import FastAPI
from controllers.root_controller import router as root_router
from controllers.person_controller import router as person_router
import uvicorn

from db.connection import SessionLocal, engine,Base
from services.fetch_people import fetch_people_data

# Load environment variables
load_dotenv()
if not os.getenv("PORT") or not os.getenv("NATIONALITY"):
    raise EnvironmentError("❌ Missing critical env variables: PORT or NATIONALITY.")
nationality = os.getenv("NATIONALITY", "us")
port_str = os.getenv("PORT")
port = int(port_str)

# Create DB tables
Base.metadata.create_all(bind=engine)

# Initialize app
app = FastAPI()
app.include_router(root_router)
app.include_router(person_router)


@app.on_event("startup")
def startup_event():
    session = SessionLocal()
    people_data = fetch_people_data(nationality)
    session.add_all(people_data)
    session.commit()
    session.close()
    print(f"✅ 100 {nationality.upper()} people inserted into PostgreSQL using SQLAlchemy.")



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)