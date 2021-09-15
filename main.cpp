#include <stdio.h>
#include <pico/stdlib.h>

int main()
{
  //The delay between flashes (in milliseconds)
  int delay = 500;

  //The pin number
  const uint external_led_pin = 28;
  const uint internal_led_pin = 25;

  //Initialize LED pin
  gpio_init(external_led_pin);
  gpio_init(internal_led_pin);

  //Set the direction of the data
  gpio_set_dir(external_led_pin, GPIO_OUT);
  gpio_set_dir(internal_led_pin, GPIO_OUT);
  
  //Initialize chosen serial port
  stdio_init_all();

  //Loop forever
  while (true)
  {
    //Blink LED
    gpio_put(external_led_pin, true); //Put true for on
    gpio_put(internal_led_pin, false);
    sleep_ms(delay);
    gpio_put(external_led_pin, false); //Put false for off
    gpio_put(internal_led_pin, true);
    sleep_ms(delay);
  }
}