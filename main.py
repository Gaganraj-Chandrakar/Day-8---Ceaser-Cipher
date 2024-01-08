from art import logo

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesar(start_text, jump, task):
    end_text = ""
    if task == "decode":
        jump *= -1
    for text_pointer in range(len(start_text)):
        if text[text_pointer] not in alphabet:
            end_text += text[text_pointer]
        else:
            index = alphabet.index(start_text[text_pointer])
            end_text += alphabet[(index + jump) % 26]
    print(f"Here's the {task}d result: {end_text}")


print(logo)
go_again = True

while go_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    go_on = input("Type 'yes' if you want to go again. Otherwise type 'no'. ")
    if go_on.lower() == 'no':
        go_again = False
