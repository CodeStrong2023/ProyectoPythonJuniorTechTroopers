from enum import Enum

# Utilizamos enums para crear enumeraciones, así tenemos mejor legibilidad en el código y menor riesgo de equivocación
class Location(Enum):
# Clase Location que contiene las provincias y 10 ciudades
# Definimos las provincias argentinas como miembros de la clase Enum

#Provincias Argentinas
    BUENOS_AIRES = "Buenos Aires"
    CATAMARCA = "Catamarca"
    CHACO = "Chaco"
    CHUBUT = "Chubut"
    CORDOBA = "Cordoba"
    CORRIENTES = "Corrientes"
    ENTRE_RIOS = "Entre Rios"
    FORMOSA = "Formosa"
    JUJUY = "Jujuy"
    LA_PAMPA = "La Pampa"
    LA_RIOJA = "La Rioja"
    MENDOZA = "Mendoza"
    MISIONES = "Misiones"
    NEUQUEN = "Neuquen"
    RIO_NEGRO = "Rio Negro"
    SALTA = "Salta"
    SAN_JUAN = "San Juan"
    SAN_LUIS = "San Luis"
    SANTA_CRUZ = "Santa Cruz"
    SANTA_FE = "Santa Fe"
    SANTIAGO_DEL_ESTERO = "Santiago del Estero"
    TIERRA_DEL_FUEGO = "Tierra del Fuego"
    TUCUMAN = "Tucuman"

#Ciudades de Argentina
    MAR_DEL_PLATA = "Mar del Plata"
    ROSARIO = "Rosario"
    CARLOS_PAZ = "Carlos Paz"
    SAN_RAFAEL = "San_Rafael"
    PUERTO_MADRYN = "Puerto Madryn"
    PANAMA = "Panama"
    USHUAIA = "Ushuaia"
    MERLO = "Merlo"
    SAN_MARTIN_DE_LOS_ANDES= "San Martin de los Andes"
    BARILOCHE = "Bariloche"
