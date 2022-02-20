def get_string(string: str, level: int) -> str:
    result = ' ' * ((len(string) - level) // 2) + '*' * level + ' ' * ((len(string) - level) // 2)
    return result


def delete_duplicates(ls: list[str], length: int):
    for string in ls:
        if string == '*' * length:
            ls.remove(string)
            break


def clear_diamond(ls: list[str], length: int) -> list[str]:
    result = []
    for string in ls:
        if string == ' ' * length:
            continue
        else:
            result.append(string)
    delete_duplicates(result, length)
    return result


number = int(input("Size of diamond: "))

diamond = [' ' * number for _ in range(number)]
for i in range(1, len(diamond) + 1, 2):
    diamond[i - 1] = get_string(diamond[i - 1], i)
for i in range(len(diamond), 0, -2):
    diamond.append(get_string(diamond[i - 1], i))
diamond = clear_diamond(diamond, number)

for crystal in diamond:
    print(crystal)
