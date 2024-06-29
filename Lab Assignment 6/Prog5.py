# Create a simple language translator using dictionaries. Store pairs of 
# words or phrases in dictionaries for different languages. Prompt the 
# user to enter a word or phrase in one language and translate it to 
# another language by looking it up in the dictionaries
def display_menu():
    print("\nSimple Language Translator")
    print("1. Translate English to Spanish")
    print("2. Translate Spanish to English")
    print("3. Translate English to French")
    print("4. Translate French to English")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

def translate(word, dictionary):
    return dictionary.get(word.lower(), "Translation not found.")

def main():
    english_to_spanish = {
        "hello": "hola",
        "goodbye": "adiós",
        "please": "por favor",
        "thank you": "gracias",
        "yes": "sí",
        "no": "no",
        "dog": "perro",
        "cat": "gato"
    }

    spanish_to_english = {v: k for k, v in english_to_spanish.items()}

    english_to_french = {
        "hello": "bonjour",
        "goodbye": "au revoir",
        "please": "s'il vous plaît",
        "thank you": "merci",
        "yes": "oui",
        "no": "non",
        "dog": "chien",
        "cat": "chat"
    }

    french_to_english = {v: k for k, v in english_to_french.items()}

    while True:
        choice = display_menu()
        if choice == '1':
            word = input("Enter an English word or phrase: ")
            print("Spanish translation:", translate(word, english_to_spanish))
        elif choice == '2':
            word = input("Enter a Spanish word or phrase: ")
            print("English translation:", translate(word, spanish_to_english))
        elif choice == '3':
            word = input("Enter an English word or phrase: ")
            print("French translation:", translate(word, english_to_french))
        elif choice == '4':
            word = input("Enter a French word or phrase: ")
            print("English translation:", translate(word, french_to_english))
        elif choice == '5':
            print("Exiting the Language Translator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
