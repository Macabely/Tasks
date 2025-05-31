from faker import Faker

def test():
    fake = Faker()

    while True:
        card_type = input("Enter card type (Mastercard or Visa): ").strip().capitalize()
        if card_type in ["Mastercard", "Visa"]:
            break
        print("Invalid input. Please enter 'Mastercard' or 'Visa'.")

    if card_type == "Mastercard":
        card = fake.credit_card_number(card_type="mastercard")
    elif card_type == "Visa":
        card = fake.credit_card_number(card_type="visa")

    number = " ".join(card[i:i+4] for i in range(0, len(card), 4))

    print("Fake card number generated:")
    print(f"Card type: {card_type}")
    return f"Number: {number}"

print(test())