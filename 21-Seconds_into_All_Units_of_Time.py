# Ai Assignment 20 - Convert Seconds into all Units Of Time
print("Convert Seconds into All Units Of Time")
ss = int(input("Input Seconds: "))
d = ss // (24 * 3600)
ss = ss % (24 * 3600)
h = ss // 3600
ss = ss % 3600
m = ss // 60
ss = ss % 60
s = ss
print("D:H:M:S = "+str(d)+":"+str(h)+":"+str(m)+":"+str(s))
