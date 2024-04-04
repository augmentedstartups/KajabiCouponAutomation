from pynput.mouse import Listener
import pyautogui

def on_click(x, y, button, pressed):
    if pressed:
        # Get the current mouse position
        x, y = pyautogui.position()
        print(f"Mouse clicked at ({x}, {y}) with {button}")

# Set up the listener for mouse clicks
with Listener(on_click=on_click) as listener:
    listener.join()