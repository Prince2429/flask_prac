import json

def load_db():
    with open("question.json") as file:
        return json.load(file)

def save_db():
    with open('question.json','w') as file:
        return json.dump(db,file) 

db=load_db()    