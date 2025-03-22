# Pokémon CRUD Application

This project is a simple Pokémon CRUD application that interacts with the [PokéAPI](https://pokeapi.co/) to fetch Pokémon data and store it in a local *SQLite* database. The application is built using *Python* with *SQLAlchemy* for database management and *Pydantic* for validation.

## Features

- Fetch Pokémon data from the PokéAPI.
- Store Pokémon data in a local SQLite database.
- Automatically fetch and add random Pokémon to the database every 10 seconds.

## Project Structure

### Key Files

- `src/main.py`: Entry point of the application. Fetches random Pokémon data and adds it to the database.
- `src/controller.py`: Contains logic for fetching Pokémon data from the PokéAPI and adding it to the database.
- `src/db.py`: Configures the SQLite database connection and session.
- `src/models.py`: Defines the database model for Pokémon.
- `src/schema.py`: Defines the Pydantic schema for Pokémon data validation.

## Requirements

- Python 3.13.2
- SQLite
- Dependencies listed in `requirements.txt`

## Setup

1. Clone the repository:
   `git clone git@github.com:ViniciusSonntagDorow/crud_pokemon.git`
   `cd crud_pokemon`

2. Create a virtual enviroment and activate it:
    `python -m venv .venv`
    `source .venv/bin/activate`
    or
    `.venv\Scripts\activate\`

3. Install dependencies
    `pip install -r requirements.txt`

4. Run the application
    `python src/main.py`