alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

user_choice = input("Type 'encode' to encrypt and 'decode' to decrypt:\n")
user_text = input("Type your message:\n").lower()
shifted = int(input("Type shift number:\n"))



def encrypt(original_text, shift):
    for letter in original_text:
        if letter in alphabet:
            shifted_pos = (alphabet.index(letter) + shift )% 26
            print(alphabet[shifted_pos].capitalize(), end="")
        else:
            print(letter, end="")
def decrypt(original_text, shift):
    for letter in user_text:
        if letter in alphabet:
            shifted_pos= (alphabet.index(letter) - shift) % 26
            print(alphabet[shifted_pos].capitalize(),end="")
        else:
            print(letter, end="")
if user_choice== "encode":
    encrypt(user_text, shifted)
elif user_choice== "decode":
    decrypt(user_text,shifted)
else:
    print("Invalid Entry! Please check again.")