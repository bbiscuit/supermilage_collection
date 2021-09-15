#include <stdio.h>
#include <pico/stdlib.h>

int main()
{

  //The pin number
  const uint led_pin = 28;

  //Initialize LED pin
  gpio_init(led_pin);

  //Set the direction of the data
  gpio_set_dir(led_pin, GPIO_OUT);

  //Initialize chosen serial port
  stdio_init_all();

  //Loop forever
  while (true)
  {

    //Blink LED
    gpio_put(led_pin, true); //Put true for on
    sleep_ms(1000);
    gpio_put(led_pin, false); //Put false for off
    sleep_ms(1000);
  }
}