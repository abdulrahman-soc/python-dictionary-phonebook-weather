phone_book = {
    "0568323222": "Amal",
    "0522222232": "Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556": "Rawan",
    "0560664566": "Faisal",
    "0567917077": "Layla"
}
phone_number = input("Enter a phone number: ").strip()

if len(phone_number) == 10 and phone_number.isdigit():
    name = phone_book.get(phone_number)

    if name:
        print("The name is:", name)
    else:
        print("Sorry, the number is not found")

else:
    print("This is invalid number")
    



