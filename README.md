# 🎮 Tic-Tac-Toe with GUI and AI  

A classic Tic-Tac-Toe game for the desktop, featuring an unbeatable AI opponent. This project showcases the implementation of the Minimax algorithm with Alpha-Beta Pruning to create an intelligent and challenging opponent, all within a simple graphical user interface built with Python's Tkinter library.  

---

## 🚀 Features  
- Unbeatable AI: The AI opponent uses the Minimax algorithm to predict all possible moves and always choose the optimal one, ensuring it never loses.  
- Graphical User Interface (GUI): An intuitive and user-friendly interface powered by Tkinter.  
- Player Selection: Choose to play as either 'X' or 'O'.  
- Restart Game: Easily restart the game at any point to play again.  

---

## 📦 Prerequisites  
To run this game, you need:  
- Python 3.x  
- The Tkinter library, which is typically included with standard Python installations.  

---

## ▶️ How to Run  
- Save the code from game_with_gui.py to a file on your computer.  
- Open your command line or terminal.  
- Navigate to the directory where you saved the file.  
- Run the game using the following command:  

```bash
python game_with_gui.py

---

# 🧠 Algorithm  

The AI's logic is based on the Minimax Algorithm, a recursive search algorithm used in decision-making and game theory. The AI evaluates every possible move on the board and assigns a score to each one:  

- A winning move for the AI gets a high score.  
- A winning move for the human player gets a low score (negative).  
- A draw gets a neutral score.  

The AI then chooses the move that maximizes its score, assuming the human player will always play optimally to minimize it. To optimize this process and reduce the number of calculations, Alpha-Beta Pruning is used to ignore branches of the game tree that will not affect the final decision.  
