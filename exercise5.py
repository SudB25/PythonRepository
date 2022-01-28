# # <--Dictionary-->

# a = {}

# a["key1"] = "Amarnath"
# a["key2"] = "Deloitte"
# a[3] = "India"
# print(a)

# print(a["key2"])

# b = {"id":'100', "name":"Amar", "desig": "trainer"}
# print(b)

# print(b["id"])
a = {"next":{"next":{"next":{"next":{"next":{"next":{"final":{"employer":"Deloitte"}}}}}}}}
# print(a["next"]["next"]["next"]["next"]["next"]["next"]["final"]["employer"])

# for x in a:
#     print(x)
# for key in a():
#     print(key,':',Value)
# def get_all_values(a):
#     for key, value in a.items():
#         if type(value) is dict:
#             get_all_values(value)
#         else:
#             print(value)

# a = {"next":{"next":{"next":{"next":{"next":{"next":{"final":{"employer":"Deloitte"}}}}}}}}

# get_all_values(a)
a = {"next":{"next":{"next":{"next":{"next":{"next":{"final":{"employer":"Deloitte"}}}}}}}}

b = a["next"]
while b != "Deloitte":
    if b == "final":
        b = b["final"]
    elif b == "employer":
        b = b["employer"]
    else:
        b = b["next"]

print(b)
