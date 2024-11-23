import tkinter as tk

# Screen settings
WIDTH, HEIGHT = 800, 600

# Colors
MINTGREEN = "#94C9B3"
TEALBLUE = "#2A485C"

# Text content
title_text = "Fertility Awareness"
subtitle_text = "Developed by WOWEN"
description_text = [
    "The Fertility Awareness App is a digital assistant designed",
    "to democratize access to fertility understanding and women's health.",
    "Our aim is to provide reliable, quick, and easily accessible information",
    "to power women in taking control of their reproductive health.",
]
link_text = "Contact: www.wowen.tech"

# Animation settings
ANIMATION_SPEED = 20  # milliseconds between updates
TEXT_SPEED = 50       # speed of typewriter effect (ms per character)

def animate_title():
    """Animate the title by moving it up and down."""
    global title_direction, title_y
    title_y += title_direction
    if title_y <= 90 or title_y >= 110:
        title_direction *= -1
    canvas.coords(title, WIDTH // 2, title_y)
    root.after(ANIMATION_SPEED, animate_title)

def typewriter_effect(text, x, y, font, fill, line_index=0, char_index=0, objects=None):
    """Display text with a typewriter effect."""
    if objects is None:
        objects = []  # Store references to text objects

    if line_index < len(text):
        # Get the current line and slice up to the current character
        line = text[line_index]
        displayed_text = line[:char_index + 1]

        # If the text object for this line doesn't exist, create it
        if len(objects) <= line_index:
            obj = canvas.create_text(x, y + (line_index * 30), text=displayed_text, font=font, fill=fill, anchor="center")
            objects.append(obj)
        else:
            # Update the existing text object
            canvas.itemconfig(objects[line_index], text=displayed_text)

        # Continue typing the current line
        if char_index < len(line) - 1:
            root.after(TEXT_SPEED, typewriter_effect, text, x, y, font, fill, line_index, char_index + 1, objects)
        else:
            # Move to the next line
            root.after(TEXT_SPEED, typewriter_effect, text, x, y, font, fill, line_index + 1, 0, objects)

# Create the main window
root = tk.Tk()
root.title("WOWEN - Weaving the Web")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.configure(bg=MINTGREEN)

# Create a canvas to draw text
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=MINTGREEN, highlightthickness=0)
canvas.pack()

# Add the title
title_y = 100
title_direction = 1
title = canvas.create_text(WIDTH // 2, title_y, text=title_text, font=("Arial", 36, "bold"), fill=TEALBLUE)

# Add the subtitle
subtitle = canvas.create_text(
    WIDTH // 2, 150, text=subtitle_text, font=("Arial", 24, "italic"), fill=TEALBLUE
)

# Add the description text with typewriter effect
typewriter_effect(description_text, WIDTH // 2, 200, ("Arial", 14), TEALBLUE)

# Add the link
canvas.create_text(
    WIDTH // 2, HEIGHT - 50, text=link_text, font=("Arial", 16), fill=TEALBLUE
)

# Start the title animation
animate_title()

# Run the main loop
root.mainloop()
