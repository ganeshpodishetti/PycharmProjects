a = str(input())
b = a.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
print(b.lower())
