from bs4 import BeautifulSoup
import requests
import sys

number_parameters = len(sys.argv)
if number_parameters < 2:
    print("El parametro del usuario es requerido")
    exit(1)
elif number_parameters > 2:
    print("Tiene demasiados parametros")
    exit(1)

username = sys.argv[1]
# username = "jeirf12"
# username = "Juancarcaicedo"
# username = "MateoK13"

repositories = []
for index in range(1, 3):
    url = f"https://github.com/{username}?page={index}&tab=repositories"

    html = requests.get(url)
    content = html.text

    html_raw = BeautifulSoup(content, "html.parser")
    # print(html_raw.prettify())
    repositories.extend(html_raw.find_all(attrs={ "itemprop": "name codeRepository" }))

for repository in repositories:
    print(f"{repository.get_text()}\t --> https://github.com{repository.get("href")}")

