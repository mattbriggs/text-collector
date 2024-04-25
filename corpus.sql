CREATE TABLE corpus (
    corpus_id TEXT PRIMARY KEY,
    corpus_name TEXT,
    no_words INTEGER,
    doc_count INTEGER
    );

CREATE TABLE document (
    doc_id TEXT PRIMARY KEY,
    corpus_id TEXT,
    doc_path TEXT,
    doc_ext TEXT,
    doc_raw TEXT,
    doc_length INTEGER,
    FOREIGN KEY(corpus_id) REFERENCES corpus(corpus_id)
    );

CREATE TABLE lines (
    doc_id TEXT,
    line_no INTEGER,
    line_text TEXT,
    possent REAL,
    nuesent REAL,
    negsent REAL,
    compsent REAL,
    PRIMARY KEY(doc_id, line_no),
    FOREIGN KEY(doc_id) REFERENCES document(doc_id)
    );

CREATE TABLE body (
    doc_id TEXT PRIMARY KEY,
    body_text TEXT,
    FOREIGN KEY(doc_id) REFERENCES document(doc_id)
    );

CREATE TABLE metadata (
    doc_id TEXT PRIMARY KEY,
    metadata_raw TEXT,
    title TEXT,
    meta_description TEXT,
    author TEXT,
    ms_author TEXT,
    ms_service TEXT,
    ms_topic TEXT,
    ms_date TEXT,
    FOREIGN KEY(doc_id) REFERENCES document(doc_id)
    );