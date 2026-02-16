user = { 
    "language" : "English", 
    "fontSize" : "10px", 
    "font" : "Sans-serif", 
    "time" : "AEST", 
    "job" : "Student"
}

# print(user["language"])

user["time"] = "AEDT"

user["relationship status"] = "dating"

remove_item = user.pop("time")

# print(user)

# print(user.get("salary", "Not found"))

try: 
    print(user.get("salary"))
except: 
    print("Not found")

sorted_dict = sorted(user.items(), key = lambda x: x[1])

print(sorted_dict)