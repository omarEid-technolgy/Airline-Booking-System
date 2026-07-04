print("Welcome to the October Airlines website.")
print("This website was created by Omar Eid.")

name = input("What is your name? ")

travel = input("Do you want to travel? (yes/no): ")

price = 0

if travel.lower() == "yes":

    print("\nTicket Prices:")
    print("Economy Class = 1800")
    print("Business Class = 3000")

    travel_class = input("What is your choice? ").lower()

    if travel_class == "economy class":
        price = 1800

    elif travel_class == "business class":
        price = 3000

    else:
        print("Invalid class selected.")
        exit()

    age = int(input("How old are you? "))

    if age <= 18:
        price *= 0.5
        print("You received a 50% discount.")

    national_id = input("What is your National ID Number? ")

    print("\n---------- YOUR TICKET ----------")
    print("Name:", name)
    print("Age:", age)
    print("National ID:", national_id)
    print("Class:", travel_class.title())
    print("Price:", price)

elif travel.lower() == "no":

    print("Thank you for visiting October Airlines.")

else:

    print("Invalid choice.")

