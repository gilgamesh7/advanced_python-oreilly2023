from fastapi import FastAPI
from uvicorn import run

from requests import get
from multiprocessing import Process


app = FastAPI()

@app.get('/test')
async def test():
    return({'success': True})

def target():
    print(get('http://localhost:8000/test'))

if __name__ == '__main__':
    process = Process(target=target)
    process.start()
    run(app)
    process.join()