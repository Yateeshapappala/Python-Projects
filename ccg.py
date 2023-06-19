import random
print("choices are red,yellow,orange,green,blue")
p=0
ct=0
while True:
    u=input("enter ur choice ")
    u=u.lower()
    print(u)
    if (u!="red" and u!="yellow" and u!="orange" and u!="green" and u!="blue"):
        print("enter valid colour")
        continue
    print("your choice is",u)
    c=random.randint(1,5)
    if c==1:
        com_choice="red"
    if c==2:
        com_choice="yellow"
    if c==3:
        com_choice="orange"
    if c==4:
        com_choice="green"
    if c==5:
        com_choice="blue"
    print("computer choice is",com_choice)
    if u==com_choice:
        p=p+1
    else:
       ct=ct+1
    print("your score is",p)
    print("computer score is",ct)
    q=input("want to play again y/n? ")
    if q=="n"or q=="N":
        break
if p>ct:
    print("you won!!")
elif p==ct:
    print("game is tied")
else:
    print("oops! computer won the game")

