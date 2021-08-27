#!/usr/bin/env python3

import sys
from logger import debug, info, warning, error, critical

# Convert string with br formar number to int X 100.
def convert_br_currency_to_int_100(val):
    return round(float(val.replace('.', '').replace(',', '.')) * 100)

# Convert kg string to int grams.
def convert_kg_string_to_int_grams(val):
    return round(float(val.replace('.', '').replace(',', '.')) * 1000)

def get_it_codigo(item):
    it_codigo = item.find('it_codigo').text
    if it_codigo == None or it_codigo == '':
        raise Exception(f'it_codigo: {it_codigo}')
        #  warning(f'Received it_codigo: {it_codigo}')            
        #  print_item(item)
    else:
        it_codigo = it_codigo.strip()
    return it_codigo

def get_desc_item(item):
    desc_item = item.find('desc_item').text.strip()
    if desc_item != None:
        desc_item = desc_item.strip()
    return desc_item

def get_desc_item_ec(item):
    desc_item_ec = item.find('desc_item_ec').text
    if desc_item_ec != None:
        desc_item_ec = desc_item_ec.strip()
    return desc_item_ec

def get_narrativa_ec(item):
    narrativa_ec = item.find('narrativa_ec').text
    if narrativa_ec != None:
        narrativa_ec = narrativa_ec.strip()
    return narrativa_ec

def get_vl_item(item):
    vl_item = item.find('vl_item').text
    #  print(type(vl_item))
    #  print(vl_item)
    if not vl_item == None:
        try:
            # convert int * 100
            vl_item = convert_br_currency_to_int_100(vl_item)
            #  debug(vl_item)
        except:
            raise Exception(f'Could not parse vl_item: {vl_item}') 
    return vl_item

def get_vl_item_sdesc(item):
    vl_item_sdesc = item.find('vl_item_sdesc').text
    #  debug(type(vl_item_sdesc))
    #  debug(vl_item_sdesc)
    if not vl_item_sdesc == None:
        try:
            # convert int * 100
            vl_item_sdesc = convert_br_currency_to_int_100(vl_item_sdesc)
            #  debug(vl_item_sdesc)
        except:
            raise Exception(f'Could not parse vl_item_sdesc: {vl_item_sdesc}') 
    return vl_item_sdesc

def get_vl_ipi(item):
    vl_ipi = item.find('vl_ipi').text
    #  debug(type(vl_ipi))
    #  debug(vl_ipi)
    if not vl_ipi == None:
        try:
            # convert int * 100
            vl_ipi = convert_br_currency_to_int_100(vl_ipi)
            #  debug(vl_ipi)
        except:
            raise Exception(f'Could not parse vl_ipi: {vl_ipi}') 
    return vl_ipi


def get_perc_preco_sugerido_solar(item):
    perc_preco_sugerido_solar = item.find('perc_preco_sugerido_solar').text
    #  debug(perc_preco_sugerido_solar)
    if not perc_preco_sugerido_solar == None:
        try:
            # convert int * 100
            perc_preco_sugerido_solar = convert_br_currency_to_int_100(perc_preco_sugerido_solar)
            #  debug(perc_preco_sugerido_solar)
        except:
            raise Exception(f'Could not parse perc_preco_sugerido_solar: {perc_preco_sugerido_solar}') 
    return perc_preco_sugerido_solar

def get_preco_sugerido(item):
    preco_sugerido = item.find('preco_sugerido').text
    #  debug(preco_sugerido)
    if not preco_sugerido == None:
        try:
            # convert int * 100
            preco_sugerido = convert_br_currency_to_int_100(preco_sugerido)
            #  debug(preco_sugerido)
        except:
            raise Exception(f'Could not parse preco_sugerido: {preco_sugerido}') 
    return preco_sugerido

def get_preco_maximo(item):
    preco_maximo = item.find('preco_maximo').text
    #  debug(preco_maximo)
    if not preco_maximo == None:
        try:
            # convert int * 100
            preco_maximo = convert_br_currency_to_int_100(preco_maximo)
            #  debug(preco_maximo)
        except:
            raise Exception(f'Could not parse preco_maximo: {preco_maximo}') 
    return preco_maximo

def get_categoria(item):
    categoria = item.find('categoria').text
    #  debug(categoria)
    if not categoria == None:
        categoria = categoria.strip()
    return categoria

def get_sub_categoria(item):
    sub_categoria = item.find('sub_categoria').text
    #  debug(sub_categoria)
    if not sub_categoria == None:
        sub_categoria = sub_categoria.strip()
    return sub_categoria

def get_peso(item):
    peso = item.find('peso').text
    #  debug(peso)
    if not peso == None:
        try:
            peso = convert_kg_string_to_int_grams(peso)
            #  debug(peso)
        except:
            raise Exception(f'Could not parse peso: {peso}') 
    return peso

def get_codigo_refer(item):
    codigo_refer = item.find('codigo_refer').text
    #  debug(codigo_refer)
    if not codigo_refer == None:
        codigo_refer = codigo_refer.strip()
    return codigo_refer

def get_fabricante(item):
    fabricante = item.find('fabricante').text
    #  debug(fabricante)
    if not fabricante == None:
        fabricante = fabricante.strip()
    return fabricante

def get_saldos(item):
    saldos = item.find('saldos').text
    #  debug(saldos)
    if not saldos == None:
        saldos = saldos.strip()
        #  debug(saldos)
    return saldos

def get_arquivo_imagem(item):
    # Concat array of url images separated by a non printed character.
    images_arr = []
    arquivo_imagem = item.find('arquivo_imagem')
    for image in arquivo_imagem:
        url_imagem = image.find('arquivo_imagem').text
        #  debug(seq_imagem)
        #  debug(url_imagem)
        if not url_imagem == None:
            images_arr.append(url_imagem.strip())
    images = '\uffff'.join(images_arr)
    #  debug(f'images: {images}')
    return images
