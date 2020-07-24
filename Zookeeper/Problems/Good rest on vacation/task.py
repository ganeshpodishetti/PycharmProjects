# put your python code here
days = int(input())
food = int(input())
flight = int(input())
hotel = int(input())
tot = (days * food) + (flight * 2) + (hotel * (days - 1))
print(tot)
