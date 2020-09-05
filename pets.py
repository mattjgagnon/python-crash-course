def describe_pet(animal_type, pet_name='spot'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")

# use default positional arguments
describe_pet('hamster', 'harry')

# use keyword arguments
describe_pet(animal_type='dog', pet_name='lily')
describe_pet(pet_name='lily', animal_type='dog')
describe_pet('cat')
