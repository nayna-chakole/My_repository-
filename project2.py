# Word Counter Program
# This program counts the number of words in a given sentence or paragraph.

def count_words(text):
    
    '''Counts the number of words in the text.'''
    if not text.strip():
        return 0
    words = text.split()
    
    return len(words)

def main():
    print("\n Welcome to the Word Counter Program! ")
    print("Enter a sentence or paragraph, and I'll count the words!!.\n")

    # Taking user input
    user_input = input(" Enter your text: ").strip()

    word_count = count_words(user_input)

    print("\n")
    if word_count == 0:
        print("Oops! You didn't enter any text. Please try again.")
    else:
        print("Word Count: " + str(word_count) + " words")
    
    print("\n")

if __name__ == "__main__":
    main()