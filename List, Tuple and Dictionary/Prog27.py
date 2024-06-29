# Create a PhoneDic where the pair is name and phone number (atleast 10). Input the name of the person to print the phone number in python.
PhoneDic = {
    "John": "123-456-7890",
    "Alice": "234-567-8901",
    "Bob": "345-678-9012",
    "Emma": "456-789-0123",
    "Michael": "567-890-1234",
    "Sarah": "678-901-2345",
    "David": "789-012-3456",
    "Emily": "890-123-4567",
    "Daniel": "901-234-5678",
    "Olivia": "012-345-6789"
}

def find_phone_number(name):
    if name in PhoneDic:
        return PhoneDic[name]
    else:
        return "Name not found in the PhoneDic."

name = input("Enter the name to find the phone number: ")
print(find_phone_number(name))
