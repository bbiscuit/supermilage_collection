#include <stdio.h>
#include <pico/stdlib.h>

int main()
{
  //The pin number
  const uint buttonPin = 15;
  const uint ledPin = 25;

  //Initialize LED pin
  gpio_init(buttonPin);
  gpio_init(ledPin);

  //Set the direction of the data
  gpio_set_dir(buttonPin, GPIO_IN);
  gpio_set_dir(ledPin, GPIO_OUT);

  //Initialize chosen serial port
  stdio_init_all();

  //Loop forever
  while (true)
  {
    //Blink LED
    gpio_put(ledPin, !gpio_get(buttonPin));
  }
}