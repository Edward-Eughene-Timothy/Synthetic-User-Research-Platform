import random

def generate_persona():

    occupations = [
        "Student",
        "Software Engineer",
        "Business Owner",
        "Teacher",
        "Homemaker",
    ]

    interests = [
        "Technology",
        "Shopping",
        "Education",
        "Finance",
        "Healthcare",
    ]

    persona = {
        "name": f"User_{random.randint(100,999)}",
        "age": random.randint(18, 60),
        "occupation": random.choice(occupations),
        "interest": random.choice(interests),
        "budget": random.choice(["Low", "Medium", "High"]),
    }

    return persona

def generate_behavior(persona):

    if persona["occupation"] == "Student":
        behavior = "Price conscious"

    elif persona["occupation"] == "Software Engineer":
        behavior = "Technology focused"

    elif persona["occupation"] == "Business Owner":
        behavior = "Value focused"

    else:
        behavior = "Convenience focused"

    persona["behavior"] = behavior

    return persona


if __name__ == "__main__":
    user = generate_persona()
    generate_behavior(user)
    print(user)
