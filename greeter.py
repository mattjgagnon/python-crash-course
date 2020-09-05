def greet_user(username = ''):
    """Display a simple greeting."""
    if username:
        print(f"Hello, {username.title()}!")
    else:
        print('Hello!')

greet_user('jesse')
greet_user()
