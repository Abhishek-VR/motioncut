# -*- coding: utf-8 -*-
"""motioncut_exp2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jmvF34LsZXeR5NgUbtCtSTXTJe1zELAi
"""

def word_count(text):

    if not text.strip():
        return 0
    words = text.split()
    return len(words)

def main():
    print("Welcome to the Word Counter!")
    while True:
        text = input("Please enter a sentence or paragraph (or 'q' to quit): ")
        if text.lower() == 'q':
            print("Exiting...")
            break
        count = word_count(text)
        print(f"Word count: {count}")

if __name__ == "__main__":
    main()