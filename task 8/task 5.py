sampleDict = { 
  "name": "Harsh",
  "age":25, 
  "salary": 80000, 
  "city": "New york" }

keys = ["name", "salary"]

newDict = {k: sampleDict[k] for k in keys}
print(newDict)