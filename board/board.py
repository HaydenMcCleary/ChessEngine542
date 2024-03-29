import tkinter as tk
from from_root import from_here

# Link image directory
image_dir = from_here("images")

# Create a Tkinter window
root = tk.Tk()
root.title("Chess Game")

# Create a Canvas widget to draw the chessboard
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Draw the chessboard squares
for i in range(8):
    for j in range(8):
        color = "white" if (i + j) % 2 == 0 else "gray"
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

# Place pieces on the board
# Example: canvas.create_image(x_position, y_position, image=piece_images["pawn"])

for column in range(8):
    canvas.create_image(column * 50 + 25, 6 * 50 + 25, image=piece_images["white pawn"])
canvas.create_image(0 * 50 + 25, 7 * 50 + 25, image=piece_images["white rook"])
canvas.create_image(7 * 50 + 25, 7 * 50 + 25, image=piece_images["white rook"])
canvas.create_image(1 * 50 + 25, 7 * 50 + 25, image=piece_images["white knight"])
canvas.create_image(6 * 50 + 25, 7 * 50 + 25, image=piece_images["white knight"])
canvas.create_image(2 * 50 + 25, 7 * 50 + 25, image=piece_images["white bishop"])
canvas.create_image(5 * 50 + 25, 7 * 50 + 25, image=piece_images["white bishop"])
canvas.create_image(3 * 50 + 25, 7 * 50 + 25, image=piece_images["white queen"])
canvas.create_image(4 * 50 + 25, 7 * 50 + 25, image=piece_images["white king"])

#to do fill in the rest of this


for column in range(8):
    canvas.create_image(column * 50 + 25, 1 * 50 + 25, image=piece_images["black pawn"])
canvas.create_image(0 * 50 + 25, 0 * 50 + 25, image=piece_images["black rook"])
canvas.create_image(7 * 50 + 25, 0 * 50 + 25, image=piece_images["black rook"])
canvas.create_image(1 * 50 + 25, 0 * 50 + 25, image=piece_images["black knight"])
canvas.create_image(6 * 50 + 25, 0 * 50 + 25, image=piece_images["black knight"])
canvas.create_image(2 * 50 + 25, 0 * 50 + 25, image=piece_images["black bishop"])
canvas.create_image(5 * 50 + 25, 0 * 50 + 25, image=piece_images["black bishop"])
canvas.create_image(3 * 50 + 25, 0 * 50 + 25, image=piece_images["black queen"])
canvas.create_image(4 * 50 + 25, 0 * 50 + 25, image=piece_images["black king"])





# Functions for piece movement
selected_piece = None
offset_x = 0
offset_y = 0

def select_piece(event):
    global selected_piece, offset_x, offset_y
    item = canvas.find_closest(event.x, event.y)
    piece_tags = canvas.gettags(item)  # Get tags associated with the clicked item
    if 'white' in piece_tags:  # Check if the clicked piece is white
        selected_piece = item[0]
        x0, y0, _, _ = canvas.coords(selected_piece)
        offset_x = event.x - x0
        offset_y = event.y - y0


def move_piece(event):
    global selected_piece
    if selected_piece:
        canvas.coords(selected_piece, event.x - offset_x, event.y - offset_y)

def release_piece(event):
    global selected_piece
    if selected_piece:
        x = event.x - offset_x
        y = event.y - offset_y
        column = int(x / 50)
        row = int(y / 50)
        canvas.coords(selected_piece, column * 50 + 25, row * 50 + 25)
        selected_piece = None

# Bind mouse events
canvas.bind("<Button-1>", select_piece)
canvas.bind("<B1-Motion>", move_piece)
canvas.bind("<ButtonRelease-1>", release_piece)
# Start the Tkinter event loop
root.mainloop()

images/wR.png