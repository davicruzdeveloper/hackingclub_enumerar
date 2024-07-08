def adjust_character(current_char, difference):
    ascii_value = ord(current_char)
    new_ascii_value = ascii_value + difference
    return chr(new_ascii_value)

def adjust_string_interactively(initial_string):
    new_string = list(initial_string)
    for i in range(12, len(initial_string) - 1):  # Pular os primeiros 12 caracteres e o último '}'
        current_char = new_string[i]
        difference = int(input(f"caractere '{current_char}' na posicao {i}: "))
        new_char = adjust_character(current_char, difference)
        new_string[i] = new_char
        updated_string = ''.join(new_string)
        print(f"ajustado '{current_char}' feito para {i} with difference {difference}: novo '{new_char}'")
        print("string final:", updated_string)
    return ''.join(new_string)

# example of use
initial_string = "hackingclub{flag_aqui_nao}"

adjusted_string = adjust_string_interactively(initial_string)
print("", adjusted_string)
