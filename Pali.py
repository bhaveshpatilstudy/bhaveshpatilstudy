def palindrome_checker():
    print("=== PALINDROME CHECKER ===")
    text = input("Enter a word or number: ")
    
    # Preprocess: ignore case and spaces
    clean_text = text.replace(" ", "").lower()
    reversed_text = clean_text[::-1]

    if clean_text == reversed_text:
        print(f"'{text}' is a palindrome.")
    else:
        print(f"Error404:'{text}' is not a palindrome.")

palindrome_checker()
