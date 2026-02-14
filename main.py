from fastapi import FastAPI
from api.user_api.main import user_router
from database import Base, engine



# Создание моделей в бд
Base.metadata.create_all(engine)


app = FastAPI(docs_url="/")
app.include_router(user_router)


# uvicorn main:app --reload
