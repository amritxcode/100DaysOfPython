# Caesar Cipher CLI Tool

A simple Python command-line tool to **encode** or **decode** messages using the Caesar Cipher technique.

---

## Features

- Encode and decode messages using a shift value.
- Handles non-letter characters like spaces and punctuation.
- Includes an ASCII art logo.
- Allows repeated use until the user decides to exit.

---

## How to Use

1. Run the script:

   python caesar_cipher.py

2. Follow the prompts:

   - Type `encode` to encrypt or `decode` to decrypt.
   - Enter your message.
   - Enter the number of positions to shift.
   - Choose whether to run the tool again or exit.

---

## Example

Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello world!
Type the number of shifts you want:
3
Here is the encoded result: khoor zruog!
Type 'Yes' if you want to go again. Otherwise type 'No'.
no
Thank You

---

## Notes

- The cipher works with lowercase English letters only.
- Input is automatically converted to lowercase.
- Shift wraps around the alphabet (e.g., shifting `z` by 1 becomes `a`).

---