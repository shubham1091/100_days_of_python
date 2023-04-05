alphabet = 'abcdefghijklmnopqrstuvwxyz'
def ceasar (start_text, shift_amount,cipher_direction):
    end_text=""
    if cipher_direction == "decode":
        shift_amount*=-1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text+=alphabet[new_position%len(alphabet)]
        else:
            end_text+=char
    print(f"Here's the {cipher_direction} result: {end_text}")
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").strip().lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift%len(alphabet)
    ceasar(text,shift,direction)
    inp = input("Type 'yes if you want to go again. Otherwise, type 'no'\n")
    if inp == 'no':
        should_continue = False
        print("Good bye!")