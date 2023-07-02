# Recipe App

This is a simple recipe application built with Flask.

## Installation

1. Clone the repository:

 2. Install the dependencies:
 3. pip install -r requirements.txt
 4. Set up the database:
     flask db init
     flask db migrate
     flask db upgrade
5. Run the application:
   flask run


The application should now be running on `http://localhost:5000`.

## API Endpoints

- User Registration: `POST /register`
- Create a new user account.
- Sample Input:
 ```
 {
     "username": "john_doe",
     "password": "password123"
 }
 ```

- User Login: `POST /login`
- Login with an existing user account.
- Sample Input:
 ```
 {
     "username": "john_doe",
     "password": "password123"
 }
 ```

- Create Recipe: `POST /recipes`
- Create a new recipe.
- Requires authentication (JWT token).
- Sample Input:
 ```
 {
     "title": "Pizza",
     "description": "Delicious homemade pizza recipe"
 }
 ```

- Update Recipe: `PUT /recipes/<recipe_id>`
- Update an existing recipe.
- Requires authentication (JWT token).
- Sample Input:
 ```
 {
     "title": "Pizza Margherita",
     "description": "Authentic Italian pizza recipe"
 }
 ```

- Delete Recipe: `DELETE /recipes/<recipe_id>`
- Delete an existing recipe.
- Requires authentication (JWT token).

- Get All Recipes: `GET /recipes`
- Get a list of all recipes.

- Add Comment to Recipe: `POST /recipes/<recipe_id>/comments`
- Add a comment to a recipe.
- Requires authentication (JWT token).
- Sample Input:
 ```
 {
     "text": "This recipe is amazing!"
 }
 ```

Please note that for the endpoints that require authentication, you need to include the JWT token in the `Authorization` header of the request. The token can be obtained by logging in with a valid user account.




