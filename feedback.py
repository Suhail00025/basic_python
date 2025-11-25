try:
    name = input("Enter your name: ").strip()
    feedback = input("Enter your feedback: ").strip()

    if not name:
        raise ValueError("Name cannot be empty.")
    if not feedback:
        raise ValueError("Feedback cannot be empty.")

except ValueError as e:
    print(f"Error: {e}")

else:
    print("\nThank you for your feedback!")
    print(f"Name: {name}")
    print(f"Feedback: {feedback}")

finally:
    print("\nProcess complete. Have a nice day!")
