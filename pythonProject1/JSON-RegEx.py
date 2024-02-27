"""
# The JSON (is a syntext for storing and exchanging data, JSON is text, written with JavaScript object notation).
# convert json to python
import json
x = '{"name":"Done", "age":19, "favorite":"computer"}'

y = json.loads(x)

print(y["name"])

# convert python to json
import json

x = {
    "name": ["Done", "Vang sure"],
    "age": 19,
    "favorite": ["sport", "some game", "computer", "science"],
    "like beer": True,
    "beer always": False
}

print(json.dumps(x, indent=2, separators=(".", "=")))

# write JSON file
import json
info_dict = {
    "first name": "Mr. Done",
    "last name": "Yang",
    "age": 19,
    "student": True,
    "carree": None
}
with open("page info json", "w") as json_file:
    json.dump(info_dict, json_file, indent=4)

# read JSON file
import json
with open("page info json", "r") as py_data:
    data = json.load(py_data)
    print(data)
    print(type(data))

# The RegEx module
# findall function
import re

txt = "mr done pass the exam"
score = "mr done get 29 point"
# how to use RegEx metacharacters
x = re.findall("false|pass", txt)
print(x)

# to count the white space in the content
import re

txt = "Returns a match where the string contains a white space character"

x = re.findall("\s", txt)
y = re.findall("[a-z]", txt)

if x:
    print("it matched")
else:
    print("not match")
cht = len(txt)-len(x)
print("all position in txt: ", len(txt), "\nthe white space in txt is: ", len(x), "\nso, the charter is: ", cht,
      "\nExample", "\n-all charter: ", y, "\n-all white space: ", x)
"""

