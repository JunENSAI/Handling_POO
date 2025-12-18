## Task: 

- Write a class Price that handles currency.

- Init: Accepts amount (float) and currency (str, e.g., "USD").

- String (__str__): Returns format like "50.00 USD".

- Repr (__repr__): Returns "Price(amount=50.0, currency='USD')".

- Add (__add__):

    - Allows adding two Price objects only if they have the same currency.

    - If currencies differ, raise a ValueError.

    - Returns a new Price object with the summed amount.
----