#!/usr/bin/env python
import os
from logger import debug, info, warning, error, critical
import xml.etree.ElementTree as ET
import sqlite3

DB_FILE = os.environ['HANDYTECH_DB']
#  debug(f'Db file: {DB_FILE}')
#  conn = sqlite3.connect(DB_FILE)
#  debug(conn.total_changes)

# Print first item example.
def print_item(item):
    for el in item:
        print(f'{el.tag} - {el.text}')

# Print tags.
def print_tags(root):
    for el in root[0]:
        print(el.tag)

# Print all of the same tag.
def print_tag_values(root, tag):
    values = set()
    for el in root:
        #  print(el.find(tag).text)
        values.add(el.find(tag).text)
    print(values)

# Get categories.
def get_categories(root):
    values = set()
    for el in root:
        values.add(el.find('categoria').text)
    return sorted(values)

# Get makers.
def get_makers(root):
    values = set()
    for el in root:
        values.add(el.find('fabricante').text)
    return sorted(values)

# Convert string with br formar number to int X 100.
def convert_br_currency_to_int_100(val):
    return round(float(val.replace('.', '').replace(',', '.')) * 100)

# Upsert on db..
def upsert_on_db(root):
    for item in root:

        # it_codigo.
        it_codigo = item.find('it_codigo').text
        if it_codigo == None or it_codigo == '':
            warning(f'Received it_codigo: {it_codigo}')            
            print_item(item)
            next
        else:
            it_codigo = it_codigo.strip()

        # desc_item.
        desc_item = item.find('desc_item').text.strip()
        if desc_item != None:
            desc_item = desc_item.strip()

        # desc_item_ec.
        desc_item_ec = item.find('desc_item_ec').text
        if desc_item_ec != None:
            desc_item_ec = desc_item_ec.strip()

        # narrativa_ec.
        narrativa_ec = item.find('narrativa_ec').text
        if narrativa_ec != None:
            narrativa_ec = narrativa_ec.strip()

        # vl_item.
        vl_item = item.find('vl_item').text
        #  print(type(vl_item))
        #  print(vl_item)
        if not vl_item == None:
            try:
                # convert br decimal string to
                vl_item = int(float(vl_item.replace('.', '').replace(',', '.')) * 100)
                print(vl_item)
            except:
                error(f'Parsing vl_item: {vl_item}, it_codigo: {it_codigo}') 
                next

#  vl_item
#  vl_item_sdesc
#  vl_ipi
#  perc_preco_sugerido_solar
#  preco_sugerido
#  preco_maximo
#  categoria
#  sub_categoria
#  peso
#  codigo_refer
#  fabricante
#  saldos
#  arquivo_imagem

       

tree = ET.parse(os.environ['HANDYTECH_XML'])
root = tree.getroot()

# Print the first item.
#  print_item(root[0])

#  debug(root.tag)
#  print(root[0])
#  print(root[0][0])

#  print_tags(root)
#  print_tag_values(root, 'categoria')
#  print(get_categories(root))
#  print(get_makers(root))


#  upsert_on_db(root)


#  it_codigo
#  desc_item
#  desc_item_ec
#  narrativa_ec
#  vl_item
#  vl_item_sdesc
#  vl_ipi
#  perc_preco_sugerido_solar
#  preco_sugerido
#  preco_maximo
#  categoria
#  sub_categoria
#  peso
#  codigo_refer
#  fabricante
#  saldos
#  arquivo_imagem



