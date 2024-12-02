# Recipe Generator App

A web-based recipe generator that allows users to create, search, and retrieve random recipes. Built with Flask, SQLAlchemy, and PostgreSQL, containerized using Docker.

## Features

- Add Recipes: Submit recipes with ingredients, instructions, cuisine, and meal type.
- Search Recipes: Find recipes by name, cuisine, or meal type.
- Random Recipe: Retrieve a randomly selected recipe.
- Database Integration: Powered by PostgreSQL for reliable data storage.
- Containerized Environment: Easily deployable using Docker.

## Getting Started

1. **Clone the repository**

   ```bash
   git clone https://github.com/mchourishi//recipe-generator.git
   cd recipe-generator
   ```

2. **Setup Environment Variables**

   Rename .env.copy to .env and update the database connection settings as needed.

3. **Build and Start the Application**

   `docker-compose up --build`

   This will:

   - Build the Flask app and PostgreSQL services.
   - Expose the Flask app on http://127.0.0.1:5000.

## Usage

1.  Get a Random Recipe: From the app, click on 'Get Random Recipe' button.
2.  Search Recipe: From the app, type in the search bar to find a recipe by name, cuisine, or meal type.
3.  Add Recipe: This is just an api call to add a new recipe and can be done using postman or any other tool that can make http requests.

            Eg:

            ````
            curl -X POST http://127.0.0.1:5000/add -H "Content-Type: application/json" \
            -d '{"name": "Spaghetti Carbonara", "ingredients": "Spaghetti, eggs, pancetta, parmesan cheese, pepper", "instructions": "Cook spaghetti. Fry pancetta. Mix eggs with cheese. Combine all.", "cuisine": "Italian", "meal_type": "main"}'

            ````
