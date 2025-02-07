
info = {
    "key" : "value",
    "name" : "khushi",
    "age" : 18,
}
print(info)
print(info["key"]) #accessing values

#NESTED DICTIONARY-
student = {
    "name":"KHUSHI WALIA",
    "Subject Marks" : {
        "Phy" : 91,
        "Chem" : 90,
        "Hindi" : 95,
    }
}
print(student)
#dictionary methods
#1. dict.keys() - returns all the keys
print(info.keys())

#typecast-
print(list(info.keys()))

#dict.values() - returns all values
print(info.values())
print(list(info.values()))

#dict.items() - returns all pairs of (key,value)
print(info.items())
#dict.get("key") - returns the key according to value
print(info["name"])
print(info.get("name"))