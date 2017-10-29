import json

jsonString = '''{"arrayOfNums":[{"number":0},{"number":1},{"number":2}],
  "arrayOfFruits":[{"fruit":"apple"},{"fruit":"banana"},{"fruit":"pear"}]}'''
jsonObj = json.loads(jsonString)

print(jsonObj["arrayOfNums"])
print(jsonObj["arrayOfNums"][1])
print(jsonObj["arrayOfNums"][1]["number"]+
      jsonObj["arrayOfNums"][2]["number"])
print(jsonObj["arrayOfFruits"][2]["fruit"])
