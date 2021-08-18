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

# Convert kg string to int grams.
def convert_kg_string_to_int_grams(val):
    return round(float(val.replace('.', '').replace(',', '.')) * 1000)

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
                # convert int * 100
                vl_item = convert_br_currency_to_int_100(vl_item)
                #  debug(vl_item)
            except:
                error(f'Parsing vl_item: {vl_item}, it_codigo: {it_codigo}') 
                next

        # vl_item_sdesc.
        vl_item_sdesc = item.find('vl_item_sdesc').text
        #  debug(type(vl_item_sdesc))
        #  debug(vl_item_sdesc)
        if not vl_item_sdesc == None:
            try:
                # convert int * 100
                vl_item_sdesc = convert_br_currency_to_int_100(vl_item_sdesc)
                #  debug(vl_item_sdesc)
            except:
                error(f'Parsing vl_item_sdesc: {vl_item_sdesc}, it_codigo: {it_codigo}') 
                next

        # vl_ipi.
        vl_ipi = item.find('vl_ipi').text
        #  debug(type(vl_ipi))
        #  debug(vl_ipi)
        if not vl_ipi == None:
            try:
                # convert int * 100
                vl_ipi = convert_br_currency_to_int_100(vl_ipi)
                #  debug(vl_ipi)
            except:
                error(f'Parsing vl_ipi: {vl_ipi}, it_codigo: {it_codigo}') 
                next

        # perc_preco_sugerido_solar.
        perc_preco_sugerido_solar = item.find('perc_preco_sugerido_solar').text
        #  debug(perc_preco_sugerido_solar)
        if not perc_preco_sugerido_solar == None:
            try:
                # convert int * 100
                perc_preco_sugerido_solar = convert_br_currency_to_int_100(perc_preco_sugerido_solar)
                #  debug(perc_preco_sugerido_solar)
            except:
                error(f'Parsing perc_preco_sugerido_solar: {perc_preco_sugerido_solar}, it_codigo: {it_codigo}') 
                next

        # preco_sugerido.
        preco_sugerido = item.find('preco_sugerido').text
        #  debug(preco_sugerido)
        if not preco_sugerido == None:
            try:
                # convert int * 100
                preco_sugerido = convert_br_currency_to_int_100(preco_sugerido)
                #  debug(preco_sugerido)
            except:
                error(f'Parsing preco_sugerido: {preco_sugerido}, it_codigo: {it_codigo}') 
                next

        # preco_maximo.
        preco_maximo = item.find('preco_maximo').text
        #  debug(preco_maximo)
        if not preco_maximo == None:
            try:
                # convert int * 100
                preco_maximo = convert_br_currency_to_int_100(preco_maximo)
                #  debug(preco_maximo)
            except:
                error(f'Parsing preco_maximo: {preco_maximo}, it_codigo: {it_codigo}') 
                next

        # categoria.
        categoria = item.find('categoria').text
        #  debug(categoria)
        if not categoria == None:
            categoria = categoria.strip()

        # sub_categoria.
        sub_categoria = item.find('sub_categoria').text
        #  debug(sub_categoria)
        if not sub_categoria == None:
            sub_categoria = sub_categoria.strip()

        # peso.
        peso = item.find('peso').text
        #  debug(peso)
        if not peso == None:
            try:
                peso = convert_kg_string_to_int_grams(peso)
                #  debug(peso)
            except:
                error(f'Parsing peso: {peso}, it_codigo: {it_codigo}') 
                next

        # codigo_refer.
        codigo_refer = item.find('codigo_refer').text
        #  debug(codigo_refer)
        if not codigo_refer == None:
            codigo_refer = codigo_refer.strip()

        # fabricante.
        fabricante = item.find('fabricante').text
        #  debug(fabricante)
        if not fabricante == None:
            fabricante = fabricante.strip()

        # saldos.
        saldos = item.find('saldos').text
        #  debug(saldos)
        if not saldos == None:
            saldos = saldos.strip()
            #  debug(saldos)

        # arquivo_imagem.
        arquivo_imagem = item.find('arquivo_imagem')
        for im in arquivo_imagem:
            #  seq_imagem = im.find('seq_imagem').text
            url_imagem = im.find('arquivo_imagem').text
            #  debug(seq_imagem)
            debug(url_imagem)
            #  if not arquivo_imagem == None:
                #  arquivo_imagem = arquivo_imagem.strip()
                #  debug(arquivo_imagem)
       

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


upsert_on_db(root)


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



