# ShareLink-API

**ShareLink-API** is a Django Rest Framework API designed to collect, store, and delete links or short text. It is perfect for users who want to seamlessly share information between devices, such as sending a link from a laptop to a phone. The API ensures secure data sharing through user authentication and token-based authorization.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [Authentication](#authentication)
- [Contributing](#contributing)


---

## Features

- **User Authentication**: Secure sign-up, login, and token-based authentication.
- **Link/Text Collection**: Allows users to store important links or short texts.
- **Deletion Capability**: Users can delete previously stored links or texts.
- **Swagger Documentation**: Integrated Swagger UI for easy API exploration.
- **Secure Access**: Only authenticated users can store, view, or delete their content.

---

## Tech Stack

- **Backend**: Django, Django Rest Framework
- **Authentication**: `dj-rest-auth`, Token-based authentication
- **Database**: PostgreSQL
- **Deployment**: Render

---

## Installation

To run this project locally, follow these steps:

### Prerequisites

- Python 3.x
- PostgreSQL or SQLite (for development)
- Pip (Python package manager)

### Steps

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Donchuks02/ShareLink-API-project.git
   cd ShareLink-API-project
   ```

2. **Create a Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:

   Create a `.env` file in the root directory and configure your secret key and database settings:

   ```bash
   SECRET_KEY=your-secret-key
   DEBUG=True
   DATABASE_URL=postgres://user:password@localhost:5432/dbname
   ```

5. **Apply Migrations**:

   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser**:

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**:

   ```bash
   python manage.py runserver
   ```

---

## API Endpoints

### Authentication

- **Register**: `/api/v1/dj-rest-auth/registration/`
  Allows new users to sign up.

  **POST** Example:

  ```json
  {
    "username": "newuser",
    "email": "newuser@example.com",
    "password1": "securepassword",
    "password2": "securepassword"
  }
  ```

- **Login**: `/api/v1/dj-rest-auth/login/`
  Authenticate and obtain a token.

  **POST** Example:

  ```json
  {
    "username": "newuser",
    "password": "securepassword"
  }
  ```

- **Logout**: `/api/v1/dj-rest-auth/logout/`
  Logout the current user and invalidate their token.

### Link/Text Collection

- **Store a Link/Text**: `/api/v1/`
  Allows an authenticated user to store a new link or short text.

  **POST** Example:

  ```json
  {
    "content": "https://useful-link.com",
  }
  ```

- **View All Links/Texts**: `/api/v1/`
  Retrieve all the links or short texts that belong to the authenticated user.

- **Delete a Link/Text**: `/api/v1/<id>/`
  Delete a specific link or text using its ID.

  **DELETE** Example:

  ```bash
  DELETE /api/v1/1/
  ```

---

## Usage

1. **Test API using Postman or Swagger**:
   - Swagger documentation is available at `https://sharelink-api.onrender.com/api/schema/swagger/`.
   - For Postman, ensure you pass the token in the `Authorization` header after logging in.

2. **Frontend Integration**:
   This API can be consumed by frontend applications to store and retrieve user-specific links and text data. Ensure the token is included in every API request.

---

## Authentication

The API uses **token-based authentication** to secure access. Once a user logs in, they receive a token that must be included in the headers of subsequent requests.

### Example of Header with Token

```bash
Authorization: Token <your_token>
```

Tokens are issued when a user logs in via `/api/dj-rest-auth/login/`.

---

## Contributing

Contributions to improve the API are always welcome! Here's how you can contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

---


## Contact

For questions or feedback, feel free to reach out via my X(Twitter): [@Dev_Chukwudi](https://x.com/Dev_Chukwudi).

---