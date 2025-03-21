import time
import random
from controller import fetch_pokemon_data, add_pokemon_to_db


def main():
    while True:
        pokemon_id = random.randint(1, 350)
        pokemon_schema = fetch_pokemon_data(pokemon_id)
        if pokemon_schema:
            add_pokemon_to_db(pokemon_schema)
            print(f"Added Pokemon {pokemon_schema.name} to the database.")
        else:
            print(f"Pokemon with ID {pokemon_id} not found.")
        time.sleep(10)


if __name__ == "__main__":
    main()
