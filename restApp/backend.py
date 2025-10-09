from fastapi import FastAPI
from pydantic import BaseModel
import os

backend = FastAPI()
DATA_FILE = "database.txt"

# Ensure the text file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        f.write("")

class User(BaseModel):
    name: str
    email: str


def read_users():
    users = []
    with open(DATA_FILE, "r") as f:
        for line in f:
            if line.strip():
                id, name, email = line.strip().split("|")
                users.append({"id": int(id), "name": name, "email": email})
    return users


def write_user(name, email):
    users = read_users()
    new_id = len(users) + 1
    with open(DATA_FILE, "a") as f:
        f.write(f"{new_id}|{name}|{email}\n")
    return {"id": new_id, "name": name, "email": email}

# fetching the record
@backend.get("/users")
def get_users():
    return read_users()

#adding the records
@backend.post("/users")
def add_user(user: User):
    new_user = write_user(user.name, user.email)
    return {"message": "User added successfully", "user": new_user}
