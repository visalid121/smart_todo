import random
from datetime import datetime, timedelta

def generate_task_suggestion():
    """Generate a random task suggestion for testing purposes."""
    task_titles = [
        "Complete project documentation",
        "Schedule team meeting",
        "Review pull requests",
        "Update dependencies",
        "Write unit tests",
        "Plan next sprint",
        "Code review",
        "Bug fixing",
        "Feature implementation",
        "Performance optimization"
    ]
    
    categories = ["work", "personal", "study", "health", "finance"]
    
    # Generate a random deadline between now and 7 days from now
    now = datetime.now()
    days_ahead = random.randint(1, 7)
    random_deadline = now + timedelta(days=days_ahead)
    
    suggestion = {
        "title": random.choice(task_titles),
        "deadline": random_deadline.isoformat(),
        "category": random.choice(categories)
    }
    
    return suggestion

def get_suggestions(count=3):
    """Get multiple task suggestions."""
    return [generate_task_suggestion() for _ in range(count)]
