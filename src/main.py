from fastapi import FastAPI, Form
import uvicorn
import logging

import random

from prometheus_fastapi_instrumentator import Instrumentator

# Базовая настройка для консоли
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(asctime)s | %(message)s",
    datefmt="%d.%m.%Y %H:%M:%S",
    handlers=[logging.StreamHandler()]  # Вывод в консоль
)

# Добавляем обработчик для файла
file_handler = logging.FileHandler('app.log', mode='a', encoding='utf-8')
file_formatter = logging.Formatter("%(levelname)s | %(asctime)s | %(message)s", datefmt="%d.%m.%Y %H:%M:%S")
file_handler.setFormatter(file_formatter)

# Получаем корневой логгер и добавляем обработчик файла
root_logger = logging.getLogger()
root_logger.addHandler(file_handler)

app = FastAPI(
    title="TEST YANDEX API",
    version="1.0.0",
)
Instrumentator().instrument(app).expose(app)


test_users = ['Sugawara', 'Ivan']

@app.get('/')
async def get_start(data: str = None, testing: str = None):
    global test_users
    data = random.randint(0, 100)
    testing = random.randint(2, 50)
    logging.info(f'GET | / | {test_users[random.randint(0, 1)]} | data={data} testing={testing}')

@app.get('/main')
async def get_main(data: str = None, testing: str = None):
    global test_users
    data = random.randint(100, 1000)
    testing = random.randint(20, 500)
    logging.info(f'GET | /main | {test_users[random.randint(0, 1)]} | data={data} testing={testing}')


if __name__ == '__main__':
    uvicorn.run(app="main:app", host='0.0.0.0', port=9999, reload=True, access_log=False,)
