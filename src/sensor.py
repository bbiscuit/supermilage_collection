from machine import ADC, Pin

# This class gets voltage from a pin on the pico
class Sensor:    
        
    # Set the pin that we're sensing from
    def __init__(self, pin):
        self.adc = ADC(Pin(26))
        
    # Read the voltage from the pin
    def get_val(self) -> int:
        return self.adc.read_u16()