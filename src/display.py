# Display Image & text on I2C driven ssd1306 OLED display
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import utime

# The size of the screen
WIDTH = 128
HEIGHT = 64

# The maximum amount of lines on the screen
LINES = 6

# The spacing between lines
SPACING = 10

# This class is a wrapper for the oled allowing us to print lines of text to the display as well as helper functions
class Display:

    # Class constructor
    def __init__(self):
        
        # Init I2C using pins GP0 & GP1 as well as init oled
        self.i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=200000)
        self.oled = SSD1306_I2C(WIDTH, HEIGHT, self.i2c)
        
        # Display basic information on start
        self.oled.show_info()
        utime.sleep(1)
        self.clear()
    
    # Clear the screen
    def clear_screen(self):
        self.oled.fill(0)
        self.oled.show()
    
    # Clear the screen and clear all lines
    def clear(self):
        self.clear_screen()
        self.lines = []

    # Print a line of text to the screen
    def print_text(self, text):
        self.oled.fill(0)
        
        # Make sure theres only LINES number of lines
        self.lines.append(text)
        if len(self.lines) > LINES:
            self.lines.pop(0)
        
        # Print all lines
        current_y = 0
        for line in self.lines:
            self.oled.text(line, 0, current_y)
            current_y += SPACING
        
        self.oled.show()
        