## 1. What is an API?

An API (Application Programming Interface) is a waiter.

- **The Kitchen:** Your Database & Python Logic.

- **The Customer:** A Mobile App, a Website, or another Server.

- **The API:** The Customer tells the API what they want, and the API gets it from the kitchen.

---

## 2. What is REST?

`REST (Representational State Transfer)` is a set of rules for how this conversation happens. It uses standard HTTP methods (verbs) to perform actions on Resources (nouns).

### The 4 Major Verbs (CRUD)

- `GET:` Retrieve data. (Read)

    - **GET /users** -> Get all users.

    - **GET /users/1** -> Get user ID 1.

- `POST:` Create new data. (Create)

    - **POST /users** -> Create a new user (Data sent in body).

- `PUT / PATCH: `Update existing data. (Update)

    - **PUT /users/1** -> Update user 1.

- `DELETE:` Remove data. (Delete)

    - **DELETE /users/1** -> Delete user 1.

---

## 3. The Status Codes

The API replies with a number to indicate success or failure.

- `2xx (Success)`:

    - **200 OK**: "Here is your data."

    - **201 Created**: "I built the thing you asked for."

- `4xx (Client Error - You messed up)`:

    - **400 Bad Request**: "You sent me garbage data."

    - **401 Unauthorized**: "Who are you?"

    - **404 Not Found**: "That user doesn't exist."

- `5xx (Server Error - I messed up)`:

    - **500 Internal Server Error**: "My code crashed."

---

## 4. Key Takeaway

- Resources are `URLs`: /products, /orders.

- Actions are `Verbs`: GET, POST.

- Communication is `JSON`: The universal language of the web.

---

## 5 Task: Fill in the blanks below.

- Action: I want to read the article with ID 55.

    - Method: _______ (response : `GET`)

    - URL: /articles/_______ (response :  `/articles/55`)

- Action: I want to publish a new article.

    - Method: _______ (response : `POST`)

    - URL: /articles

- Action: I want to delete the comment with ID 12 belonging to article 55.

    - Method: _______ (repose : `DELETE`)

    - URL: /articles/55/comments/_______ (response : `/articles/55/comments/12`)

- Action: I want to update the title of article 55.

    - Method: _______ (response : `PATCH`)

    - URL: /articles/55

---