import pyautogui
import time
import random
import string

def move_and_click(target_coords,move_duration =0.5):
    pyautogui.moveTo(target_coords, duration=move_duration)
    time.sleep(0.2)
    pyautogui.click()

def type_random_coupon_code(length=8):
    # Generate a random alphanumeric code of the specified length
    coupon_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

    # Type the coupon code
    pyautogui.write(coupon_code)

    # Optionally, print the coupon code for reference
    print(f"Coupon code typed: {coupon_code}")


def type_custom_coupon_code(code, discount_amount,isFreecouponTrue):
    # Format the discount amount
    if isFreecouponTrue == 0:
        discount_str = f"_{discount_amount}"
    else:
        discount_str = "FREE"

    # Concatenate the parts to form the coupon code
    coupon_code = f"{code}{discount_str}"

    # Type the coupon code
    pyautogui.write(coupon_code)

    # Optionally, print the coupon code for reference
    print(f"Coupon code typed: {coupon_code}")


def main():
    type_random_coupon_code()

if __name__ == "__main__":
    main()
