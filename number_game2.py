#number-game
import time
print("Think of any number .... I will wait go on do it.. if you have done it now multiply the number by 2 and add 2 to the result..")
time.sleep(2)
print("If you have completed all the steps above then multiply the last result with 5 and add 5 to it")
time.sleep(2)
print("Now enter the value that you got and let me do the magic and guess the number that you thought")
val=input("The value :")
nv=val[:-1]
new=int(nv)
time.sleep(2)
print("Now the number you thought is :",new-1)
