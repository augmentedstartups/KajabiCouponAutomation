import customtkinter as ctk
import webbrowser
import pyautogui
import time
import control
import json
from interpreter import interpreter
from Backup import sqlcreate

movement_duration=0.15   #mouse movement
main_offer = 299

# Read coordinates from JSON file
with open('coordinates.json', 'r') as file:
    coords = json.load(file)

def slow_type(text, interval=0.25):
    for char in text:
        pyautogui.write(char)
        time.sleep(interval)

# Function to enable/disable discount amount entry based on the state of free_coupon_checkbox
def toggle_discount_amount_state():
    if free_coupon_checkbox.get():
        discount_amount_entry.configure(state=ctk.DISABLED, fg_color="gray")  # Disable the entry field
        discount_amount_entry.delete(0, 'end')  # Clear the entry field
        discount_amount_entry.insert(0, '0')  # Set the value to 0

    else:
        discount_amount_entry.configure(state=ctk.NORMAL, fg_color='#353638')  # Enabled the entry field

def start_automation(discount_amount,category,forever_check,category_to_lookup,isFreecouponTrue):
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

def on_go_button_pressed(event=None):
    category_to_lookup = category_combobox.get()
    print(category_to_lookup)
    print(str(duration_forever_checkbox.get()))
    # Check if the 100% Off Free Coupon checkbox is checked
    isFreecouponTrue = free_coupon_checkbox.get()
    if isFreecouponTrue:
        discount_amount = 100  # Set discount to 100 for 100% off
        print("We will generative a 100% off coupon for you.")
    else:
        discount_amount = int(discount_amount_entry.get())  # Otherwise, use the entered discount amount

    category = category_combobox.get()
    start_automation(discount_amount, category,duration_forever_checkbox.get(),category_to_lookup,isFreecouponTrue)

# Create the main window and set the theme
root = ctk.CTk()
root.title("Kajabi Coupon Generator")

# Create a frame for the input field and dropdown
input_frame = ctk.CTkFrame(root)
input_frame.pack(pady=10)
# Create the discount amount input field
ctk.CTkLabel(input_frame, text="Discount Amount:").pack(side='left', padx=(10, 0))
discount_amount_entry = ctk.CTkEntry(input_frame, width=100)
discount_amount_entry.pack(side='left', padx=5)
discount_amount_entry.insert(0, '49')  # 0 is the index where the text is to be inserted



# Create the category dropdown
ctk.CTkLabel(input_frame, text="Category:").pack(side='left')
category_combobox = ctk.CTkComboBox(input_frame, values=["JETSON", "OAK", "YOLONAS", "INFLUENCER", "AGRICULTURE", "TRADING","SELF DRIVING CAR","GAN","UNET","LANGCHAIN"])
category_combobox.pack(side='left', padx=5)
category_combobox.set("JETSON")  # Set the default value


# Create the checkbox for enabling/disabling the "Forever" duration click
duration_forever_checkbox = ctk.CTkCheckBox(root, text="Enable Forever Duration Click")
duration_forever_checkbox.pack(pady=5)
# Create the checkbox for 100% off free coupon
free_coupon_checkbox = ctk.CTkCheckBox(root, text="100% Off Free Coupon", command=toggle_discount_amount_state)
free_coupon_checkbox.pack(pady=5)


# Create the "Go" button
go_button = ctk.CTkButton(root, text="Go", command=on_go_button_pressed)
go_button.pack(pady=5)
root.bind('<Return>', on_go_button_pressed)

# Start the GUI loop
root.mainloop()


