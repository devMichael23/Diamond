def get_string(string: str, level: int) -> str:
    result = ' ' * ((len(string) - level) // 2) + '*' * level + ' ' * ((len(string) - level) // 2)
    return result


number = int(input("Size of diamond: "))
void_string = ""
for i in range(number):
    void_string += " "

half_diamond = [void_string for _ in range(number)]
for i in range(1, len(diamond)+1, 2):
    half_diamond[i-1] = get_string(half_diamond[i-1], i)
