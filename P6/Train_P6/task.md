## Task Requirements:

- Imports: Use logging and typing.

- Class: Create DataProcessor.

- Method: process_data(data: list[int]) -> float.

    - It should calculate the average of the list.

    - Logging: Log an INFO message: "Processing N items".

    - Error Handling: If the list is empty, raise a custom EmptyDataError.

- Test: Write a pytest function (in the same script or below) that:

- Uses pytest.raises to verify that passing an empty list [] triggers the EmptyDataError.

---