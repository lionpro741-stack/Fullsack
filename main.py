from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI()

# ✅ Разрешаем GitHub Pages
origins = [
    "https://lionpro741-stack.github.io/Fullsack/"  # <- поменяй на свой GitHub Pages
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # или ["*"] для всех
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Данные
ideas = ["Угадай число", "Камень ножницы бумага", "Онлайн викторина"]

class AddIdea(BaseModel):
    idea: str

# Получение всех идей
@app.get("/all_ideas")
async def get_all_ideas():
    return {"ideas": ideas}

# Добавление идеи
@app.post("/add_idea")
async def add_idea(i: AddIdea):
    if not i.idea.strip():
        raise HTTPException(status_code=400, detail="Идея пуста")
    ideas.append(i.idea)
    return {"added": i.idea}

# Получение случайной идеи
@app.get("/random_idea")
async def random_idea():
    if not ideas:
        raise HTTPException(status_code=404, detail="Нет идей")
    return {"idea": random.choice(ideas)}