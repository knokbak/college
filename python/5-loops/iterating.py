############################################################
# Licensed under the BSD 3-Clause License                  #
# See https://github.com/knokbak/college/blob/main/LICENSE #
############################################################

# Print list of IP addresses in a /24 network
# OK - 27 Sep 2023

def get_word():
    word = input('Enter word: ')
    return word

def check_for_vowels(word):
    vowel_count = 0
    for letter in word.lower():
        Vowels = ('a', 'e', 'i', 'o', 'u')
        if letter in Vowels:
            vowel_count += 1
    return vowel_count

def main():
    word = get_word()
    vowel_count = check_for_vowels(word)
    print(f'There are {vowel_count} vowels in {word}')

if __name__ == '__main__':
    main()
