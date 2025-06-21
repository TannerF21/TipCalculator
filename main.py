def get_valid_tip():
    while True:
        tip_input = input("Choose a tip percentage (15, 20, or 25): ").strip()
        if tip_input in ["15", "20", "25"]:
            return int(tip_input)
        else:
            print("Please enter 15, 20, or 25.")


def main():
    print("Welcome to the Tip Calculator!\n")

    try:
        total_bill = float(input("Enter the total bill amount: $"))
        if total_bill < 0:
            raise ValueError("Bill cannot be negative.")

        num_people = int(input("Enter number of people splitting the bill: "))
        if num_people <= 0:
            raise ValueError("Must be at least one person.")

        tip_percent = get_valid_tip()

        tip_amount = total_bill * (tip_percent / 100)
        total_with_tip = total_bill + tip_amount
        per_person = total_with_tip / num_people

        print("\n--- Tip Breakdown ---")
        print(f"Selected Tip: {tip_percent}%")
        print(f"Tip Amount: ${tip_amount:.2f}")
        print(f"Total Bill with Tip: ${total_with_tip:.2f}")
        print(f"Each Person Owes: ${per_person:.2f}")

    except ValueError as e:
        print(f"Input error: {e}")


if __name__ == "__main__":
    main()