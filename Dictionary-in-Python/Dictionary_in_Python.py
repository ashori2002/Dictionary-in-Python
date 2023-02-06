
from multiprocessing import Value
from typing import Type


mydict = {"red": "ghermez", "green": "sabz", "blue": "abi"}
print(mydict["green"])
# _______________________________________________________
del mydict["red"]
print(mydict)
# _______________________________________________________
print(mydict.get("green", "====ERROR===="))
# _______________________________________________________
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
for item in mydict:
    print(item)
    print(type(item).__name__)

# _______________________________________________________
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
for item in mydict.items():
    print(item)
    print(type(item).__name__)

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
for key, value in mydict.items():
    print(f"key: {key} and value: {value}")



#--------------------------------------------------------
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
for value in mydict.values():
    print(value)
