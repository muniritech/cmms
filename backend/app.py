"""FastAPI backend skeleton — proves verification target."""
from fastapi import FastAPI

app = FastAPI(title="CMMS", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
