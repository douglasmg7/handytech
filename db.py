#!/usr/bin/env python3

import os
import datetime
from logger import debug, info, warning, error, critical

from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String, DateTime
#  from sqlalchemy.orm import registry
from sqlalchemy.orm import declarative_base, Session

DB_FILE = os.environ['HANDYTECH_DB']
#  debug(f'Db file: {DB_FILE}')
engine = create_engine(f'sqlite+pysqlite:///{DB_FILE}', echo=False, future=True)
Base = declarative_base()
session = Session(engine)

class Product(Base):
    __tablename__ = 'product'
    zunka_product_id = Column(String)
    it_codigo = Column(String, primary_key=True)
    desc_item = Column(String)
    desc_item_ec = Column(String)
    narrativa_ec = Column(String)
    vl_item = Column(Integer)
    vl_item_sdesc = Column(Integer)
    vl_ipi = Column(Integer)
    perc_preco_sugerido_solar = Column(Integer)
    preco_sugerido = Column(Integer)
    preco_maximo = Column(Integer)
    categoria = Column(String)
    sub_categoria = Column(String)
    peso = Column(Integer)
    codigo_refer = Column(String)
    fabricante = Column(String)
    saldos = Column(Integer)
    arquivo_imagem = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

#  product = Product(it_code='qwe', desc_item='asdf asdf ', vl_item=123)
#  session.add(product)
#  session.commit()

#  product = session.get(Product, 'qwe')
#  print(vars(product))

# Create db.
if not os.path.exists(DB_FILE):
    Base.metadata.create_all(engine)
    #  Base.metadata.drop_all()
