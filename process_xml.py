#!/usr/bin/env python3

import os
from logger import debug, info, warning, error, critical
import xml.etree.ElementTree as ET
from sqlalchemy.orm import Session
from db import Product, engine

xml_file = os.environ['HANDYTECH_XML']

#  from handytech import HandytechProduct
import handytech
#  import sqlite3

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

# Upsert on db.
def upsert_on_db(root):
    info(f'Processing {len(root)} products')
    with Session(engine) as sess:
        for item in root:
            try:
                product = Product() 
                product.it_codigo = handytech.get_it_codigo(item)
                product.desc_item = handytech.get_desc_item(item)
                product.desc_item_ec = handytech.get_desc_item_ec(item)
                product.narrativa_ec = handytech.get_narrativa_ec(item)
                product.vl_item = handytech.get_vl_item(item)
                product.vl_item_sdesc = handytech.get_vl_item_sdesc(item)
                product.vl_ipi = handytech.get_vl_ipi(item)
                product.perc_preco_sugerido_solar = handytech.get_perc_preco_sugerido_solar(item)
                product.preco_sugerido = handytech.get_preco_sugerido(item)
                product.preco_maximo = handytech.get_preco_maximo(item)
                product.categoria = handytech.get_categoria(item)
                product.sub_categoria = handytech.get_sub_categoria(item)
                product.peso = handytech.get_peso(item)
                product.codigo_refer = handytech.get_codigo_refer(item)
                product.fabricante = handytech.get_fabricante(item)
                product.saldos = handytech.get_saldos(item)
                product.arquivo_imagem = handytech.get_arquivo_imagem(item)
            except Exception as e:
                error(f'Product it_codigo: {product.it_codigo}. {e}')
            #  print(vars(product))
            sess.merge(product)
        sess.commit()

# Print the first item.
#  print_item(root[0])

#  debug(root.tag)
#  print(root[0])
#  print(root[0][0])

#  print_tags(root)
#  print_tag_values(root, 'categoria')
#  print(get_categories(root))
#  print(get_makers(root))

if os.path.exists(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    upsert_on_db(root)
    # Remove file, next will be download.
    os.remove(xml_file)
else:
    info(f'No {xml_file} to be processed')

