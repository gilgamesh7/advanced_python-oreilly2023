from fastapi import FastAPI
from uvicorn import run

from time import sleep

from requests import get
from threading import Thread


app = FastAPI()

@app.get('/test')
async def test():
    return({'success': True})

def target():
    sleep(1)
    print(get('http://localhost:8000/test'))

if __name__ == '__main__':
    thread = Thread(target=target)
    thread.start()
    run(app)
    thread.join()