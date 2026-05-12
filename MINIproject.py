import tkinter as tk
import random

# Initialize the tkinter window
window = tk.Tk()
window.title("Ludo Game")

# Set canvas dimensions
canvas_width = 400
canvas_height = 400

# Create canvas to display the Ludo board
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height)
canvas.pack()

# Function to draw the Ludo board
def draw_board():
    # Draw outer square
    canvas.create_rectangle(50, 50, canvas_width - 50, canvas_height - 50)
    
    # Draw home positions
    canvas.create_rectangle(50, 50, 150, 150, fill="red")
    canvas.create_rectangle(canvas_width - 150, 50, canvas_width - 50, 150, fill="green")
    canvas.create_rectangle(50, canvas_height - 150, 150, canvas_height - 50, fill="blue")
    canvas.create_rectangle(canvas_width - 150, canvas_height - 150, canvas_width - 50, canvas_height - 50, fill="yellow")
    
    # Draw center square
    canvas.create_rectangle(150, 150, canvas_width - 150, canvas_height - 150)
    
    # Draw lines for positions
    for i in range(6):
        # Draw vertical lines
        x = 100 + i * 50
        canvas.create_line(x, 50, x, 150)
        canvas.create_line(x, canvas_height - 150, x, canvas_height - 50)
        
        # Draw horizontal lines
        y = 100 + i * 50
        canvas.create_line(50, y, 150, y)
        canvas.create_line(canvas_width - 150, y, canvas_width - 50, y)

# Function to move the pawn
def move_pawn(steps):
    # Get the current coordinates of the pawn
    x1, y1, x2, y2 = canvas.coords(red_pawn)
    
    # Calculate the distance to move based on steps
    distance = 50 * steps

    # Calculate the number of steps needed to reach the center square
    steps_to_center = 12 - (y1 - 150) // 50

    # If the pawn is already in the center square, move it forward
    if steps_to_center == 0:
        canvas.move(red_pawn, 0, -distance)
    # If the number of steps is less than or equal to steps needed to reach the center square, move it forward
    elif steps <= steps_to_center:
        canvas.move(red_pawn, 0, -distance)
    # If the number of steps is greater than the steps needed to reach the center square, move it to the center square first
    else:
        canvas.move(red_pawn, 0, -steps_to_center * 50)
        canvas.move(red_pawn, -((steps - steps_to_center) * 50), 0)

# Function to animate the rolling dice and move the pawn
def animate_dice():
    dice_number = random.randint(1, 6)
    print("Dice Number:", dice_number)

    # Create dice animation
    for _ in range(10):
        dice_number = random.randint(1, 6)
        canvas.delete("dice")
        canvas.create_text(canvas_width // 2, canvas_height // 2, text=dice_number, font=("Arial", 50), tags="dice")
        canvas.update()
        canvas.after(100)

    # Move the pawn according to the dice roll number
    move_pawn(dice_number)

# Create a dice button
dice_button = tk.Button(window, text="Roll Dice", command=animate_dice)
dice_button.pack()

# Create red pawn
pawn_size = 30
pawn_x = (canvas_width - pawn_size) // 2
pawn_y = canvas_height - 50 - pawn_size
red_pawn = canvas.create_oval(pawn_x, pawn_y, pawn_x + pawn_size, pawn_y + pawn_size, fill="red")

# Draw the Ludo board
draw_board()

# Start the tkinter event loop
window.mainloop()