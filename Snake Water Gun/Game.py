print("==============Snake Water Gun==============")
player_1 = input("Enter the name of player 1 ")
player_2 = input("Enter the name of player 2 ")
won_1 = 0
won_2 = 0
round_no = 1

quit_game = "n"

while quit_game=="n":

    print(f'''Won Matches
             {player_1}: {won_1}
             {player_2}: {won_2}''')
    print("===================================")
    print(f"ROUND: {round_no}")
    c_1 =input(f" Player 1 ({player_1}) Enter choice (Snake, Water, Gun: )")
    choice_1 = c_1.lower()

    c_2 =input(f" Player 2 ({player_2}) Enter choice (Snake, Water, Gun: )")
    choice_2 = c_2.lower()

    if choice_1=="snake" and choice_2=="water":
        print(f"{player_1} wins.")
        won_1+=1
    elif choice_1=="water" and choice_2=="gun":
        print(f"{player_1} wins.")
        won_1+=1
    elif choice_1=="gun" and choice_2=="snake":
        print(f"{player_1} wins.")
        won_1+=1 
    elif choice_1==choice_2:
        print("This round is draw.")
    else:
        print(f"{player_2} wins")
        won_2+=1

    round_no+=1
    print("======================================")
    quit_choice = int(input("Press\n1.Continue\n2.Quit"))
    if quit_choice==1:
        quit_game = "n"
    else: 
        break


print(f''' Won Matches
          {player_1}: {won_1}
          {player_2}: {won_2}''')
print("===================================")
