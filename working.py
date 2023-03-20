from fastapi import FastAPI

app = FastAPI()

@app.get("/") #using get method// slash "/" is the end point
def home():
    return {"Data": "Test"}

#we defined a function home just below the method

@app.get("/about")
def about():
    return {"Data": "About"}
