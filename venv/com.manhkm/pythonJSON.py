# JSON: support for story and exchanges data:
# truy xuat den nhung gia tri trong mot JSON:
#
# function json.dumps() -> use in json;
#
#
#
#
import json;    # import thu vien cua json;

valJSON = '{"name":"ManhKM", "age":25, "city":"Ha Noi"}';
objJSON = {
    "name":"Tom",
    "univercity":"UET",
    "address" : "Ha Noi"
};

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
};

valParseJSON = json.loads(valJSON);     #why use function loads if not load
valDumpsObjectJSON = json.dumps(objJSON);
valOfX = json.dumps(x, indent=10);       #After have data -> how to use it:, indent -> 10-> 10 khoang cach trang


print("My name is: " + valParseJSON["name"]);
print("His name is: " + valDumpsObjectJSON);
print("valOfX is: " + valOfX);

#json.dumps(x, indent=4, sort_keys=True)

#json.dumps(x, indent=4, separators=(". ", " = "))


