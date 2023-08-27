from fastapi import FastAPI
from uvicorn import run

app = FastAPI()

@app.get('/test')
async def test():
    return({'success': True})

if __name__ == '__main__':
    run(app)