## 1. The Problem: Repetitive Code

Imagine you have `50 endpoints` (Create User, Get User, Delete User, Buy Item...). In every single one of them, you need to:

- Connect to the Database.

- Check if the user is logged in.

- Log the request.

If you write `db = connect() in 50 places`, and then the database password changes, you have to fix 50 files. This is a maintenance nightmare.

--

## 2. The Solution: `Depends`

- `Dependency Injection` means "FastAPI, please build this thing for me and pass it to my function."

- You write the logic once in a separate function, and FastAPI "injects" the result into any endpoint that asks for it.

---

## 3. How it Works

- Define a function (e.g., get_db).

- In your endpoint, add a parameter: `db: Session = Depends(get_db)`.

- `FastAPI` sees Depends, runs **get_db first**, pauses it, runs your endpoint, and then finishes **get_db** (cleaning up).

---