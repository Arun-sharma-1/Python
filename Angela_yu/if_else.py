print("Welcome to Treasure Island Your mission is to find treasure. ")
choose_dir_1 = input("Enter left or right ")
if(choose_dir_1 == 'right'):
    print('Game over:')
    exit()
else:
    x = input('swim or wait ')
    if(x == 'swim'):
        print('Game over:')
        exit()
    else:
        door = input('Which door u want to choose: Blue or Yellow ')
        if(door!='Yellow'):
            print('Game over:')
            exit();
        else:
            print('HURRAY!! YOU WON')
