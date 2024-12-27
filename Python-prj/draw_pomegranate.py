from tkinter import Tk, Canvas

# Initialize the main application window
root = Tk()
root.title("Draw a Pomegranate")

# Set up the Canvas
canvas_width = 400
canvas_height = 400
canvas = Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Draw the pomegranate body (circle)
pomegranate_body = canvas.create_oval(150, 150, 250, 250, fill="red", outline="black", width=2)

# Draw the crown (top of the pomegranate)
crown_points = [180, 150, 200, 120, 220, 150]  # Coordinates for the triangular crown
canvas.create_polygon(crown_points, fill="red", outline="black", width=2)

# Draw seeds (small circles inside the body)
seeds = [
    (170, 170), (190, 170), (210, 170),
    (180, 190), (200, 190),
    (190, 210)
]
for x, y in seeds:
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="white", outline="black")

# Run the application
root.mainloop()
