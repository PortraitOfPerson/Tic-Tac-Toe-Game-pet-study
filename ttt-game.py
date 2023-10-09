#The tic-tac-toe game by Nikita Kharchenko 
#A pet-training-project (the code was not invented by me, the project was taken for training purposes)
#No Pygame,draw and play in terminal


field_size = 3
field = [1,2,3,4,5,6,7,8,9]



def draw_field():
    print('_' * 4 * field_size)
    for i in range(field_size):
        print(" " * 3 + "│")
        print(field[i*field_size],'│')
        
        
        
        
def game_action():
    #Doing action
    pass

def check_win():
    pass

def start_game():
    draw_field()

print("Welcome to Tic-Tac-Toe!")
start_game()


    



