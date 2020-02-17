from OurClass.DBClass import DBClass

db = DBClass("localhost", "root", "", "htcs5606")
result = db.selectQuery("product")

for x in result:
    print(x)