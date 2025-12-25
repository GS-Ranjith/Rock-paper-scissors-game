import random

print("-------welcome to the \"rock\",\"Paper\",\"scissor\"🎮😊---------")

user_score=0
computer=0
tie=0

for i in range(10):

    print('''-------------🤖 Rules of the game 🤖--------------
        🎱 rock  vs 📄 paper ==> paper wins 🎮
        📄 paper vs ✂️  scissor ==> scissor win 🎮
        ✂️  scissor vs 🎱 rock ==> rock wins 🎮''')


    while True:
        print('\n 1=>🎱 rock \n 2=> 📄 paper \n 3=> ✂️  scissor \n enter the number according the names ')
        print()
        try:
            user_input=int(input("enter the number according the names :"))
            if user_input>3 or user_input<=0:
                print("enter the number 1 to 3 to choose the value")
            else:
                break
        except ValueError as e:
            print(" the value must be an number 😊")
            print(e)

    computer_value=random.randint(1,3)
    a="🎱 rock"
    b="📄 paper"
    c="✂️  scissor "
    print()
    if user_input==1 and computer_value==2:
        print(f"your choice is{a} and coumputer choice is{b}==>paper wins 🎮")
        computer+=1

    elif user_input==2 and computer_value==1:
        print(f"your choice is{b} and coumputer choice is{a}==>paper wins 🎮")
        user_score+=1

    elif user_input==2 and computer_value==3:
        print(f"your choice is{b} and coumputer choice is{c}==>scissor win 🎮")
        computer+=1
    elif user_input==3 and computer_value==2:
        print(f"your choice is{c} and coumputer choice is{b}==>scissor win 🎮")
        user_score+=1
    elif user_input==3 and computer_value==1:
        print(f"your choice is{c} and coumputer choice is{a}==>rock wins 🎮")
        computer+=1
    elif user_input==1 and computer_value==3:
        print(f"your choice is{a} and coumputer choice is{c}==>rock wins 🎮")
        user_score+=1
    else:
        print("both choosed the same so it is tied")
        tie+=1
print()
    

if user_score > computer:
    print ("you won the game==>",user_score,"🤩")
    print('computer_score==>',computer)
    print("number of ties==>",tie)
elif user_score < computer:
    print ("computer won the game==>",computer,"😣")
    print('your_score==>',user_score)
    print("number of ties==>",tie)
else:
    print("the game is tied")
    print('computer_score==>',computer)
    print('your_score==>',user_score)
    print("number of ties==>",tie)

print()
print("-------Thanks for playing the game-------")

