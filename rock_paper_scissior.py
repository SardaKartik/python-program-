def rock_paper_scissor(num1,num2,bit1,bit2):
    p1=int(num1[bit1])%3
    p2=int(num2[bit2])%3
    if(player_one[p1]=="rock" and player_two[p2]=="rock"):
        print("match tied")
    elif(player_one[p1]=="scissor" and player_two[p2]=="scissor"):
        print("match tied")
    elif(player_one[p1]=="paper" and player_two[p2]=="paper"):
        print("match tied")
    elif(player_one[p1]=="rock" and player_two[p2]=="paper"):
        print("player 2 won ")
    elif(player_one[p1]=="rock" and player_two[p2]=="scissor"):
        print("player 1 won")
    elif(player_one[p1]=="scissor" and player_two[p2]=="paper"):
        print("player 1 won")
    elif(player_one[p1]=="scissor" and player_two[p2]=="rock"):
        print("player two won")
    elif(player_one[p1]=="paper" and player_two[p2]=="rock"):
        print("player one won")
    elif(player_one[p1]=="paper" and player_two[p2]=="scissor"):
        print("player two won")



player_one= {0:"rock",1:"scissor",2:"paper"}
player_two={0:"scissor",1:"papaer",2:"rock"}
# here we have created a dictionory to do the assignment

while(1):
    num1=(input("enter your choice "))
    num2=(input("enter your choice "))
    bit1=int(input("player 1 enter the sceret bit position "))
    bit2=int(input("player 2 enter the seceret bit position "))
    rock_paper_scissor(num1,num2,bit1,bit2)
    ch=input("Do you want to continue y/n")
    if(ch=='n'):
        break







