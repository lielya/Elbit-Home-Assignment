from flask import Flask
import docker

app = Flask(__name__)

@app.route('/')
def containers():
    client = docker.from_env()
    containers = client.containers.list(all=True)
    return [c.name for c in containers]

if __name__ == '__main__':
    app.run()
