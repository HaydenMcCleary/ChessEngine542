import chess
import tkinter as tk
from tkinter import messagebox

def is_legal(moved_char_not, board):
    try:
        move = chess.Move.from_uci(moved_char_not)
    except ValueError:
        return False
    return move in board.legal_moves

def play_game():
    board = chess.Board()
    moves = []

    def on_submit():
        user_move = entry.get()
        if is_legal(user_move, board):
            move = chess.Move.from_uci(user_move)
            board.push(move)
            moves.append(move)
            update_board()
            if board.is_game_over():
                end_game()

    def update_board():
        canvas.delete("all")
        piece_symbols = {'p': '♟', 'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚',
                         'P': '♙', 'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔'}
        for square in chess.SQUARES:
            row = square // 8
            col = square % 8
            color = "white" if (row + col) % 2 == 0 else "gray"
            canvas.create_rectangle(col*50, (7-row)*50, (col+1)*50, (8-row)*50, fill=color)
            piece = board.piece_at(square)
            if piece is not None:
                canvas.create_text((col*50 + 25, (7-row)*50 + 25), text=piece_symbols[piece.symbol()], font=("Helvetica", 30))

    
    def end_game():
        messagebox.showinfo("Game Over", f"Result: {board.result()}\nMoves Played: {', '.join(str(move) for move in moves)}")
        window.destroy()

    window = tk.Tk()
    window.title("Chess Game")

    canvas = tk.Canvas(window, width=400, height=400)
    canvas.pack()

    entry = tk.Entry(window)
    entry.pack()

    submit_button = tk.Button(window, text="Submit Move", command=on_submit)
    submit_button.pack()

    update_board()

    window.mainloop()

play_game()
