import pyperclip, re


text = str(pyperclip.paste())
matches = []
url_finder = re.compile(
    r"(http|https)(://)(\w+)(\.\w{2,3})([a-zA-Z0-9!@#$%^&*-_+()?/]*)"
)

for groups in url_finder.findall(text):
    address = "".join([groups[0], groups[1], groups[2], groups[3], groups[4]])
    matches.append(address)
print("Copied to clipboard:")
print("\n".join(matches))
pyperclip.copy("\n".join(matches))
