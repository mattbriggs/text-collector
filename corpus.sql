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
    doc_text LONGTEXT,
    doc_raw LONGTEXT,
    doc_length INTEGER,
    FOREIGN KEY(corpus_id) REFERENCES corpus(corpus_id)
    );