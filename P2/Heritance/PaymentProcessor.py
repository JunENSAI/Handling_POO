class PaymentProcessor:
    def __init__(self, currency="USD"):
        self.currency = currency
        self.status = "Pending"

    def process_payment(self, amount):
        print(f"--- Starting Transaction ---")
        print(f"Validating currency: {self.currency}")

class PayPalProcessor(PaymentProcessor):
    def __init__(self, currency, email):
        super().__init__(currency) 
        self.email = email

    def process_payment(self, amount):
        super().process_payment(amount)

        print(f"Connecting to PayPal API for {self.email}...")
        print(f"Charging ${amount}...")
        self.status = "Paid"

# Usage
pay = PayPalProcessor("EUR", "user@example.com")
pay.process_payment(50)