#The tic-tac-toe game, a pet-training-project 
#No pygame,draw and play in terminal
#I guess its a worst way to write this game...


field_size = 3
field = [1,2,3,4,5,6,7,8,9]


#draw a field by a hand(yea,just training press buttons)
def draw_field():
    for i in range(field_size):
        print('_' * 4 * field_size)
        print((" " * 3 + "│") *3)
        print("",field[i*field_size], '│', field[1 + i*3], '│', field[2 + i*3],'│')
        print(("_" * 3 + "│") *3)
        
        
        
def game_action(index,char):
    #Doing action
    if index > 9 or index < 1 or field[index-1] in ('X','O'):
        return False
    
    field[index-1] = char
    return True

def check_win():
    win = False
    win_combination = (
        (0,1,2),(3,4,5),(6,7,8),(0,4,8),(0,3,6),(1,4,7),(2,5,8),(2,4,6)
    )
    
    for pos in win_combination:
        if (field[pos[0]] == field[pos[1]] and field[pos[1]] == field[pos[2]]):
            win = field[pos[0]]
    return win

def start_game():
    current_player = 'X'
    step = 1
    draw_field()
    
    
    while (step<10) and (check_win() == False):
        index = input('Player ' + current_player + ' turn!' + ' Enter field number (0 - quit)')
        if (index == "0"):
            break
        
        
        if (game_action(int(index),current_player)):
            print('Good turn')
            
            if (current_player == 'X'):
                current_player = 'O'
            else:
                current_player = 'X'
            
            draw_field()
            step += 1
        else:
            print("Wrong turn! Try again!")
            
    print(check_win() + 'Won!')
        
        
        

#python ttt-game.py

print("Welcome to Tic-Tac-Toe!")
start_game()


    



