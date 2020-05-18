#numbers-game
import time
print("Think of any number x .... I will wait go on do it.. if you have done it now multiply the number by 2")
time.sleep(2)
print("Now think of another number y which is even ... and now add this number to the above result...")
time.sleep(2)
print("Now divide the result obtained by two and then subract it from the number you thought at first(number x)...")
time.sleep(2)
value=int(input("Now enter the resultant value or the obtained result :"))
time.sleep(2)
print("Now the half of the even number you though (number y) is :",value,"\nAnd the even number is :",value*2)
