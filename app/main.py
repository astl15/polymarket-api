from fastapi import FastAPI

app = FastAPI(
        title="PolymarketClient"
)

@app.get("/")
def ping():
        return {"status": "RUNNING"}