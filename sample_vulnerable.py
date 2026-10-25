
# Intentionally insecure examples for scanner testing only

password = "demo_password_123"
api_key = "example_test_key"

user_input = input("Enter a value: ")
result = eval(user_input)

query = f"SELECT * FROM users WHERE name = '{user_input}'"
