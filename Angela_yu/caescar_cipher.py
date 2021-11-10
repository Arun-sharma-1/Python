from typing import Text
alphabelt = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
             'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# only encoe will cause problem not decode coz it start from negative in negative indexing not the underflow case


def caesar(plain_text, shift_amount, cipher_direction):
    end_text = ''
    for letter in plain_text:
        if letter in alphabelt:
            position = alphabelt.index(letter)
            if cipher_direction == 'decode':
                shift_amount *= -1
            new_index = position+shift_amount
            end_text += alphabelt[new_index]
    print(f'The {cipher_direction}d text is {end_text}: ')


should_end = False
while not should_end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(text, shift, direction)

    restart = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")


# def encrypt(Text, shift):
        # for i in range(len(Text)):
        #     text=''
        #     text[i]=alphabelt[i+shift] 'str' object does not support item assignment
        # print(text)

        # cipher_text = ''
        # for letter in Text:
        #     position = alphabelt.index(letter)
        #     new_position = position+shift
        #     new_letter = alphabelt[new_position]
        #     cipher_text += new_letter  # here u are not assigning we are adding to string
        # print(cipher_text)
        # print(type(new_letter))
        # print(type(cipher_text))


# def decode(cipher_text, shift):
#     decoded_text = ''
#     for letter in cipher_text:
#         position = alphabelt.index(letter)
#         new_position = position-shift
#         new_letter = alphabelt[new_position]
#         decoded_text += new_letter
#     print(decoded_text)
