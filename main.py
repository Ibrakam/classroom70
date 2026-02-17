from fastapi import FastAPI
from api.user_api.main import user_router
from api.class_api.main import class_router
from api.hw_api.main import hw_router
from database import Base, engine



# Создание моделей в бд
Base.metadata.create_all(engine)


app = FastAPI(docs_url="/")
app.include_router(user_router)
app.include_router(hw_router)
app.include_router(class_router)


# uvicorn main:app --reload
