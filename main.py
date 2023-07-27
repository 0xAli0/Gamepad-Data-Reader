import pygame

def main():
    # Initialize Pygame
    pygame.init()

    # Initialize the gamepads
    pygame.joystick.init()

    # Get the number of connected gamepads
    joystick_count = pygame.joystick.get_count()

    if joystick_count == 0:
        print("No connected gamepad found.")
        return

    # Get the first gamepad (You can change the index for more gamepads)
    gamepad = pygame.joystick.Joystick(0)
    gamepad.init()

    print("Use the gamepad to read its data.")
    print("Press 'Ctrl+C' to exit.\n")

    try:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN:
                    print(f"Button {event.button} pressed.")
                elif event.type == pygame.JOYBUTTONUP:
                    print(f"Button {event.button} released.")
                elif event.type == pygame.JOYAXISMOTION:
                    print(f"Axis {event.axis} value: {event.value}")

    except KeyboardInterrupt:
        print("\nProgram terminated.")

if __name__ == "__main__":
    main()
