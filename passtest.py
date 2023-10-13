from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Now you can access the environment variables as follows
import os

HFreadAPIkey = os.getenv("HUGGINGFACE_READ_API")
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
secret_key = os.getenv("SECRET_KEY")

# Use the environment variables in your application
print(f"DB Host: {db_host}")
print(f"DB User: {db_user}")
print(f"DB Password: {db_password}")
print(f"Secret Key: {secret_key}")
