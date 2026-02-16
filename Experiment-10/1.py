# Type Content here...

string = input()
new_string = ""

for i in string:
	if i.isalnum() or i == " ":
		new_string += i

print(new_string)
