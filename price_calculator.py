def calculate_gross_net():
    print("Product Gross and Net Price Calculator (€)")

    # User input
    try:
        product = input("Enter the product name: ")
        gross = float(input("Enter the gross price (€): "))
        vat_percentage = float(input("Enter the VAT rate (%): "))

        # Convert VAT percentage to decimal
        vat = vat_percentage / 100

        # Calculate net price
        net = gross / (1 + vat)

        # Calculate VAT amount
        vat_amount = gross - net

        # Display the result
        print("\n----- Result -----")
        print(f"Product: {product}")
        print(f"Gross price: {gross:.2f} €")
        print(f"Net price: {net:.2f} €")
        print(f"VAT amount: {vat_amount:.2f} € ({vat_percentage}%)")
        print("------------------")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Run the program
calculate_gross_net()
