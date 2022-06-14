from backend.schemas.user import User
from fastapi import APIRouter
from backend.models.user import users
from backend.config.db import conn

user = APIRouter()


@user.get("/")
async def fetch_users():
    return conn.execute(users.select()).fetchall()


@user.get("/{id}")
async def fetch_user(id: int):
    return conn.execute(users.select().where(users.c.id == id)).first()


@user.post("/")
async def create_users(user: User):
    conn.execute(users.insert().values(name=user.name, email=user.email, password=user.password))
    return conn.execute(users.select()).fetchall()


@user.put("/{id}")
async def update_user(id: int, user: User):
    conn.execute(
        users.update().values(name=user.name, email=user.email, password=user.password).where(users.c.id == id)
    )
    return conn.execute(users.select()).fetchall()


@user.delete("/{id}")
async def delete_users(id: int):
    conn.execute(users.delete().where(users.c.id == id))
    return conn.execute(users.select()).fetchall()
