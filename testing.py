import docker

client = docker.from_env()

output = client.containers.run('python:3.12', 'python3 /testing/script.py', detach=False, volumes=["/home/alex/PycharmProjects/pythonProject4/testing:/testing/"])

print(output)