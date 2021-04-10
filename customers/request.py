CUSTOMERS = [
    {
        "id": 1,
        "name": "Susan Pring",
        "address": "2038 Mink Dr",
        "animalId": 3
    },
    {
        "id": 2,
        "name": "Jaron Lee",
        "address": "183 Addles Blue ct",
        "animalId": 2
    },
    {
        "id": 3,
        "name": "Jada Walker",
        "address": "900 Talloway Springs Dr",
        "animalId": 4
    },
    {
        "id": 4,
        "name": "Karen Jen",
        "address": "100 Damp Dew Dr",
        "animalId": 2
    },
    {
        "id": 5,
        "name": "Billy Jones",
        "address": "1091 Sunny River Dr",
        "animalId": 1
    }
]


def create_customer(customer):
    # Get the id value of the last customer in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the customer dictionary
    customer["id"] = new_id

    # Add the customer dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer

# doesnt have self bc is not in class


def get_all_customers():
    return CUSTOMERS

# Function with a single parameter


def get_single_customer(id):
    # Variable to hold the found customer, if it exists
    requested_customer = None

    # Iterate the CUSTOMERS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer
