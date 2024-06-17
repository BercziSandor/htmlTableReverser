# HtmlTableTools

`HtmlTableTools` is a Python utility with many functions. 
It can:
- `reverse` the rows of an HTML table based on a specified identifier string within the table's content.

## Features

- **Reverse Table Rows:** Reverse the order of rows in an HTML table.
- **Identifier String:** Specify a string to locate the table within the HTML file.
- **Optional Header Handling:** Support for tables with or without a header row.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/BercziSandor/htmlTableReverser.git
```


2. Install dependencies using Poetry:
_In case Poetry is not available:__
```bash
curl -sSL https://install.python-poetry.org | python -
```


```bash
cd htmlTableReverser
poetry install
```



## Usage

To reverse the rows of a table in an HTML file:

```bash
poetry run python html_table_reverser.py input_file.html identifier_string output_file.html [--no-header]
```
- `input_file.html`: Path to the input HTML file containing the table.
- `identifier_string`: String to identify the table within the HTML content.
- `output_file.html`: Path to save the modified HTML with reversed table rows.
- `--no-header`: Optional flag to indicate that the table has no header row.


### Examples

Reverse rows of a table with a header:
```bash
poetry run python html_table_reverser.py sample.html "Table 1" output.html
```
Reverse rows of a table without a header:
```bash
poetry run python html_table_reverser.py sample.html "Table 2" output.html --no-header
```

