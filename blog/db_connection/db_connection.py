import pymongo
url = "mongodb+srv://sumaia:mongo123@cluster01.wgamolu.mongodb.net/"
client = pymongo.MongoClient(url)
db = client["myblog"]
