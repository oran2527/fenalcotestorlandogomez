import pandas
import json
import sys

# arreglo con los datos finales del archivo txt
txt_data = []

# extrae informacion de archivo de excel
#excel_data_df = pandas.read_excel('archivo_a_transformar.xlsx')
excel_data_df = pandas.read_excel(sys.argv[1])
json_str = excel_data_df.to_json()

# convertir string a diccionario
dict_json_str = json.loads(json_str)

# extrae informacion del archivo json con las reglas
with open("reglas.json") as reglas:
    datos_reglas = json.load(reglas)

# extraccion en variables de las regla anio
anio_json_type = datos_reglas[0]['tipo']
anio_json_size = int(datos_reglas[0]['TAMANO'])

# extraccion en variables de las regla concepto
concepto_json_type = datos_reglas[1]['tipo']
concepto_json_size = int(datos_reglas[1]['TAMANO'])

# extraccion en variables de las regla valor
valor_json_type = datos_reglas[2]['tipo']
valor_json_size = int(datos_reglas[2]['TAMANO'])

for i in range(0, len(dict_json_str['ANIO']), 1):
    anio_txt = ''
    concepto_txt = ''
    valor_txt = ''
    
    if(str(dict_json_str['ANIO'][str(i)]) == 'NaN' or str(dict_json_str['ANIO'][str(i)]) == 'None'):
        anio_txt = ''        
    elif(len(str(dict_json_str['ANIO'][str(i)])) < anio_json_size):
        anio_txt = ('0' * (anio_json_size - len(str(int(dict_json_str['ANIO'][str(i)]))))) + str(int(dict_json_str['ANIO'][str(i)]))
    else:
        anio_txt = str(int(dict_json_str['ANIO'][str(i)]))

    if(str(dict_json_str['CONCEPTO'][str(i)]) == 'NaN' or str(dict_json_str['CONCEPTO'][str(i)]) == 'None'):
        concepto_txt = ''
    elif(len(str(dict_json_str['CONCEPTO'][str(i)])) < concepto_json_size):
        concepto_txt = str(dict_json_str['CONCEPTO'][str(i)]) + ('$' * (concepto_json_size - len(str(dict_json_str['CONCEPTO'][str(i)]))))
    else:
        concepto_txt = str(dict_json_str['CONCEPTO'][str(i)])
    
    if(str(dict_json_str['VALOR'][str(i)]) == 'NaN' or str(dict_json_str['VALOR'][str(i)]) == 'None'):
        valor_txt = ''
    elif(len(str(int(dict_json_str['VALOR'][str(i)]))) < valor_json_size):
        valor_txt = ('0' * (valor_json_size - len(str(int(dict_json_str['VALOR'][str(i)]))))) + str(int(dict_json_str['VALOR'][str(i)]))
    else:
        valor_txt = str(int(dict_json_str['VALOR'][str(i)]))
    
    # se añade cada concatenacion al array final
    txt_data.append(anio_txt + concepto_txt + valor_txt)

# se abre archivo txt para escribir la informacion del array
with open(sys.argv[2], 'wt') as final_text:
    for n in txt_data:
        final_text.write(n + '\n') 