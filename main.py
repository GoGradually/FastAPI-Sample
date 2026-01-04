import fastapi.main

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("startfastapi.main:app", host="localhost", port=8000, reload=True)

