import docker, docker.errors as errors

client = docker.from_env()

try:
    output = client.containers.run('python:3.12', 'python3 /testing/script.py', detach=False, volumes=["/home/alex/PycharmProjects/pythonProject4/testing:/testing/"])
except errors.ContainerError as e:
    output = e

print(output)