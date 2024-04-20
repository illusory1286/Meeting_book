from fastapi import FastAPI
app = FastAPI()  # Fastapi 物件


# 建立網站的首頁
@app.get("/")
def index():
    return "Hello FastAPI"
