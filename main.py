from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/post")
def poster():
    return "I am posting darling"

@app.post("/createpost")
def createpost():
    return "success"