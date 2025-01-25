import random
import string

# Lists of adjectives and nouns
adjectives = ["Yummy", "Happy", "simily", "Brave", "CLUMSY", "Charming", "Gentle", "Funny", "Funky", "Love","Lovely","Cute","Silly"]
nouns = ["Tiger","Lion", "Dragon", "Penguin", "Panda", "Parrot", "Unicorn", "Monkey", "Lizard", "RABBIT", "Robot","Peacock","Crockodile"]

# Function to generate a random username
def generate(numbers=True, special_chars=True, username_len=None):
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    
    username = f"{adj}{noun}"
    
    if numbers:
        username += str(random.randint(0,999))
    
    if special_chars:
        username += random.choice(string.punctuation)
    
    if username_len and len(username) > username_len:
        username = username[:username_len]
    
    return username

# Function to save usernames to a file
def save_username(usernames, filename="usernames.txt"):
    try:
        with open(filename, "w") as file:
            for username in usernames:
                file.write(username + "\n")
        print(f"Usernames saved to {filename}")
    except IOError as e:
        print(f"Error saving to file: {e}")

# Main function for user interaction
def main():
    print("Welcome to the Random Username Generator!")
    num_Usernames = int(input("How many usernames would you like to generate? "))
    numbers = input("Include numbers in usernames? (y/n): ").strip().lower() == 'y'
    special_chars = input("Include special characters in usernames? (y/n): ").strip().lower() == 'y'
    username_len = input("Enter maximum username length (or press Enter to skip): ").strip()
    if username_len.isdigit():
        username_len = int(username_len)
    else:
        username_len = None

    
    usernames = []
    for i in range(num_Usernames):
        usernames.append(generate(numbers, special_chars, username_len))
    
    print("\nGenerated Usernames:")
    for username in usernames:
        print(username)
    
    save = input("\nSave usernames to a file? (y/n): ").strip().lower()
    if save == 'y':
        filename = input("Enter filename (default: usernames.txt): ").strip() 
        if filename == "":
            filename = "usernames.txt"
    save_username(usernames, filename)

if __name__ == "__main__":
    main()
