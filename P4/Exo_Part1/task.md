## Task:

- Create a Singleton class `DBConnection`:

- Implement `__new__` to ensure only one instance exists.

- In `__init__`, set self.status = "Connected".

- Create a Factory class ModelFactory:

    - Add a static method create_model(model_type).

    - If model_type is "user", return a string "User Model Created".

    - If model_type is "product", return a string "Product Model Created".

    - Otherwise, raise ValueError.

- Test it:

    - Create two variables `conn1` and `conn2` from `DBConnection`. Print conn1 is conn2 (should be True).

    - Use the Factory to create a "user" model.