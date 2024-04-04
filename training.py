from pynput.mouse import Listener
import json

def activate_safari(prompt):
    print(prompt)

    coords = {'x': None, 'y': None}

    # Define the event listener callback function
    def on_click(x, y, button, pressed):
        if button == button.left and pressed:
            coords['x'] = x
            coords['y'] = y
            # Stop listener
            return False

    # Start the listener
    with Listener(on_click=on_click) as listener:
        listener.join()

    return

def capture_coordinate(prompt):
    print(prompt)
    print("Click at the desired position.")

    coords = {'x': None, 'y': None}

    # Define the event listener callback function
    def on_click(x, y, button, pressed):
        if button == button.left and pressed:
            coords['x'] = x
            coords['y'] = y
            # Stop listener
            return False

    # Start the listener
    with Listener(on_click=on_click) as listener:
        listener.join()

    return [coords['x'], coords['y']]



def main():
    activate_safari("Click on Safari to get started")
    coordinates = {
        "CouponDetail": {
            "CouponCode": capture_coordinate("Step 1: Capture the 'Coupon Code' coordinate."),
        },
        "DiscountType": {
            "AmountOffToggle": capture_coordinate("Step 2: Capture the 'Amount Off Toggle' coordinate."),
            "CurrencyType": capture_coordinate("Step 3: Capture the 'Currency Type' coordinate."),
            "USD": capture_coordinate("Step 4: Capture the 'USD' coordinate."),
            "InputAmount": capture_coordinate("Step 5: Capture the 'Input Amount' coordinate."),
        },
        "Duration": {
            "Forever": capture_coordinate("Step 6: Capture the 'Forever' coordinate."),
        },
        "Continue": {
            "Enter": capture_coordinate("Step 7: Capture the 'Enter' coordinate."),
        },
        "Offer": {
            "AddOffer": capture_coordinate("Step 8: Capture the 'AddOffer' coordinate."),
            "SelectOffer": capture_coordinate("Step 9: Capture the 'SelectOffer' coordinate."),
            "ConfirmSelectOffer": capture_coordinate("Step 10: Capture the 'ConfirmSelectOffer' coordinate."),
            "DiscountLink": capture_coordinate("Step 11: Capture the 'Discount Link' coordinate."),
        }
    }

    json_filename = 'coordinates.json'
    with open(json_filename, 'w') as file:
        json.dump(coordinates, file, indent=4)
    print(f"All coordinates have been captured and saved to '{json_filename}'.")


if __name__ == "__main__":
    main()