from src.display import Display

# Create a basic display
display = Display()

for i in range(0, 100000):
    display.print_text("Line #" + str(i))
    print(str(i))
