import argparse
import sys

from bs4 import BeautifulSoup


def reverse_html_table(html_file: str, identifier_string, output_file=None,
                       has_header=True):
    # Read the HTML file
    with open(html_file, 'r', encoding='utf-8') as file:
        content = file.read()

    if output_file is None:
        output_file = html_file.replace('.html', '.out.html')

    soup = BeautifulSoup(content, 'html.parser')

    # Search for tables based on the identifier string
    tables_found = [table for table in soup.find_all('table') if
                    identifier_string in table.get_text(strip=True)]

    # Ensure only one table is found
    if len(tables_found) == 0:
        print("ERROR: No table found with the specified identifier string:", identifier_string)
        sys.exit(1)
    elif len(tables_found) > 1:
        print("ERROR: More than one table found with the specified identifier string:", identifier_string)
        sys.exit(2)

    # Proceed with the single found table
    table_found = tables_found[0]

    # Extract header row if present
    header = []
    if has_header:
        header_row = table_found.find('tr')
        if header_row:
            header = [td.get_text(strip=True) for td in
                      header_row.find_all(['th', 'td'])]

    # Reverse the rows within the selected table
    rows = []
    for tr in table_found.find_all('tr')[
              1 if has_header else 0:]:  # Skip header row if present
        cells = [td.get_text(strip=True) for td in tr.find_all(['th', 'td'])]
        rows.append(cells)

    # Reverse the order of rows
    rows = rows[::-1]

    # Replace the content of the table with the reversed rows
    table_found.clear()  # Clear table content
    if has_header:
        # Add header row back if present
        header_row = soup.new_tag('tr')
        for cell in header:
            th = soup.new_tag('th')
            th.string = cell
            header_row.append(th)
        table_found.append(header_row)
    for row in rows:
        tr = soup.new_tag('tr')
        for cell in row:
            td = soup.new_tag('td')
            td.string = cell
            tr.append(td)
        table_found.append(tr)

    # Save the modified HTML content to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(soup.prettify())

    print(f"reverse_html_table({html_file}, {identifier_string}, {output_file})")


def main():
    parser = argparse.ArgumentParser(
        description="Reverse table rows in a HTML file based on identifier "
                    "string.")
    parser.add_argument("input_file", help="Input HTML file path")
    parser.add_argument("identifier_string",
                        help="Identifier string to locate the table")
    parser.add_argument("output_file", help="Output HTML file path")
    parser.add_argument("--no-header", action="store_false", dest="has_header",
                        help="Specify if the table has no header")
    args = parser.parse_args()

    reverse_html_table(args.input_file, args.identifier_string,
                       args.output_file, args.has_header)


if __name__ == "__main__":
    main()
