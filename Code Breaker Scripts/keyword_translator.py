ui = input("keyword to be translated: ")

ui_indexed = list(ui)
ui_sorted = sorted(ui)

output = []
for char in (ui_indexed):
    num = ui_sorted.index(char)
    if num in output:
        num+= (output.count(num))
    output.append(num)
output = ''.join(char for char in str(output) if char.isalnum())
print(output)
