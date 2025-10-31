# query_pets.py
import sqlite3

connection = sqlite3.connect("pets.db")
cursor = connection.cursor()

while True:
    person_id = int(input("Enter person ID (or -1 to exit): "))
    if person_id == -1:
        print("Exiting program.")
        break

    cursor.execute("SELECT first_name, last_name, age FROM person WHERE id = ?", (person_id,))
    person = cursor.fetchone()

    if person:
        print(f"{person[0]} {person[1]}, {person[2]} years old")

        cursor.execute("""
        SELECT pet.name, pet.breed, pet.age, pet.dead
        FROM pet
        JOIN person_pet ON pet.id = person_pet.pet_id
        WHERE person_pet.person_id = ?
        """, (person_id,))

        pets = cursor.fetchall()

        for pet in pets:
            status = "that is" if pet[3] == 1 else "who is"
            print(f"  {person[0]} {person[1]} owned {pet[0]}, a {pet[1]}, {status} {pet[2]} years old.")
    else:
        print("No person found with that ID.")
