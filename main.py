from typing import Union

from fastapi import FastAPI

from models import Item 
import somefunc

app = FastAPI()

testfunc = somefunc.somefunc()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    result = testfunc.text_return_n(str(q))
    return {"item_id": item_id, "q": q, "result": result}

@app.get("/ipconfig")
def return_ipconfig():
    result = testfunc.run_ipconfig()
    return {"result": result}

@app.post("/writefile")
def write_file(item_id: int, item: Item):
    result = testfunc.write_to_file(item)
    return {"item_id": item_id, "result": result}

