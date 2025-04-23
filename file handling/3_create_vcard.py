# Accept contact details from the user and create a vcard that we can directly store in our mobile.
name = input("Enter full name: ")
phone = input("Enter phone number: ")
email = input("Enter email: ")

vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL;TYPE=CELL:{phone}
EMAIL:{email}
END:VCARD
"""

with open("contact.vcf", "w") as file:
    file.write(vcard)

print("vCard created successfully.")
