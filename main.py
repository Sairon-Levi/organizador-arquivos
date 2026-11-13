
import shutil
from pathlib import Path
import sys

caminho = Path(input("Qual pasta deseja organizar?: "))

if caminho.is_absolute():
    diretorio = caminho
else:
    diretorio = Path.home() / caminho

if not diretorio.exists() or not diretorio.is_dir():
    print(f"Pasta não encontrada - {diretorio}")
    sys.exit()

imagens = [
    ".jpg", ".jpeg", ".png", ".gif", ".webp",
    ".bmp", ".svg", ".ico", ".heic"
]

for arquivo in diretorio.iterdir():

    if not arquivo.is_file():
        continue

    extensao = arquivo.suffix.lower()

    if extensao in imagens:
        pasta = "IMAGENS"
    elif not extensao:
        pasta = "OUTROS"
    else:
        pasta = extensao.lstrip(".").upper()

    destino = diretorio / pasta

    # Cria a pasta somente quando necessário
    destino.mkdir(exist_ok=True)

    # Move o arquivo
    shutil.move(str(arquivo), str(destino))

print("Organização concluída com sucesso!")
