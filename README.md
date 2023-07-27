# Gamepad Data Reader using Pygame

This Python script allows you to read and display data from a gamepad connected to your computer using the Pygame library. The script will show real-time button presses and axis movements of the gamepad.

## Requirements

- Python 3.x
- Pygame library

## Installation

1. Install Python 3.x from the official website: https://www.python.org/downloads/
2. Install the Pygame library using pip:


## Usage

1. Connect your gamepad to the computer via USB or Bluetooth.
2. Run the `main.py` script using Python:

3. The script will detect the connected gamepad and display its data in the terminal.
4. Use the gamepad buttons and axis movements to see the real-time updates in the terminal.
5. Press `Ctrl+C` to exit the script.

## Script Explanation

- The script uses the Pygame library to handle gamepad input.
- It initializes Pygame and gamepad detection at the beginning.
- The script checks the number of connected gamepads and ensures at least one gamepad is available.
- The first gamepad is chosen for demonstration purposes (you can change the index for more gamepads).
- The main loop continuously reads events from the gamepad using `pygame.event.get()`.
- The script prints the event type and relevant data when buttons are pressed, released, or when the axis value changes.

## Gamepad Data Display

- Button Events: When a button on the gamepad is pressed, the script will display a message indicating which button was pressed.
- Button Releases: When a button on the gamepad is released, the script will display a message indicating which button was released.
- Axis Movements: When the axis (analog stick) on the gamepad is moved, the script will display the axis number and its current value.

## Troubleshooting

- If the script cannot detect your gamepad, ensure that it is connected correctly (USB or Bluetooth).
- Verify that the Pygame library is installed correctly and is compatible with your Python version.
