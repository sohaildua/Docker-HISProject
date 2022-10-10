import docker
import json

client =docker.from_env()
apiVersion = docker.APIClient
print(client.containers.get("deploytool").attrs)
def login(username, password) :
	try:
		loginData=client.login(userName,password)
		return True
	except 
		docker.errors.APIError as e:
		return False
	count = 0
while True:
	userName = input("Hello! Welcome to Dockerhub! \n\nUsername: ")
	password = input("Password: ")
	val=login(userName, password)
	if val == True:
		tag = input("Enter tag name:")
		repo = input("Enter repo name:")
		message = input("Enter message:")
		author = input("Enter author name:")
		apiVersion.commit(container="deploytool",tag=tag,repository=repo,message=message,author=author)
		break
	else:
		pass