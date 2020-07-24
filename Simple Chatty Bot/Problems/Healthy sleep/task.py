A = int(input())
B = int(input())
H = int(input())

if A <= H <= B:
    print("Normal")
else:
    print("Deficiency" if A > H else "Excess")
