Task: Create a class **Page**.

- \_\_init__: Accepts a **list of items** (e.g., `["a", "b", "c", "d"]`) and a **page_size** (e.g., 2).

- \_\_iter__: Making **the object iterable** should only yield the items for the first page. (e.g., if page size is 2, looping over the object yields only "a" and "b").

- `@classmethod from_text:`

    - Input: A single string "item1,item2,item3" and page_size.

    - Logic: Splits the string by comma and creates the Page object.

- `@staticmethod helper_message:`

    - Returns a string: "Pagination helps manage large datasets."