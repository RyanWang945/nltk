from fastapi import FastAPI


app = FastAPI(title="NLTK API Server")


@app.get("/")
@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("api_server:app", host="0.0.0.0", port=28000)
