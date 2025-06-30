from api_client import submit_feedback

def collect_feedback():
    print("=== Feedback Form ===")
    name = input("Your Name: ")
    email = input("Your Email: ")
    message = input("Your Feedback: ")

    feedback = {
        "name": name,
        "email": email,
        "message": message
    }

    result = submit_feedback(feedback)

    if "error" in result:
        print("❌ Failed to submit feedback:", result["error"])
    else:
        print("✅ Feedback submitted successfully!")
        print("Server response:", result)

if __name__ == "__main__":
    collect_feedback()
