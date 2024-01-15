def count_words(text):
    """
    Count the number of words in the given text.
    """
    # Check if the input text is empty
    if not text:
        return 0
    
    # Split the text into words using whitespace as the separator
    words = text.split()
    
    # Return the count of words
    return len(words)

def main():
    # Prompt the user to enter a sentence or paragraph
    user_input = input("Enter a sentence or paragraph: ")
    
    # Call the function to count words
    word_count = count_words(user_input)
    
    # Display the word count to the console
    print(f"Word count: {word_count}")

# Run the main function if the script is executed
if _name_ == "_main_":
    main()