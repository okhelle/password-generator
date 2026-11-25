# Password generator
import secrets
import string

characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(secrets.choice(characters) for _ in range(16))

print(password)
