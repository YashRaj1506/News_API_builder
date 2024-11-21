import subprocess

def flush_database():
    """
    Flush the database, removing all data but preserving the schema.
    """
    try:
        print("Flushing the database...")
        result = subprocess.run(
            ["python", "manage.py", "flush", "--noinput"],
            check=True,
            capture_output=True,
            text=True
        )
        print("Database flushed successfully.")
        print("Output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error occurred while flushing the database:")
        print(e.stderr)


def create_superuser(username, email, password):
    """
    Create a superuser programmatically after flushing the database.
    """
    try:
        print(f"Creating superuser with username '{username}'...")
        # Run the createsuperuser command
        subprocess.run(
            [
                "python", "manage.py", "createsuperuser",
                "--username", username,
                "--email", email,
                "--noinput"
            ],
            check=True,
            capture_output=True,
            text=True
        )

        # Set the password using the Django ORM in a subprocess shell
        print("Setting password for superuser...")
        subprocess.run(
            [
                "python", "manage.py", "shell", "-c", f'''
from django.contrib.auth.models import User
user = User.objects.get(username="{username}")
user.set_password("{password}")
user.save()
print("Superuser '{username}' password set successfully!")
            '''
            ],
            check=True
        )
        print(f"Superuser '{username}' created successfully.")
    except subprocess.CalledProcessError as e:
        print("Error occurred while creating superuser:")
        print(e.stderr)
