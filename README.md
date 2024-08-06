# Auth Service

This repository contains the authentication microservice implemented using Flask and JWT.

## Instructions

### How to Programmatically Request Data

To request data from the microservice, you need to use the following endpoints:

- **Register User**: `POST /register`
    - Request body:
      ```json
      {
        "username": "your_username",
        "email": "your_email",
        "password": "your_password"
      }
      ```
    - Response:
      ```json
      {
        "message": "User created successfully"
      }
      ```

- **Login User**: `POST /login`
    - Request body:
      ```json
      {
        "username": "your_username",
        "password": "your_password"
      }
      ```
    - Response:
      ```json
      {
        "access_token": "your_access_token"
      }
      ```

- **Update User**: `PUT /update`
    - Request header:
      ```plaintext
      Authorization: Bearer your_access_token
      ```
    - Request body:
      ```json
      {
        "username": "new_username",
        "email": "new_email",
        "password": "new_password",
        "current_password": "your_current_password"
      }
      ```
    - Response:
      ```json
      {
        "access_token": "your_new_access_token",
        "message": "User information updated successfully"
      }
      ```
- **Get User Information**: `GET /profile`
    - Request header:
      ```plaintext
      Authorization: Bearer your_access_token
      ```
    - Response:
      ```json
      {
        "id": "user_id",
        "username": "your_username",
        "email": "your_email"
      }
      ```
- **Delete User**: `DELETE /delete`
    - Request header:
      ```plaintext
      Authorization: Bearer your_access_token
      ```
    - Response:
      ```json
      {
        "message": "User account deleted successfully"
      }
      ```

### UML Sequence Diagram



### Mitigation Plan

1. **Teammate**: I implemented “Microservice A” for Joonbum Kang.
2. **Current Status**: The microservice is fully implemented and tested.
3. **Access**: My teammate can access the microservice by cloning this GitHub repository and running the code locally. Instructions for running the service are provided below.
4. **Availability**: If there are any issues accessing or calling the microservice, please contact me via Discord.
5. **Notification**: If my teammate cannot access/call the microservice, they should notify me as soon as possible, but no later than 2 days before the deadline.
6. **Additional Information**: Integration example code with Flask application will be added later.

## Running the Service

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/auth.git
    cd auth
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the service:
    ```bash
    flask run
    ```
4. The service will be available at http://localhost:5000.