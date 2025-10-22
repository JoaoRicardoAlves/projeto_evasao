# Faz inicialização do banco, e confere se inicialização foi bem sucedida
import subprocess
from pathlib import Path
import time

ROOT = Path(__file__).parent
DOCKER_COMPOSE_FILES = ["docker-compose.yml", "docker-compose.yaml"]#busca o arquivo contendo as informações para acessar o DB

def start_docker_compose():
    for file_name in DOCKER_COMPOSE_FILES:
        file_path = ROOT / file_name
        if file_path.exists():
            print(f"Iniciando o banco de dados usando {file_name}...")
            subprocess.run(["docker", "compose", "-f", str(file_path), "up", "-d"])
            print("Banco de dados iniciado!")
            return True
    print("Arquivo docker-compose.yml não encontrado na raiz do projeto.")
    return False

if __name__ == "__main__":#Cria função a ser importada no main
    started = start_docker_compose()
    if started:
        print("Aguardando inicialização do banco de dados...")
        time.sleep(5)
        print("Banco de dados deve estar pronto para uso!")
