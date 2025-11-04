"""
Author: Arlo Virta
Date: 2025-11-03
Description: Formats a title into the proper case
"""

AVOID_CAPITALIZING = [ "the", "a", "an", "of" ]

def processing(title = ""):
    title_parts = title.lower().strip().split(" ")      # "  THE THING " -> [ "the", "thing" ]
    proper_title = ""

    for index, word in enumerate(title_parts):
        if word == "": continue

        force_capitalize = index == 0 or index == len(title_parts) - 1      # force capitalize first and last word

        if(force_capitalize or word not in AVOID_CAPITALIZING):
            word = word[0].upper() + word[1:]       # capitalize first letter, use rest of lowercase word

        proper_title += word + " "
    
    return proper_title[:-1]        # trim last character (added space)
    
    

def main():
    print("=== The Program That Corrects Titles v1.0.0 ===")
    input_title = input("Enter a title- ")

    while len(input_title.strip()) == 0:
        input_title = input("Enter a VALID title- ")
    
    print(f"Formatted title: {processing(input_title)}")

main()
