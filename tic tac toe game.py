def printboard(board):
    for i in range(1,10):
        print(board[i],end="|")
        if i%3==0:
            print()
            print("_"*6)

def play_game(board,pos,player):
    if board[pos]!='x' and board[pos]!='o':
        board[pos]=player
    else:
        print("enter the empty position")
    return board

def check(board,player):
    if board[1]==board[4]==board[7]:
        return player
    elif board[2]==board[5]==board[8]:
        return player
    elif board[3]==board[6]==board[9]:
        return player
    elif board[1]==board[2]==board[3]:
        return player
    elif board[4]==board[5]==board[6]:
        return player
    elif board[7]==board[8]==board[9]:
        return player
    elif board[1]==board[5]==board[9]:
        return player
    elif board[7]==board[5]==board[3]:
        return player
    else:
        return "lose"

   
board={i:i for i in range(1,10)}
printboard(board)
choice='y'
xcount=0
ocount=0

while choice.lower()=='y':
    current_player='x'
    move_count=0
    while True:
        pos=int(input(f"enter a postion you want to choose player {current_player} "))
        if pos>=1 and pos<10:
            board=play_game(board,pos,current_player)
            printboard(board)
            result=check(board,current_player)
            if result=='x' or result=='o':
                if current_player=='x':
                    xcount+=1
                else:
                    ocount+=1
                break
            move_count+=1
            if move_count==9:
                print("IT'S A TIE")
                break
        else:
            print("enter valid position")
        if current_player=='x':
            current_player='o'
        else:
            current_player='x'
    print(f"Score => X: {xcount}, O: {ocount}")
    choice = input("Do you want to play again? (y/n): ")
    if choice.lower() == 'y':
        board = {i: i for i in range(1, 10)}  
        printboard(board)
print("        PLAYER 1(X) GOT ",xcount,"SCORE")
print("        PLAYER 2(O) GOT ",ocount,"SCORE")
if xcount>ocount:
    print("             PLAYER 1 WON")
elif xcount==ocount:
    print("             OHH! IT'S TIE")
else:
    print("             PLAYER 2 WON")
