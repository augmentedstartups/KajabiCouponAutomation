import customtkinter as ctk
import automations

# Function to enable/disable discount amount entry based on the state of free_coupon_checkbox
def toggle_discount_amount_state():
    if free_coupon_checkbox.get():
        discount_amount_entry.configure(state=ctk.DISABLED, fg_color="gray")  # Disable the entry field
        discount_amount_entry.delete(0, 'end')  # Clear the entry field
        discount_amount_entry.insert(0, '0')  # Set the value to 0

    else:
        discount_amount_entry.configure(state=ctk.NORMAL, fg_color='#353638')  # Enabled the entry field


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

    automations.start_automation(discount_amount,duration_forever_checkbox.get(),category_to_lookup,isFreecouponTrue)

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


