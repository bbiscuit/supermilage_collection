from src.display import Display

# Create a basic display
display = Display()

for i in range(0, 15):
    display.print_text("Line #" + str(i))
