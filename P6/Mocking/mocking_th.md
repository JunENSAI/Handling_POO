## 1. Fixtures: The "Setup" Problem

Imagine you are testing a Database class.

- Test A needs a connected DB.

- Test B needs a connected DB.

- Test C needs a connected DB.

If you write `db = Database()` in every test, you are violating DRY (Don't Repeat Yourself). Fixtures allow you to define the setup logic once.

```Python
@pytest.fixture
def db_conn():
    conn = connect_to_db()
    yield conn
    conn.disconnect()
```

## 2. Mocking: The "Dependency" Problem

This is the hardest concept for new engineers. Your code rarely lives in isolation. It talks to:

- PostgreSQL (Database)

- Stripe (Payment API)

- AWS S3 (File Storage)

You cannot let your unit tests talk to these real services.

- It's slow.

- It costs money (API calls).

- It's unreliable (What if the internet is down?).

`The Solution:` A Mock is a magical object that pretends to be the real thing.

- **Real Object:** "I will connect to Postgres at 192.168.1.5..."

- **Mock Object:** "I am a Postgres connection! (Just kidding, I'm empty, but I will return True if you ask if I'm connected)."

We use `unittest.mock` (standard library) or `pytest-mock`.

---