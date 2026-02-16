# Type Content here...

n = int(input())
Dict = dict()

for i in range(n):
	cmd = input().split(" ")
	if cmd[0] == "ADD":
		Dict[cmd[1]] = cmd[2]
	elif cmd[0] == "REMOVE":
		Dict.pop(cmd[1], " ")
	elif cmd[0] == "DISPLAY":
		keys = list(Dict.keys())
		keys.sort()
		for i in keys:
			print(f"{i}: {Dict[i]}")
		if not len(keys):
			print("No contacts")
	