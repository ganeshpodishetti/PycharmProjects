a = int(input())
b = int(input())
g = (a/b) * 100
if 90 <= g < 100:
    print("A")
elif 80 <= g < 90:
    print ("B")
elif 70 <= g < 80:
    print ("C")
elif 60 <= g < 70:
    print ("D")
else:
    print ("F")
