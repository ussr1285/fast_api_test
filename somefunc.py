import subprocess
from models import Item 
from fastapi import Body

class somefunc:
    def __init__(self):
        self.name = "test"
    
    def text_return_n(self, text: str):
        text = text + "n"
        return text
    
    def run_ipconfig(self):
        result = subprocess.run(["ipconfig"], capture_output=True, text=True)
        return result.stdout
    
    def write_to_file(self, item: Item = Body(...)):
        with open("./test.txt", 'w') as file:
            file.write(item.name)

# 문자열을 NFC 형태로 정규화
# import unicodedata
# normalized_name = unicodedata.normalize('NFC', class_name)