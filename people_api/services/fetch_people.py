import requests
from typing import List
from models.person import Person

def fetch_people_data(nationality: str) -> List[Person]:
    API_URL = f"https://randomuser.me/api/?results=100&nat={nationality}"

    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []

    return [
        Person(
            first_name=p["name"]["first"],
            last_name=p["name"]["last"],
            email=p["email"],
            nationality=p["nat"]
        )
        for p in data.get("results", [])
    ]
