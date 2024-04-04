import webbrowser
import time
import pyautogui
import control
from interpreter import interpreter
from Backup import sqlcreate
import json

main_offer = 299
movement_duration=0.15   #mouse movement

# Read coordinates from JSON file
with open('coordinates.json', 'r') as file:
    coords = json.load(file)


def open_url_in_safari(url):
    browser_name = 'safari'
    try:
        # Check if Safari is available on the system
        browser = webbrowser.get(browser_name)
        browser.open_new(url)
        print(f"Opened {url} in Safari.")
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'alt', 'enter')
        print('Open Safari Link Done')
        time.sleep(4)

    except webbrowser.Error:
        print(f"Failed to open {url} in Safari. Safari browser not available on this system.")


def start_automation(discount_amount,forever_check,category_to_lookup,isFreecouponTrue):
    ##Open= Safari=========================
    open_url_in_safari("https://app.kajabi.com/admin/sites/104576/coupons/new")

    # =Coupon Detail==========================
    code = sqlcreate.get_code_for_category(category_to_lookup)
    pyautogui.press('tab')
    #control.type_random_coupon_code(category)
    control.type_custom_coupon_code(code, discount_amount,isFreecouponTrue)

    # # =Discount Type==========================
    if isFreecouponTrue == 0:
        # control.move_and_click(coords['DiscountType']['AmountOffToggle'], movement_duration)
        interpreter.computer.mouse.click("Amount Off")
        pyautogui.press('tab')# Now at Amount off
        amount_off = main_offer - discount_amount
        print('$' + str(amount_off))
        pyautogui.write(str(amount_off))

        pyautogui.press('tab')  # Please Select Currency
        pyautogui.press('space')  # Please Select Currency
        pyautogui.press('down', presses=2)
        pyautogui.press('enter')
    else:
        pyautogui.press('tab')  # Now at Amount off
        pyautogui.write(str(discount_amount))

    # # =Duration=(optional)=========================
    if forever_check == 1:
        control.move_and_click(coords['Duration']['Forever'], movement_duration)

    # # =Continue=========================
    pyautogui.press('end')
    control.move_and_click(coords['Continue']['Enter'], movement_duration)

    # # =Offers Page======================
    time.sleep(4)
    #control.move_and_click(coords['Offer']['AddOffer'], movement_duration)
    control.move_and_click(coords['Offer']['AddOffer'], movement_duration)
    time.sleep(0.5)
    control.move_and_click(coords['Offer']['SelectOffer'], movement_duration)
    time.sleep(0.5)

    if code:
        print(f"The code for {category_to_lookup} is {code}")
        interpreter.computer.keyboard.write(code)
    else:
        print(f"No code found for category {category_to_lookup}")

    time.sleep(6)
    pyautogui.press('enter') #confirm selection
    #control.move_and_click(coords['Offer']['ConfirmSelectOffer'], movement_duration)
    time.sleep(4)
    control.move_and_click(coords['Offer']['DiscountLink'], movement_duration)  #Copy to clipboard