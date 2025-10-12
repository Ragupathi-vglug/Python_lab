import pymongo

# Create Mongo connection

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# Create database
mydb = myclient["Emp"]

# Check if DB exists
dblist = myclient.list_database_names()
if "Emp" in dblist:
    print("The database exists.")
else:
    print("This DB is not available")

# Create collection
mycol = mydb["emp1"]
clist = mydb.list_collection_names()
if "emp1" in clist:
    print("The Collection exists.")
else:
    print("Collection is not available")

# Insert a single document
mydict = {"name": "raman", "age": 20, "dept": "IT"}
mycol.insert_one(mydict)
print("Inserted one document successfully.")

# Read the document
x = mycol.find_one()
print("\nRead a single document after insertion")
print("----------------------------------------")
print(x)

# Insert multiple documents
mylist = [
    {"name": "Ragu", "age": 20, "dept": "IT"},
    {"name": "Bala", "age": 22, "Course": "IT", "Gender": "Male"},
    {"name": "Saran", "age": 19, "address": "New St, VPM"},
    {"name": "raman", "Design": "Manager", "Dept": "Mech"}
]
mycol.insert_many(mylist)
print("\nInserted multiple documents successfully.")

# Read all documents
print("\nRead all the documents after insertion")
print("----------------------------------------")
x = mycol.find()
for i in x:
    print(i)

# Delete a single document
dlist = {"name": "raman"}
mycol.delete_one(dlist)
print("\nOne document deleted...")

# Read remaining documents
print("\nDocuments after deleting one record")
print("----------------------------------------")
x = mycol.find()
for i in x:
    print(i)

# Delete many documents
mycol.delete_many(dlist)
print("\nDocuments deleted successfully (all with name 'raman').")

# Read remaining documents
print("\nDocuments after deleting many records")
print("----------------------------------------")
x = mycol.find()
for i in x:
    print(i)

# Drop the collection
mycol.drop()
print("\nCollection deleted successfully.")
