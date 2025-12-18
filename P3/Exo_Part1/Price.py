class Price:

    def __init__(self, amount:float,currency:str):
        self.amount = amount
        self.currency = currency
    
    def __str__(self):
        return f"{self.amount} {self.currency}"
    
    def __repr__(self):
        return f"Price(amount={self.amount}, currency={self.currency})"
    
    def __add__(self,other):
        if isinstance(other, Price) and self.currency==other.currency:
            return Price(self.amount + other.amount, self.currency)
        raise TypeError("Currency must be the same for addition ")


p_1 = Price(24.5, "EUR")
p_2 = Price(5.5, "EUR")

print(p_1)

print([p_2])

res = p_1 + p_2
print(res)

p_3 = Price(30.0, "USD")

bad_res = p_1 + p_3

print(bad_res)
