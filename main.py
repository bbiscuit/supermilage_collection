import time
from src.display import Display
from src.sensor import Sensor

# Create a basic display
display = Display()
display.print_text("Starting script")

# Get sensor from resistor
sensor = Sensor(26)

for i in range(0, 100000):
    print(sensor.get_val())
    display.print_text(str(sensor.get_val()))
    time.sleep(.2)