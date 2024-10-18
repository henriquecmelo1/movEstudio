from app import app


@app.get("/")
async def root():
    return {"Hello": "World"}


