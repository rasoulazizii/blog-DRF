This project is a simple yet powerful RESTful API for a blog platform, built with Django and Django REST Framework (DRF). It serves as a foundational project for demonstrating core backend development skills, including user authentication, CRUD operations, and permission handling.

The primary goal of this project is to provide a clean and robust API for creating, reading, updating, and deleting blog posts and their associated comments.

---

## Features

-   **JWT Authentication**: Secure user registration and login using JSON Web Tokens (`djangorestframework-simplejwt`).
-   **Post Management**: Full CRUD (Create, Read, Update, Delete) functionality for blog posts.
-   **Comment System**: Users can add and view comments on posts.
-   **Permission System**:
    -   Any visitor (authenticated or not) can view posts and comments.
    -   Only authenticated users can create new posts or comments.
    -   Only the author of a post can edit or delete it.
-   **Nested Serialization**: Comments are nested within the post detail endpoint for a clean and efficient response.
-   **Pagination**: API responses for lists are paginated to ensure performance.

---

## API Endpoints

The base URL for the API is `/api/`.

### Authentication (`/api/accounts/`)

| Method | Endpoint                  | Description                                |
| :----- | :------------------------ | :----------------------------------------- |
| `POST` | `/register/`              | Register a new user.                       |
| `POST` | `/token/`                 | Obtain JWT access and refresh tokens.      |
| `POST` | `/token/refresh/`         | Refresh an expired access token.           |

### Blog Posts (`/api/blog/`)

| Method | Endpoint                  | Description                                |
| :----- | :------------------------ | :----------------------------------------- |
| `GET`    | `/posts/`                 | Get a paginated list of all posts.         |
| `POST`   | `/posts/`                 | Create a new post (Authentication required). |
| `GET`    | `/posts/<int:pk>/`        | Retrieve a single post by its ID.          |
| `PUT`    | `/posts/<int:pk>/`        | Update a post (Author only).               |
| `PATCH`  | `/posts/<int:pk>/`        | Partially update a post (Author only).     |
| `DELETE` | `/posts/<int:pk>/`        | Delete a post (Author only).               |

### Comments (`/api/blog/`)

| Method | Endpoint                        | Description                                     |
| :----- | :------------------------------ | :---------------------------------------------- |
| `GET`    | `/posts/<int:post_pk>/comments/` | Get all comments for a specific post.           |
| `POST`   | `/posts/<int:post_pk>/comments/` | Create a new comment for a post (Auth required). |
