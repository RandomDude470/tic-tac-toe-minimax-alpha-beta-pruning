import pygame
import LogicFn
import ai

pygame.init()
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_WIDTH))
game_array = [[0,0,0],[0,0,0],[0,0,0]]
coordinates=[[(55,50),(170,50),(285,50)],
             [(55,160),(170,160),(285,160)],
             [(55,280),(170,280),(285,280)]]
playable = True

def update_board(gameArray):
    for i in range(3):
        for j in range(3):
            if gameArray[i][j]==1:
                screen.blit(X,coordinates[i][j])
            elif gameArray[i][j]==-1:
                screen.blit(O,coordinates[i][j])
    pygame.display.update()
def draw_line(line_number):
    if line_number == 1-1 :
        line = pygame.Rect(SCREEN_WIDTH * 0.17 ,SCREEN_HEIGHT * 0.18,0.7*SCREEN_WIDTH,8 )
        pygame.draw.rect(screen,(0,0,0),line)
    elif line_number == 2-1 :
        line = pygame.Rect(SCREEN_WIDTH * 0.17 ,SCREEN_HEIGHT * 0.45,0.7*SCREEN_WIDTH,8 )
        pygame.draw.rect(screen,(0,0,0),line)
    elif line_number == 3-1 :
        line = pygame.Rect(SCREEN_WIDTH * 0.17 ,SCREEN_HEIGHT * 0.76,0.7*SCREEN_WIDTH,8 )
        pygame.draw.rect(screen,(0,0,0),line)
    elif line_number == 4-1 :
        line = pygame.Rect(SCREEN_HEIGHT * 0.195,SCREEN_WIDTH * 0.15 ,8,0.7*SCREEN_WIDTH )
        pygame.draw.rect(screen,(0,0,0),line)
    elif line_number == 5-1 :
        line =  pygame.Rect(SCREEN_HEIGHT * 0.475,SCREEN_WIDTH * 0.15 ,8,0.7*SCREEN_WIDTH )
        pygame.draw.rect(screen,(0,0,0),line)
    elif line_number == 6-1 :
        line =pygame.Rect(SCREEN_HEIGHT * 0.765,SCREEN_WIDTH * 0.15 ,8,0.7*SCREEN_WIDTH )
        pygame.draw.rect(screen,(0,0,0),line)
    elif line_number == 6 :
        pygame.draw.line(screen , (0,0,0),(55,45),(310,300),12)
    elif line_number == 7 :
        pygame.draw.line(screen , (0,0,0),(337,45),(55,330),12)


grid_line_h_1 = pygame.Rect(SCREEN_WIDTH * 0.1 ,SCREEN_HEIGHT * 0.3,0.8*SCREEN_WIDTH,8 )
grid_line_h_2 = pygame.Rect(SCREEN_WIDTH * 0.1 ,SCREEN_HEIGHT * 0.6,0.8*SCREEN_WIDTH,8 )
grid_line_V_1 = pygame.Rect(SCREEN_HEIGHT * 0.325,SCREEN_WIDTH * 0.1 ,8,0.8*SCREEN_WIDTH )
grid_line_V_2 = pygame.Rect(SCREEN_HEIGHT * 0.625,SCREEN_WIDTH * 0.1 ,8,0.8*SCREEN_WIDTH )
rect = pygame.Rect(10,10,50,50)
tr = True
turn_croix = True
O = pygame.image.load('o.png')
X = pygame.image.load('x-symbol.png')
X= pygame.transform.scale(X,(50,50))
O= pygame.transform.scale(O,(50,50))
while tr :
    screen.fill((175,130,90))
    
    pygame.draw.rect(screen,(0 , 0 ,0),grid_line_h_1)
    pygame.draw.rect(screen,(0 , 0 ,0),grid_line_h_2)
    pygame.draw.rect(screen,(0 , 0 ,0),grid_line_V_1)
    pygame.draw.rect(screen,(0 , 0 ,0),grid_line_V_2)
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT : 
            tr =  False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and playable:  # Left mouse button
                
                mouse_pos = pygame.mouse.get_pos()
                
                if mouse_pos[0] < SCREEN_HEIGHT * 0.325 and mouse_pos[1] < SCREEN_HEIGHT * 0.3 : 
                    if game_array[0][0]!= 0:
                        print('occupied')
                    elif turn_croix :
                        game_array[0][0] = 1
                        
                        
                        turn_croix = not turn_croix
                    else :
                        game_array[0][0] = -1
                        
                        
                        turn_croix = not turn_croix
                    print('1:1')
                elif mouse_pos[0] > SCREEN_HEIGHT * 0.325 and mouse_pos[0] < SCREEN_HEIGHT*0.625 and mouse_pos[1] < SCREEN_HEIGHT * 0.3 :
                    print('1:2')
                    if game_array[0][1]!= 0:
                        print('occupied')
                    elif turn_croix :
                        game_array[0][1] = 1
                        
                        turn_croix = not turn_croix
                    else :
                        game_array[0][1] = -1
                        turn_croix = not turn_croix
                elif mouse_pos[0] > SCREEN_HEIGHT * 0.625 and mouse_pos[1] < SCREEN_HEIGHT * 0.3 :
                    if game_array[0][2]!= 0:
                        print('occupied')
                    elif turn_croix :
                        game_array[0][2] = 1
                        turn_croix = not turn_croix
                    else :
                        game_array[0][2] = -1
                        turn_croix = not turn_croix
                    print('1:3')
                elif mouse_pos[0] < SCREEN_HEIGHT * 0.325 and mouse_pos[1] > SCREEN_HEIGHT * 0.3 and mouse_pos[1] < SCREEN_HEIGHT * 0.6 :
                    print('2:1')
                    if game_array[1][0]!= 0:
                        print('occupied')
                    elif turn_croix :
                        game_array[1][0] = 1
                        turn_croix = not turn_croix
                    else :
                        game_array[1][0] = -1
                        turn_croix = not turn_croix
                elif mouse_pos[0] > SCREEN_HEIGHT * 0.325 and mouse_pos[0] < SCREEN_HEIGHT * 0.625 and mouse_pos[1] > SCREEN_HEIGHT * 0.3 and mouse_pos[1] < SCREEN_HEIGHT * 0.6 :
                    print('2:2')
                    if game_array[1][1]!= 0:
                        print('occupied')
                    elif turn_croix :
                        game_array[1][1] = 1
                        turn_croix = not turn_croix
                    else :
                        game_array[1][1] = -1
                        turn_croix = not turn_croix
                elif mouse_pos[0] > SCREEN_HEIGHT * 0.625 and mouse_pos[1] > SCREEN_HEIGHT * 0.3 and mouse_pos[1] < SCREEN_HEIGHT * 0.6 :
                    print('2:3')
                    if game_array[1][2]!= 0:
                        print('occupied')
                    elif turn_croix :
                        game_array[1][2] = 1
                        turn_croix = not turn_croix
                    else :
                        game_array[1][2] = -1
                        turn_croix = not turn_croix
                elif mouse_pos[0] < SCREEN_HEIGHT * 0.325 and mouse_pos[1] > SCREEN_HEIGHT * 0.6 :
                    print('3:1')
                    if game_array[2][0]!= 0:
                        print('occupied')
                    elif turn_croix :
                        game_array[2][0] = 1
                        turn_croix = not turn_croix
                    else :
                        game_array[2][0] = -1
                        turn_croix = not turn_croix
                elif mouse_pos[0] > SCREEN_HEIGHT * 0.325 and  mouse_pos[0] < SCREEN_HEIGHT * 0.625 and mouse_pos[1] > SCREEN_HEIGHT * 0.6 :
                    print('3:2')
                    if game_array[2][1]!= 0:
                        print('occupied')
                    elif turn_croix :
                        game_array[2][1] = 1
                        turn_croix = not turn_croix
                    else :
                        game_array[2][1] = -1
                        turn_croix = not turn_croix
                elif mouse_pos[0] > SCREEN_HEIGHT * 0.625 and mouse_pos[1] > SCREEN_HEIGHT * 0.6 :
                    print('3:3')
                    if game_array[2][2]!= 0:
                        print('occupied')
                    elif turn_croix :
                        game_array[2][2] = 1
                        turn_croix = not turn_croix
                    else :
                        game_array[2][2] = -1
                        turn_croix = not turn_croix
                
                if LogicFn.is_game_over(game_array)[0] == 3 :
                    playable = False
                    print('x wins')
                elif LogicFn.is_game_over(game_array)[0] == -3:
                    playable = False
                    print('o wins')
                elif  LogicFn.is_game_over(game_array)[0]== 0:
                    playable = False
                    print('draw')
                else:
                    playable =False
                    game_array = ai.minimax_alphaBeta(game_array,turn_croix,-10,10)[0]
                    print('after ai')
                    print(game_array)
                    turn_croix = not turn_croix
                    playable = True
                    
                LogicFn.print_matrix(game_array)
    
    draw_line(LogicFn.is_game_over(game_array)[1])
    update_board(game_array)