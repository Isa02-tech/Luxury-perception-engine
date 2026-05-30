from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Luxury Perception Engine is running"}

@app.get("/analyze")
def analyze(brand: str):
    return {
        "brand": brand,
        "score": 80,
        "summary": f"{brand} is perceived as luxury but evolving in public opinion."
    }
