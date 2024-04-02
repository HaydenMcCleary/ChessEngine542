import tkinter as tk
from from_root import from_here
import chess
from boardtracker import islegal

# Link image directory
image_dir = from_here("images")

# Create a Tkinter window
root = tk.Tk()
root.title("Chess Game")

# Create a Canvas widget to draw the chessboard
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

     board = chess.Board()
     moves = []

# Draw the chessboard squares
for i in range(8):
    for j in range(8):
        color = "white" if (i + j) % 2 == 0 else "pink"
        canvas.create_rectangle(j * 50, i * 50, (j + 1) * 50, (i + 1) * 50, fill=color)

# Load piece images
piece_images = {
    "white pawn": tk.PhotoImage(file=str(image_dir / "wp.png")),
    "white rook": tk.PhotoImage(file=str(image_dir / "wR.png")),
    "white knight": tk.PhotoImage(file=str(image_dir / "wN.png")),
    "white bishop": tk.PhotoImage(file=str(image_dir / "wB.png")),
    "white king": tk.PhotoImage(file=str(image_dir / "wK.png")),
    "white queen": tk.PhotoImage(file=str(image_dir / "wQ.png")),

    "black pawn": tk.PhotoImage(file=str(image_dir / "bp.png")),
    "black rook": tk.PhotoImage(file=str(image_dir / "bR.png")),
    "black knight": tk.PhotoImage(file=str(image_dir / "bN.png")),
    "black bishop": tk.PhotoImage(file=str(image_dir / "bB.png")),
    "black king": tk.PhotoImage(file=str(image_dir / "bK.png")),
    "black queen": tk.PhotoImage(file=str(image_dir / "bQ.png")),
}


def place_piece(column, row, piece):
    piece_id = canvas.create_image(column * 50 + 25, row * 50 + 25, image=piece_images[piece])
    if piece.startswith('white'):
        canvas.itemconfig(piece_id, tags=('white',)) 
    elif piece.startswith('black'):
        canvas.itemconfig(piece_id, tags=('black',))  # Assigning the 'black' tag to black pieces


place_piece(0, 7, "white rook")
place_piece(1, 7, "white knight")
place_piece(2, 7, "white bishop")
place_piece(3, 7, "white queen")
place_piece(4, 7, "white king")
place_piece(5, 7, "white bishop")
place_piece(6, 7, "white knight")
place_piece(7, 7, "white rook")
for i in range(8):
    place_piece(i, 6, "white pawn")

# Place remaining black pieces on the board
place_piece(0, 0, "black rook")
place_piece(1, 0, "black knight")
place_piece(2, 0, "black bishop")
place_piece(3, 0, "black queen")
place_piece(4, 0, "black king")
place_piece(5, 0, "black bishop")
place_piece(6, 0, "black knight")
place_piece(7, 0, "black rook")
for i in range(8):
    place_piece(i, 1, "black pawn")


# Functions for piece movement
selected_piece = None
offset_x = 0
offset_y = 0

def number_to_column(num):
    return chr(ord('a') + num - 1)


def select_piece(event):
    global selected_piece, offset_x, offset_y, past_column, past_row  # Add past_column and past_row to global
    item = canvas.find_closest(event.x, event.y)
    if item:
        selected_piece = item[0]
        x0, y0 = canvas.coords(selected_piece)[:2]
        offset_x = event.x - x0
        offset_y = event.y - y0
        past_row = int(y0 / 50)
        past_column = int(x0 / 50)

def move_piece(event):
    global selected_piece
    if selected_piece:
        canvas.coords(selected_piece, event.x - offset_x, event.y - offset_y)

def release_piece(event):
    global selected_piece
    global past_column 
    global past_row

    if selected_piece:
        x = event.x - offset_x
        y = event.y - offset_y
        
        column = int(x / 50)
        row = int(y / 50)

        past_column_letter = number_to_column(past_column)
        column_letter = number_to_column(column)

        move = past_column_letter.lower() + str(8 - past_row) + column_letter.lower() + str(8 - row)
        user_move = chess.Move.from_uci(move)

        if(islegal(user_move, board)):


            board.push(move)
            moves.append(move)


            destination_x = column * 50 + 25
            destination_y = row * 50 + 25
            
            overlapping_pieces = canvas.find_overlapping(destination_x , destination_y , destination_x, destination_y )
            
            for item in overlapping_pieces:
                tags = canvas.gettags(item)
                if ('black' in tags or 'white' in tags) and item != selected_piece:                # Capture the piece or perform any other action
                    canvas.delete(item)
            
            canvas.coords(selected_piece, destination_x, destination_y)
            selected_piece = None
            past_row = int(0)     # Store the past row
            past_column = int(0)  # Store the past column

        else:
            
            destination_x = past_column * 50 + 25
            destination_y = past_row * 50 + 25
            canvas.coords(selected_piece, destination_x, destination_y)
            selected_piece = None
            past_row = int(0)     # Store the past row
            past_column = int(0)  # Store the past column
        

# Bind mouse events
canvas.bind("<Button-1>", select_piece)
canvas.bind("<B1-Motion>", move_piece)
canvas.bind("<ButtonRelease-1>", release_piece)
# Start the Tkinter event loop
root.mainloop()

