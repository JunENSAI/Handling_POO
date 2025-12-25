## 1. Why FastAPI?

In the old days, we used Flask or Django.

- `Flask:` Lightweight but slow (Synchronous) and no built-in data validation.

- `Django:` Huge, heavy, and originally designed for generating HTML, not APIs.

- `FastAPI` is designed for the Cloud Era:

    - **Speed:** It is built on Starlette (ASGI) and runs as fast as NodeJS or Go.

    - **Standards**: It automatically generates Interactive Documentation (Swagger UI) for you.

    - **Bug Prevention:** It uses Python Type Hints (str, int) to validate data before your code even runs.

---

## 2. The Engine: Uvicorn

`FastAPI` is just the application logic. It needs a Server to run. We use Uvicorn, which is a lightning-fast ASGI (Asynchronous Server Gateway Interface) server implementation.

---