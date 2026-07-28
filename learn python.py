"""
Make random projects to learn Python
"""
import random
def generate_random_project():
    project_ideas = [
        "Build a to-do list application",
        "Create a simple calculator",
        "Develop a weather app using an API",
        "Make a text-based adventure game",
        "Build a personal blog website",
        "Create a budget tracker",
        "Develop a quiz application",
        "Make a recipe organizer",
        "Build a chatbot",
        "Create a photo gallery"
    ]
    return random.choice(project_ideas)
if __name__ == "__main__":
    print("Random Python Project Idea:")
    print(generate_random_project())

"""
Learn Python
"""
integers = [1, 2, 3, 4, 5]
print("Done")

string_list = ["Monday", "Tuesday", "Wednesday", "Thursday"]
print(string_list[2])

letters = ["a", "b", "c", "d", "e"]
print(letters[:3])

leangues = ["Python", "Java", "C++", "Ruby", "Swift"]
print(leangues[::2])