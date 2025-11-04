"""
Author: Arlo Virta
Date: 2025-11-04
Description: Separates entered praises by exclamation point and displays them formatted
"""

def processing(phrase_response = ""):
    phrases = phrase_response.strip().split("!")
    new_phrases = list()

    for phrase in phrases:
        phrase = phrase.strip()

        if phrase == "": continue

        new_phrases.append(phrase.capitalize() + "!")
    
    return new_phrases

def main():
    print("""
=== The Program That Separates Entered Affirmation Messages v1.0.0 ===
This program formats entered phrases of encouragement into multiple entries, delimited by an exclamation point.
Enter as many phrases as you would like.
    """)
    phrase_response = input("Enter phrases, separated by exclamation points- ")

    while len(phrase_response.strip().replace("!", "")) == 0 or "!" not in phrase_response:
        phrase_response = input("Please enter at least one phrase ending in an exclamation point- ")
    phrases = processing(phrase_response)

    print("List of inputted phrases: ")
    for i in range(len(phrases)):
        print(str(i + 1) + ": " + phrases[i])

main()