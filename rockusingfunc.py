def player(p1, p2):
 if p1 == "rock":
    if p2 == "scissors":
        print("rock beats scissors, p1 wins")
    else:
        print("paper beats rock,p2 wins")
 elif p1 == "paper":
    if p2 == "rock":
            print("Paper covers rock! p1 wins!")
    else:
            print("Scissors cuts paper! p2 wins")
 elif p1 == "scissors":
    if p2 == "paper":
        print("Scissors cuts paper! p1 win!")
    else:
        print("Rock smashes scissors! p2 wins")
 else:
     print("invalid entry")

p1 = str(input("p1 choose(rock,paper,scissors):"))
p2 = str(input("p2 choose(rock,paper,scissors):"))
print(player(p1,p2))