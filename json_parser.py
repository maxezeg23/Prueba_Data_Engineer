import json
from datetime import datetime

# extrae la informacion de constitucion de una empresa del JSON 
def extraer_informacion_constitucion(json_data):
    """
    Esta función recorre el JSON y extrae la información de constitución
    de la empresa, fecha, objeto social, domicilio y capital

    :param json_data: Diccionario para el JSON del acto
    :return: JSON con la información estructurada
    """
    # crear un diccionario para guardar la informacion extraida
    resultado = {
        "id": json_data["_id"],
        "row": []
    }
    
    # recorre los value que tenga datos de constitucion
    for item in json_data["row"][0]["value"]:
        # estrea clave-valor 
        clave = item["key"]
        valor = item["value"]
        # los adiciona al resultado
        resultado["row"].append({
            "key": clave,
            "value": valor
        })
    
    # añade la info adicional al resultado
    resultado["header_RAW"] = json_data["header_RAW"]
    resultado["company_RAW"] = json_data["company_RAW"]
    
    return resultado

# valida y normaliza las fechas de constitucion
def normalizar_fecha(fecha_str):
    """
    esta funcion valida y normaliza las fechas de constitucion para que todas tengan el formato YYYY-MM-DD

    :param fecha_str: fecha de constitucion en cualquier formato
    :return: fecha de constituciion en formato YYYY-MM-DD
    """
    # parsea la fecha, asume el formato 'd.m.y' en base al ejemplo 
    try:
        fecha_normalizada = datetime.strptime(fecha_str, '%d.%m.%y').date()
    except ValueError as e:
        # si hay un error en la transformacion de fecha hacer un print y devolver null 
        print(f"Error al convertir la fecha: {e}")
        return None
    
    # devolver la fecha en el formato necesitado
    return fecha_normalizada.strftime('%Y-%m-%d')

json_ejemplo = {
 "_id": "XXXX",
 "row": [
 {
 "key": "Constitución",
 "value": [
 {
 "key": "Comienzo de operaciones",
 "value": "7.07.21"
 },
 {
 "key": "Objeto social",
 "value": "La explotación de todo tipo de cafeterias, bares , restaurantes, hoteles, terrazas y otros establecimientos de hosteleria"
 },
 {
 "key": "Domicilio",
 "value": "C/ LEON 31 (MADRID)"
 },
 {
 "key": "Capital",
 "value": "3.010,00 Euros"
 }
 ]
 }
 ],
 "header_RAW": "366623",
 "company_RAW": "GRUPO MEXCALISTA SL"
}

# ejecutar con el ejemplo
informacion_constitucion = extraer_informacion_constitucion(json_ejemplo)

# suponiendo que la fecha de comienzo de operaciones se encuentra en el segundo elemento de "value"
fecha_constitucion_raw = informacion_constitucion['row'][0]['value']
fecha_constitucion_normalizada = normalizar_fecha(fecha_constitucion_raw)

# mostrar el resultado y la fecha normalizada
informacion_constitucion, fecha_constitucion_normalizada
