"""score game
1.ask user to input any number between 0 to 4
   0=exit
   1=add score
   2=remove score
   3=sort the score in assending order
  4=print the score
2.declare a variable named score and assign it with the empty list
3.use while loop until the user input is equal to 0
4.if user input is 1 ask user to enter the score they want to add
5.use append method to add userinput in list score
6.if user input is 2 then ask user to enter the score they want top remove.
7.use remove method tpo remove the user input score from list score.
8.if user input is equal to 3 .then use sort method to sort the score in asseending order.
9. if user input is equal to 0 the cancel the game and exit.  

"""

print("ok, lets start the game ")
print("0=exit")
print("1=add score")
print("2=remove score")
print("3=sort score in assending order")
print("4=print the score")
un=input("enter one number from 0 to 4 ")
un=int(un)
score=[]
while un!=0:
    if un==1:
       un1=input("enter the score you want to add ")
       un1=int(un1)
       score.append(un1)
       un=input("enter one number from 0 to 4 ")
       un=int(un)

    elif un==2:
        un1=input("enter the score you wat to remove ")
        un1=int(un1)
        score.remove(un1)
        un=input("enter one number from 0 to 4 ") 
        un=int(un)

    elif un==3:
         score.sort()
         print(score)
         un=input("enter one number from 0 to 4 ")
         un=int(un)
    elif un==4:
        print(score)
        un=int(input("enter one number from 0 to 4 "))
    elif un==5:
        un1=int(input("enter the no u want to count the repetation" ))
        print(score.count(un1)) 
        un=int(input("enter one number from 0 to 4 "))

    else:
        print("sorry this number is not avaialable")
        un=int(input("please enter one number from 0 to 4 ") )   