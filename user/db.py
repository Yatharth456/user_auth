import pymongo

def start_db():
    client = pymongo.MongoClient("mongodb+srv://goswami2001yatharth:zaqYdXCS7Z1Nx0Sb@cluster0.x2mdlxn.mongodb.net/test")
    db = client.test
    return db