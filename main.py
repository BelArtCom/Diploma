from fastapi import FastAPI

# Создаю экземпляр приложения FastAPI
app = FastAPI()

# Определяю базовый маршрут
@app.get('/')
async def root():
    """
    Базовый маршрут
    """
    return {'message': 'Hello, FastAPI!'}

# GET-запрос - получение данных:
# @app.get('/items/{item_id}')
# async def read_item(item_id: int):
#     return {'item_id': item_id}


# POST-запрос - добавление данных
# from pydantic import BaseModel
# class Item(BaseModel):
#     name: str
#     price: float
#
# @app.post('/items/')
# async def create_item(item: Item):
#     return {'name': item.name, 'price': item.price}


# PUT-запрос - обновление данных
# @app.put('/items/{item_id}')
# async def update_item(item_id: int, item: Item):
#     return {'item_id': item_id, 'name': item.name, 'price': item.price}


# DELETE-запрос - удаление данных
# @app.delete('/items/{item_id}')
# async def delete_item(item_id: int):
#     return {'message': 'Item deleted', 'item_id': item_id}


# uvicorn main:app --reload
# uvicorn main:app --reload --host 0.0.0.0
# uvicorn main:app --reload --port 8080
# http://127.0.0.1:8000



