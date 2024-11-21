import subprocess

def flush_database():
    try:
        # Run the command `python manage.py flush --noinput`
        result = subprocess.run(
            ["python", "manage.py", "flush", "--noinput"],
            check=True,
            capture_output=True,  # Capture stdout and stderr
            text=True             # Output as a string
        )
        print("Output:", result.stdout)  # Command output
        print("Error (if any):", result.stderr)  # Command error
        print("Database flush successful!")
    except subprocess.CalledProcessError as e:
        print("Error while flushing the database:")
        print(e.stderr)  # Display the error message