from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Zep Render Deploy Test is running!"}
