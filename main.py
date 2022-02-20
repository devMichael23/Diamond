def get_string(string: str, level: int) -> str:
    pass


number = int(input("Size of diamond: "))
void_string = ""
for i in range(number):
    void_string += " "

diamond = [void_string for _ in range(number)]

for i in range(len(diamond)):
    diamond[i] = get_string(diamond[i], i)

