import ch01.main

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("ch01.main:app", host="localhost", port=8000, reload=True)

