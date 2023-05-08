from fastapi import FastAPI

app = FastAPI()

inventory = {
    1:{
        "name":"milk",
        "price":"2.99",
        "brand":"Nido",
    }

   
}
# New App
@app.get("/get-item/{item_id}")
def get_item(item_id:int):
    return inventory[item_id]
