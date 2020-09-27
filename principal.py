
import requests
import csv
def cargarDatos():
    url = 'http://saludata.saludcapital.gov.co/osb/datos_abiertos_osb/enf-transmisibles/OSB_EnfTransm-COVID-19.csv'
    myfile = requests.get(url)
    open('datos.csv', 'wb').write(myfile.content)
def leerDatos():
    with open('datos.csv', newline='') as File:  
        reader = csv.reader(File)
        for row in reader:
            print(row)
cargarDatos()
leerDatos()