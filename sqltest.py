from Backup import sqlcreate

category_to_lookup = "JETSON"  # Replace with the category you want to look up
code = sqlcreate.get_code_for_category(category_to_lookup)

if code:
    print(f"The code for {category_to_lookup} is {code}")
else:
    print(f"No code found for category {category_to_lookup}")