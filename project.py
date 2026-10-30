def convert_to_inr(amount,currency):
    rates={"INR":1,
           "USD":83,
           "EUR":90,
           "GBP":105
           }
    return amount*rates[currency]

def convert_currency(amount,from_currency,to_currency):
    inr_amount = convert_to_inr(amount,from_currency)
    rates={
        "INR":1,
        "USD":83,
        "EUR":90,
        "GBP":105
    }
    return inr_amount/rates[to_currency]

try:
    amount = float(input("Amount: "))
    from_currency = input("From: ").strip().upper()
    to_currency = input("To: ").strip().upper()

    currencies = ["INR","USD","EUR","GBP"]
    if from_currency not in currencies:
        print("Unsupported currency"+ " " + from_currency + "." + "Available: INR,USD,EUR,GBP.")

    elif to_currency not in currencies:
        print("Unsupported currency" + " " + to_currency +"." + "Available: INR,USD,EUR,GBP.")

    elif amount < 0:
        print("Amount cannot be negative")
    else:
        result = convert_currency(amount,from_currency,to_currency)

        print(f"{amount:g} {from_currency} = {result:.2f} {to_currency}")

except ValueError:
    print("Invalid amount.Enter a number")


