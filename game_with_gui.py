import tkinter as tk
from tkinter import messagebox, PhotoImage
import random

# === Original Logic ===
HumPlayer = "X"
AiPlayer = "O"

def print_board(board: list):
    for i in range(3):
        row = "|".join(str(board[i][j]) for j in range(3))
        print(row)
        if i==2 :
            print(end="")
        else:
            print("-+-+-")

def cell_is_empty(board: list, position):
    i = (position - 1) // 3
    j = (position - 1) % 3
    return board[i][j] == " "

def player_move(board: list, player: str, position: int):
    i = (position - 1) // 3
    j = (position - 1) % 3
    board[i][j] = player
    return board

def cheak_win(board: list, player: str):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[x][x] == player for x in range(3)):
        return True
    if all(board[x][2 - x] == player for x in range(3)):
        return True

    return False

def evaluate (board : list):
    if cheak_win(board,HumPlayer):
        return -1

    if cheak_win(board,AiPlayer):
        return 1

    return 0

def is_board_full(board:list) :
    for i in range(3):
        if " " in board[i] :
            return False
    return True


def miniMaxAlgo( board:list ,depth:int , maximizing_AI_Player:bool ):
    if depth ==0 or cheak_win(board,AiPlayer) or  cheak_win(board,HumPlayer) or is_board_full(board):
        return evaluate(board)

    if maximizing_AI_Player :
        max_val = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " " :
                    board[i][j] = AiPlayer
                    new_val = miniMaxAlgo(board, depth-1 , False)
                    board[i][j] = " "
                    max_val = max(max_val,new_val)
        return max_val

    else :
        min_val = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " " :
                    board[i][j] = HumPlayer
                    new_val = miniMaxAlgo(board, depth-1 , True)
                    board[i][j] = " "
                    min_val = min(min_val,new_val)
        return min_val


def miniMaxAlgo_By_Alpha_Beta( board:list ,depth:int ,alpha:int ,beta:int ,maximizing_AI_Player:bool ):
    if depth ==0 or cheak_win(board,AiPlayer) or  cheak_win(board,HumPlayer) or is_board_full(board):
        return evaluate(board)

    if maximizing_AI_Player :
        max_val = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " " :
                    board[i][j] = AiPlayer
                    new_val = miniMaxAlgo_By_Alpha_Beta(board, depth-1 ,alpha,beta, False)
                    board[i][j] = " "
                    max_val = max(max_val,new_val)
                    alpha = max(alpha,new_val)
                    if beta <= alpha :
                        break
        return max_val

    else :
        min_val = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " " :
                    board[i][j] = HumPlayer
                    new_val = miniMaxAlgo_By_Alpha_Beta(board, depth-1 ,alpha,beta, True)
                    board[i][j] = " "
                    min_val = min(min_val,new_val)
                    beta = min(beta, new_val)
                    if beta <= alpha:
                        break
        return min_val


def best_move(board:list):
    best_score = -float("inf")
    move = (-1,-1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = AiPlayer
                ###### Selects the algorithm to be used for move evaluation (Minimax or Alpha-Beta Pruning).  ######
                #score = miniMaxAlgo(board,9,False)
                score = miniMaxAlgo_By_Alpha_Beta(board,9,-float("inf"),float("inf"),False)

                board[i][j] = " "
                if score > best_score :
                    best_score = score
                    move= 3*i+j+1

    return move



# === Tkinter GUI Logic ===
class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.config(background='#d5d6f4')
        self.icon=PhotoImage(file='tic-tac-toe.png')
        self.root.iconphoto(True,self.icon)
        self.label=tk.Label(self.root,text="Tic Tac Toe",font=('Arial',30),bg='#d5d6f4',fg='#1F213D')
        self.label.pack()
        self.turn_label = tk.Label(self.root, text="Your Turn...", font=('Arial', 18), bg='#d5d6f4', fg='#3402D2'if HumPlayer=='X'else '#9B3FFF')
        self.turn_label.pack()
        self.frame=tk.Frame(self.root)
        self.frame.pack()
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        for row in range(3):
            for col in range(3):
                btn = tk.Button(self.frame, text="", font=('Arial', 36), width=5, height=2,bg='#d5d6f4',fg='#1F213D',
                                command=lambda r=row, c=col: self.user_click(r, c))
                btn.grid(row=row, column=col)
                self.buttons[row][col] = btn

        self.reset_btn = tk.Button(self.frame, text="Restart", font=('Arial', 16), command=self.reset_game,fg='#1F213D',bg='#BABBD4')
        self.reset_btn.grid(row=3, column=0, columnspan=3, sticky="nsew")

    def user_click(self, row, col):
        position = row * 3 + col + 1
        if cell_is_empty(self.board, position):
            player_move(self.board, HumPlayer, position)
            self.buttons[row][col].config(text=HumPlayer,fg='#3402D2'if HumPlayer=='X'else '#9B3FFF')
            self.turn_label.config(text="AI's Turn...",fg='#9B3FFF'if AiPlayer=='O'else '#3402D2')
            if cheak_win(self.board, HumPlayer):
                self.end_game("You win!")
                return
            if is_board_full(self.board):
                self.end_game("It's a draw!")
                return
            self.root.after(500, self.ai_turn)

    def ai_turn(self):
        ai_pos = best_move(self.board)
        if ai_pos is not None:
            player_move(self.board, AiPlayer, ai_pos)
            row = (ai_pos - 1) // 3
            col = (ai_pos - 1) % 3
            self.buttons[row][col].config(text=AiPlayer,fg='#9B3FFF'if AiPlayer=='O'else'#3402D2')
            if cheak_win(self.board, AiPlayer):
                self.end_game("AI wins!")
            elif is_board_full(self.board):
                self.end_game("It's a draw!")
            else:
                self.turn_label.config(text="Your Turn...",fg='#3402D2'if HumPlayer=='X'else '#9B3FFF')

    def end_game(self, message):
        messagebox.showinfo("Game Over", message)
        self.disable_buttons()
        self.turn_label.config(text="Game Over",fg='#1F213D')

    def disable_buttons(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(state='disabled')

    def reset_game(self):
        self.root.destroy()
        restart = tk.Tk()
        start_win = start_window(restart)
        restart.mainloop()

class start_window:
    def __init__(self,start):
        self.start=start
        self.start.title("Tic Tac Toe")
        self.start.geometry('400x500')
        self.start.config(background='#d5d6f4')
        self.starticon = PhotoImage(file='tic-tac-toe.png')
        self.start.iconphoto(True, self.starticon)
        self.startlabel=tk.Label(self.start,text="Select Player",font=('Arial',30),bg='#d5d6f4',fg='#1F213D')
        self.startlabel.pack(pady=40)
        self.radioframe=tk.Frame(self.start)
        self.radioframe.pack()
        self.choice=tk.StringVar(value='X')
        self.x_radiobutton=tk.Radiobutton(self.radioframe,text='X',variable=self.choice,
                                          value='X',indicatoron=0,font=('Arial', 36),
                                          width=5, height=2,bg='#d5d6f4',fg='#3402D2')
        self.x_radiobutton.pack(side='left')
        self.o_radiobutton = tk.Radiobutton(self.radioframe, text='O', variable=self.choice,
                                            value='O', indicatoron=0,font=('Arial', 36),
                                            width=5, height=2,bg='#d5d6f4',fg='#9B3FFF')
        self.o_radiobutton.pack(side='left')
        self.startbutton=tk.Button(self.start,text='Start Game',font=('Arial', 16),
                                   fg='#1F213D',bg='#BABBD4',command=self.startgame)
        self.startbutton.pack(pady=40)
    def startgame(self):
        global HumPlayer,AiPlayer
        HumPlayer=self.choice.get()
        AiPlayer='O' if HumPlayer=='X' else 'X'
        self.start.destroy()
        root = tk.Tk()
        game = TicTacToeGUI(root)
        root.mainloop()



# === Run the Game ===
start_root=tk.Tk()
start=start_window(start_root)
start_root.mainloop()