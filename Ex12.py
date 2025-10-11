import pymongo

# Create Mongo connection
print("\n")
print("\n")
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# Create database
mydb = myclient["Emp"]

# Check if DB exists
dblist = myclient.list_database_names()
if "Emp" in dblist:
    print("\tThe database exists.")
else:
    print("\tThis DB is not available")

# Create collection
mycol = mydb["emp1"]
clist = mydb.list_collection_names()
print("\t")
if "emp1" in clist:
    print("\tThe Collection exists.")
else:
    print("\tCollection is not available")

# Insert a single document
mydict = {"name": "raman", "age": 20, "dept": "IT"}
mycol.insert_one(mydict)
print("\t")
print("\tInserted one document successfully.")

# Read the document
x = mycol.find_one()
print("\n\tRead a single document after insertion")
print("\t----------------------------------------")
print("\t",x)

# Insert multiple documents
mylist = [
    {"name": "Ragu", "age": 20, "dept": "IT"},
    {"name": "Bala", "age": 22, "Course": "IT", "Gender": "Male"},
    {"name": "Saran", "age": 19, "address": "New St, VPM"},
    {"name": "raman", "Design": "Manager", "Dept": "Mech"}
]
mycol.insert_many(mylist)
print("\n\tInserted multiple documents successfully.")

# Read all documents
print("\n\tRead all the documents after insertion")
print("----------------------------------------")
x = mycol.find()
for i in x:
    print("\t",i)

# Delete a single document
dlist = {"name": "raman"}
mycol.delete_one(dlist)
print("\n\tOne document deleted...")

# Read remaining documents
print("\n\tDocuments after deleting one record")
print("----------------------------------------")
x = mycol.find()
for i in x:
    print("\t",i)

# Delete many documents
mycol.delete_many(dlist)
print("\n\tDocuments deleted successfully (all with name 'raman').")

# Read remaining documents
print("\n\tDocuments after deleting many records")
print("----------------------------------------")
x = mycol.find()
for i in x:
    print("\t",i)

# Drop the collection
mycol.drop()
print("\n\tCollection deleted successfully.")
print("\n")
print("\n")
