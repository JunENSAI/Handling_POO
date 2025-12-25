## 1. The Core Problem: Over-Sharing

This is the most common security vulnerability in junior APIs.

- **Database:** Your User table has fields: id, username, email, password_hash, created_at.

- **API:** You fetch the user from the DB and return it: return user_from_db.

- **Disaster:** Your API sends the password_hash in the JSON response to the public.

---

## 2. The Solution: `Pydantic Response Models`

We use `Pydantic to create a Filter`. We define a specific model for Output that strictly lists only the fields we want the public to see.

FastAPI has a magic parameter `response_model`. Even if your function returns an object with 50 sensitive fields, FastAPI will strip out everything that isn't in the response_model.

---