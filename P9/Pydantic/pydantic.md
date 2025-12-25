## 1. The Limit of URL Parameters

We sent data in the URL: /add/5/10. But what if you want to create a User? `/create_user/alice/password123/alice@email.com/25/female/admin...`

This URL is ugly, insecure (passwords in URLs are logged in history), and limited in size. For complex data, we use POST requests and send the data inside the Body (usually as JSON).

---

## 2. Enter Pydantic

It becomes the backbone of your API. We define a Class that represents the data we expect to receive.

```Python

from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    age: int
    is_admin: bool = False
```

---

## 3. Connecting it to FastAPI

When you use a Pydantic model as a function argument, `FastAPI` reads the `JSON` body, validates it against your class, and gives you a clean Python object.

---