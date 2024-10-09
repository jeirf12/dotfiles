import subprocess
import json
import sys
from datetime import datetime

if len(sys.argv) == 2:
    url = f"https://api.github.com/repos/{sys.argv[-1]}"
    status = subprocess.getstatusoutput(f"gh api {url}")
    if status[0] == 0:
        content = subprocess.check_output(f"gh api {url}", stderr=subprocess.STDOUT, shell=True)
        json_content = json.loads(content)

        print(f"El ultimo commit fue subido en la fecha... {datetime.strptime(json_content['pushed_at'], "%Y-%m-%dT%H:%M:%SZ")}")
    else:
        print("Repositorio no encontrado...")

else:
    print("Ingrese la url del repositorio como la siguiente:\n\n\tpython consult_repo.py \"{nameAccount}/{nameRepository}\"")
    print("Ejemplo:\n\n\tpython consult_repo.py \"pepitoperez/frontend\"")
