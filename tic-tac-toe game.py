def pattern(xstate,ystate):
    zero= "X" if xstate[0]==1 else ("o" if ystate[0]==1 else 0)
    one= "X" if xstate[1]==1 else ("o" if ystate[1]==1 else 1)
    two= "X" if xstate[2]==1 else ("o" if ystate[2]==1 else 2)
    three= "X" if xstate[3]==1 else ("o" if ystate[3]==1 else 3)
    four= "X" if xstate[4]==1 else ("o" if ystate[4]==1 else 4)
    five= "X" if xstate[5]==1 else ("o" if ystate[5]==1 else 5)
    six= "X" if xstate[6]==1 else ("o" if ystate[6]==1 else 6)
    seven= "X" if xstate[7]==1 else ("o" if ystate[7]==1 else 7)
    eight= "X" if xstate[8]==1 else ("o" if ystate[8]==1 else 8)
    print(f" {zero} |  {one}  |  {two} ")
    print("---|---|---")
    print(f" {three} | {four} |  {five} ")
    print("---|---|---")
    print(f" {six} | {seven} |  {eight} ")
        

   
def winner(xstate,ystate):
        wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for win in wins:
            if(xstate[win[0]] + xstate[win[1]] + xstate[win[2]]==3):
                print("X wins the game")
                return 1
            elif (ystate[win[0]] + ystate[win[1]] + ystate[win[2]]==3):
                print("O wins the game")
                return 0
            return 2
    
xstate=[0,0,0,0,0,0,0,0,0]
ystate=[0,0,0,0,0,0,0,0,0]
print("Welcome to tic-tac-toe Game")
turn=1
pattern(xstate,ystate)
while(True):
    if(turn==1):
        print("player X's turn")
        xstate[int(input())]=1
    else:
        print("player O's turn")
        ystate[int(input())]=1
    pattern(xstate,ystate)
    winn=winner(xstate,ystate)
    if(winn!=2):
        break
    turn=1-turn

