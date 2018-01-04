#python projects

*****************************************************
#project1--guessing game
import random

num = random.randint(1,10)

guess = int(input('Guess a number between 1 and 10'))

times=1

while guess != num:
    guess = int(input('Guess again'))
    times=times+1
    if times==3:
        break     
if guess == num:
    print('You WIN!')
else:
    print('You LOSE! The number was' + str(num))
******************************************************************

#project2--rock paper scissor game
Computer_choice=("Rock")
User_choice=input("ENTER Rock,Paper, or Scissor : \n")

if Computer_choice==User_choice :
    print("TIE")
elif User_choice == "Rock" and Computer_choice == "Scissor":
    print("WIN")
elif User_choice == "Paper" and Computer_choice == "Rock":
    print("WIN")
else:
    print("YOU LOSE :( COMPUTER WINS :D ")
******************************************************************
    
#project3--rock paper scissor game with random computer choice
import random

choices=['rock','paper','scissor']
Computer_choice=random.choice(choices)

User_choice=input("ENTER rock,paper, or scissor : \n")

if Computer_choice==User_choice :
    print("TIE")
elif User_choice == "rock" and Computer_choice == "scissor":
    print("WIN")
elif User_choice == "paper" and Computer_choice == "rock":
    print("WIN")
else:
    print("YOU LOSE :( COMPUTER WINS :D ")
********************************************************************

#project4-- guess game with only one guess allowed
print("WELCOME!")
g=input("Guess the number: ")
guess=int(g)
if guess==5
    print("YEAH! You win :) ")
else:
    if guess > 5
        print("you way ahead boy!!")
    else:
        print("its low boy!!")
print("game over boy!!")
*******************************************************************

project5-- guess game with number generated randomly by program

import random

n=random.randint(1,20)

print("WELCOME!")
g=input("Guess the number: ")
guess=int(g)
if guess==n:
    print("YEAH! You win :) ")
else:
    if guess > n:
        print("you way ahead boy!!")
    else:
        print("its low boy!!")
print("game over boy!!")
***************************************************************

project6-- guess game with limited guess and number generated randomly by program

import random

num = random.randint(1,10)

guess = int(input('Guess a number between 1 and 10'))

times=1

while guess != num:
    guess = int(input('Guess again'))
    times=times+1
    if times==3:
        break     
if guess == num:
    print('You WIN!')
else:
    print('You LOSE! The number was' + str(num))
*******************************************************************

program7--to interchange the value of two given 

a=int(input('What is your first value:'))
b=int(input('What is your second value:'))
a=a+b #a=a+b
b=a-b #b=a-b=a+b-b=a b=a
a=a-b #a=a-b=b a=b
print('a is:',a,'b is:',b)
****************************************************************************

project8--to find largest odd and even number from given input numbers

n=int(input("Enter the number of elements to be in the list:"))
b=[]
for i in range(0,n):
    a=int(input("Element: "))
    b.append(a)
c=[]
d=[]
for i in b:
    if(i%2==0):
        c.append(i)
    else:
        d.append(i)
c.sort()
d.sort()
count1=0
count2=0
for k in c:
    count1=count1+1
for j in d:
    count2=count2+1
print("Largest even number:",c[count1-1])  #(c[count1-n] where we can adjust it to find the the number from last--n=2--c[count1-2]would be second last integer)
print("Largest odd number",d[count2-1])
*****************************************************************

project9--to find LCM of given two numbers

print('We are going to find LCM of two numbers')
print('So Enter the two numbers')
n1=int(input('Enter the first number: '))
n2=int(input('Enter the second number: '))
if (n1>n2):
    min1=n1
else:
    min1=n2
while(1):
    if (min1%n1==0 and min1%n2==0):
        print('LCM is: ',min1)
        break
    min1=min1+1
 ***************************************************************************
 
 project10--to find prime number from given upper limit
 
 n=int(input('Enter the upper limit: '))
for a in range(2,n+1):
    k=0
    for i in range(2,a//2):
        if(a%i==0):
            k=k+1
    if(k<=0):
        print(a)
*****************************************************************************
 
project11--to find the numbers divisible by given number from given limit
 
uplim=int(input('What is your upper limit:'))
lowlim=int(input('What is your lower limit:'))
a=int(input('Number to be divided with is:'))
for i in range(lowlim,uplim+1):
    if (i%a==0):
        print(i)
************************************************************************************
 
 project12--to arrange given 3 number in all possible ways
 
 a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
d=[]
d.append(a)
d.append(b)
d.append(c)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j&j!=k&k!=i):
                print(d[i],d[j],d[k])
*******************************************************************************

project13--to find second largest number from given input elements
#elements=(input is like 2 3 5 8 6)

n = int(input('Enter the number of elements:'))

sequence=input('Elements:').split()
lst1=[]
for i in sequence:
        lst1.append(int(i))

print(lst1)

lst2=[]
for j in lst1:
        if j not in lst2:
                   lst2.append(j)
lst2.sort()
print(lst2)

count=0
for l in lst2:
        count=count+1
print('Second largest number is:',lst2[count-2])
****************************************************************************

project14--to arrange given three numbers in such a way that its sum would never be equal to another given number

x = int(input())
y = int(input())
z = int(input())
n = int(input())
d=[]
p=0
for i in range(0,x+1):
        for j in range(0,y+1):
                for k in range(0,z+1):
                        if( i+j+k != n):
                                d.append([])
                                d[p]=[i,j,k]
                                p+=1
                               
print(d)
**************************************************************************************
