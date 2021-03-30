from converter import convert

with open("example.txt", encoding="utf-8") as f:
    data = f.read()

translated = convert(data)
print(translated)
#exec(compile(translated, "", "exec"))