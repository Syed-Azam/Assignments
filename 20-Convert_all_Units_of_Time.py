# Ai Assignment 20 - Convert All Units Of Time Into Seconds
print("Convert All Units Of Time Into Seconds")
print("Enter Unit of Time")
u = input("Day, Hour, Minute [D/H/M] : ").upper()
v = int(input("Enter Value : "))
if u == "D":
    s = v * 24 * 60 * 60
    c_unit = "Day/Days"
elif u == "H":
    s = v * 60 * 60
    c_unit = "Hour/Hours"
elif u == "M":
    s = v * 60
    c_unit = "Minute/Minutes"
else:
    print("Wrong Unit of Time")
    s = 0
print("There are",s,"Seconds in",v,c_unit)
