print('''           o    .   _     .
             .     (_)         o
      o      ____            _       o
     _   ,-/   /)))  .   o  (_)   .
    (_)  \_\  ( e(     O             _
    o       \/' _/   ,_ ,  o   o    (_)
     . O    _/ (_   / _/      .  ,        o
        o8o/      \_/ / ,-.  ,oO8/( -TT
       o8o8O | } }  / /   \Oo8OOo8Oo||     O
      Oo(""o8"""""""""""""""8oo""""""")
     _   `\`'                  `'   /'   o
    (_)    \                       /    _   .
         O  \           _         /    (_)
   o   .     `-. .----<(o)_--. .-'
      --------(_/------(_<_/--\_)--------hjw ''')
print("welcome to Treasure island.")
direction = input("Your mission is to find the treasure.\n left or wight? \n")
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