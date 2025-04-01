import time
import random
from gpiozero import LEDBoard, Button

# Define GPIO pins
LEDnumber = LEDBoard(23, 4, 25, 10, 17, 8, 22, pwm=False)  # Adjust pin numbers if needed
pushButton = Button(7)  # Adjust pin number if needed

def main():
    try:
        while True:
            number = generateNumber()
            displayNumber(number)
    except KeyboardInterrupt:
        print("\nExiting program.")

def generateNumber():  # Wait for a push, return random die value
    throw = random.randint(1, 6)
    print("Press the button to roll the dice.")
    
    pushButton.wait_for_press()  # Wait for button press
    time.sleep(0.030)  # Debounce delay
    
    while pushButton.is_pressed:
        throw += 1
        if throw > 6:  # Wrap round the number
            throw = 1
    
    print(f"Dice rolled: {throw}")
    return throw

def displayNumber(number):
    # Light up LEDs corresponding to the dice number
    for i, led in enumerate(LEDnumber):
        if i < number:
            led.on()
        else:
            led.off()
            
    time.sleep(1)  # Keep the LEDs on for 1 second
    LEDnumber.off()  # Turn off all LEDs

if __name__ == "__main__":
    main()
