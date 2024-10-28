# Your code here (˶ᵔ ᵕ ᵔ˶)

def replace_artifacts(str):
    formatted_str = str.strip()

    formatted_str = formatted_str.replace('-', '_').replace(' ', '_')

    new_formatted_str = []
    for char in formatted_str:
        if char.isupper():
            if new_formatted_str and new_formatted_str[-1] != '_':
                new_formatted_str.append('_')
            new_formatted_str.append(char.lower())
        else:
            new_formatted_str.append(char)

    formatted_str = ''.join(new_formatted_str)

    while '__' in formatted_str:
        formatted_str = formatted_str.replace('__', '_')

    while True:

        if formatted_str[0] == '_':
            formatted_str = formatted_str[1:]
        if formatted_str[-1] == '_':
            formatted_str = formatted_str[:-1]


        while formatted_str and formatted_str[0].isdigit():
            formatted_str = formatted_str[1:]

        if (formatted_str[0] != '_' and formatted_str[-1] != '_' and formatted_str[0].isdigit() == False):
            break


    if formatted_str[0] == '_':
        formatted_str = formatted_str[1:]
    if formatted_str[-1] == '_':
        formatted_str = formatted_str[:-1]


    while formatted_str and formatted_str[0].isdigit():
        formatted_str = formatted_str[1:]


    if not formatted_str.replace('_', '').isalnum():
        return "Введено некорректное имя переменной"

    return formatted_str


test = '123123----___-123camselCase-123qweqwe'
print(replace_artifacts(test))