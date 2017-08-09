import requests

print("Welcome to TextRemote.")

command = raw_input("Either type in a code or say quit. test sends a test pulse.")
while command != "quit":
	if command = "test":
		command = "code=A90:SONY:12"
	post_data = {"code":command, "pulse":2, "repeat":5, "pass"="admin"}
	send_command = requests.post(url="http://192.168.0.109/msg?code=",post_data)
	print send_command.url
http://xxx.xxx.xxx.xxx:port/msg?code=A90:SONY:12&pulse=2&repeat=5&pass=yourpasszz