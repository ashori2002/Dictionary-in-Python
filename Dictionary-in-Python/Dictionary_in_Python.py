
from multiprocessing import Value


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
# _______________________________________________________
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
for key, value in mydict.items():
    print(f"key: {key} and value: {value}")