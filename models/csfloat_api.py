import requests

def obtener_precio_skin(nombre_skin):
    url = f'https://csfloat.com/api/v1/listings?search={nombre_skin}'
    headers = {
        'Authorization': 'HE7cXSg8PL_MZwVmP476PcD5mMbl5-4x',  # Clave personal de la API de CsFloat
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        datos = response.json()
        return datos
    else:
        print(f'Error en la API: {response.status_code} - {response.text}')
        return None

