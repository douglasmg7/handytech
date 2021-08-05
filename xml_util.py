#!/usr/bin/env python
import os
from logger import debug, info, warning, error, critical
import xml.etree.ElementTree as ET

# Print first item example.
def print_first_elem(root):
    for el in root[0]:
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


       

tree = ET.parse(os.environ['HANDYTECH_XML'])
root = tree.getroot()

#  debug(root.tag)
#  print(root[0])
#  print(root[0][0])

#  print_tags(root)
#  print_first_elem(root)
#  print_tag_values(root, 'categoria')
print(get_categories(root))
print(get_makers(root))


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



