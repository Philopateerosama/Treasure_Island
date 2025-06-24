print('''_________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
        | |-%-------|
        \ | %  ))   |
         \|%________|''')
print("welcome to Treasure island.")
direction = input("Your mission is to find the treasure.\n left or right? \n")
if direction == "left":
    x = input("nice choice now choose to swim or wait!\n")
    if x == "wait":
        door = input("its good for you to wait.\n which door blue , yellow or red")
        if door == "yellow":
            print("You Win!")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")