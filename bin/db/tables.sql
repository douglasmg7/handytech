-- drop table if exists entrance;
-- enable foreign keys
-- not working, reset to off when back to db
pragma foreign_keys = on;

-- Products.
CREATE TABLE IF NOT EXISTS product (
    zunka_product_id    TEXT DEFAULT "",
    it_codigo                   TEXT NULL UNIQUE,
    desc_item                   TEXT NOT NULL,
    desc_item_ec                TEXT NOT NULL,
    narrativa_ec                TEXT NOT NULL,
    vl_item                     INTEGER NOT NULL,
    vl_item_sdesc               INTEGER NOT NULL,
    vl_ipi                      INTEGER NOT NULL,
    perc_preco_sugerido_solar   INTEGER NOT NULL,
    preco_sugerido              INTEGER NOT NULL,
    preco_maximo                INTEGER NOT NULL,
    categoria                   TEXT NOT NULL,
    sub_categoria               TEXT NOT NULL,
    peso                        INTEGER NOT NULL,
    codigo_refer                TEXT NOT NULL,
    fabricante                  TEXT NOT NULL,
    saldos                      INTEGER NOT NULL,
    arquivo_imagem              TEXT NOT NULL,
    timestamp                   DATE NOT NULL,
    created_at                  DATE NOT NULL,
    changed_at                  DATE NOT NULL,
    checked_at                  DATE DEFAULT "0001-01-01T03:00:00-03:00",
    removed_at                  DATE DEFAULT "0001-01-01T03:00:00-03:00"
);
CREATE UNIQUE INDEX IF NOT EXISTS idx_product_code ON product(it_codigo);

-- Products history.
CREATE TABLE IF NOT EXISTS product_history (
    zunka_product_id		    TEXT DEFAULT "",
    it_codigo                   TEXT NULL UNIQUE,
    desc_item                   TEXT NOT NULL,
    desc_item_ec                TEXT NOT NULL,
    narrativa_ec                TEXT NOT NULL,
    vl_item                     INTEGER NOT NULL,
    vl_item_sdesc               INTEGER NOT NULL,
    vl_ipi                      INTEGER NOT NULL,
    perc_preco_sugerido_solar   INTEGER NOT NULL,
    preco_sugerido              INTEGER NOT NULL,
    preco_maximo                INTEGER NOT NULL,
    categoria                   TEXT NOT NULL,
    sub_categoria               TEXT NOT NULL,
    peso                        INTEGER NOT NULL,
    codigo_refer                TEXT NOT NULL,
    fabricante                  TEXT NOT NULL,
    saldos                      INTEGER NOT NULL,
    arquivo_imagem              TEXT NOT NULL,
    timestamp                   DATE NOT NULL,
    created_at                  DATE NOT NULL,
    changed_at                  DATE NOT NULL,
    checked_at                  DATE DEFAULT "0001-01-01T03:00:00-03:00",
    removed_at                  DATE DEFAULT "0001-01-01T03:00:00-03:00",
    UNIQUE (it_codigo, changed_at)
);
CREATE UNIQUE INDEX IF NOT EXISTS idx_product_history_code_changed_at ON product_history(it_codigo, changed_at);
