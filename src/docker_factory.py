import docker


def create_docker_client(docker_image: str, docker_command: str, file_path: str):
    client = docker.from_env()

    client.containers.run(
        docker_image,
        docker_command,
        detach=False,
        volumes=[file_path + ":/testing/"],
        stderr=True,
        stdout=True,
        isolation='default'
    )