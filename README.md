# Text collector
v.0.0.1 | Matt Briggs

Text collector uses parallel processes to scan specified file folders to load a SQL database with the text. Includes handling for markdown files and yaml files.

This system is designed to collect and process data from various files, storing the processed information in a SQLite database. It consists of three main components: a script to run the collector, the PageProcessor class for handling file processing, and the Collector module for orchestrating the collection and processing flow.

## Getting Started

These instructions will guide you on how to set up and run the Data Collector System on your local machine.

### Prerequisites

- Python 3.x
- SQLite3
- Required Python packages:
  - `pyyaml` for YAML file processing.
  - Any other packages your environment might need.

### Installation

1. Ensure Python and SQLite3 are installed on your system.
2. Install the required Python packages:

```bash
pip -r requirements.txt
```

3. Clone this repository or download the scripts and place them in your project directory.

### Configuration

Before running the collector, you need to set up the `config.yml` file according to your environment:

```yaml
dbname: "path_to_your_database/corpus.db"
corpora:
  - name: "corpus_name"
    path: "path_to_your_files"
```

Ensure the `dbname` and `corpora` paths are correctly set to point to your SQLite database and the directories containing the files you wish to process.

### Running the Collector

To start the data collection and processing, navigate to your project directory and run:

```bash
python run_collector.py
```

`run_collector.py` is the main script that initializes the Collector, processes the specified files, and stores the results in the database.

## Components

### PageProcessor

The `PageProcessor` class is responsible for processing individual files. It reads files, extracts the necessary information, and interacts with the SQLite database to store processed data.

### Collector

The `Collector` module orchestrates the data collection process. It retrieves configuration settings, initializes the database, collects file paths for processing, and manages the multithreaded processing of files.

## Text Miner

You can use [Text Miner](https://github.com/mattbriggs/text-miner) to create text analysis workloads using Text Collector.

Text Miner is a Python application designed to process a text corpus stored in a SQLite database. The application extracts data from a database that contains corpus, generates summaries, and identifies the top fifty terms within the documents. The tool is useful for quick content analysis and data extraction from large text collections.