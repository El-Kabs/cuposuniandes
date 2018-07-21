import requests
import json
from flask import Flask

app = Flask(__name__)

@app.route("/<materiaS>")
def get(materiaS):
    headers = {'Referer': 'https://registroapps.uniandes.edu.co/oferta_cursos/index.php'}
    materia = materiaS.split('-')[0]
    codigo = materiaS.split('-')[1]
    req = requests.get('https://registroapps.uniandes.edu.co/oferta_cursos/api/get_courses.php?term=201820&ptrm=1&prefix='+str(materia)+'&campus=&attr=&attrs=', headers=headers)
    jsonP = json.loads(req.text)
    retornar = {"records": []}
    for x in jsonP['records']:
        if(x['course'] == codigo):
            retorno = {}
            retorno['section'] = x['section']
            retorno['registered'] = x['registered']
            retorno['empty'] = x['empty']
            retornar["records"].append(retorno)
    req = requests.get('https://registroapps.uniandes.edu.co/oferta_cursos/api/get_courses.php?term=201820&ptrm=8A&prefix='+str(materia)+'&campus=&attr=&attrs=', headers=headers)
    jsonP = json.loads(req.text)
    for x in jsonP['records']:
        if(x['course'] == codigo):
            retorno = {}
            retorno['section'] = x['section']
            retorno['registered'] = x['registered']
            retorno['empty'] = x['empty']
            retornar["records"].append(retorno)
    req = requests.get('https://registroapps.uniandes.edu.co/oferta_cursos/api/get_courses.php?term=201820&ptrm=8B&prefix='+str(materia)+'&campus=&attr=&attrs=', headers=headers)
    jsonP = json.loads(req.text)
    for x in jsonP['records']:
        if(x['course'] == codigo):
            retorno = {}
            retorno['section'] = x['section']
            retorno['registered'] = x['registered']
            retorno['empty'] = x['empty']
            retornar["records"].append(retorno)
    return json.dumps(retornar)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=$PORT)


