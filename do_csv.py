import csv
import config
import utils

headers = ['StartsWith', 'TranslateTo', 'Category', 'Remove']
lookup_names = []
lookup_names_dirty = False

# Important fields from transaction file:
name_field = 'CreditorName'
name_field_alt = 'PurposeDescription'
acc_num_field = 'CreditorAccountNumber'


def process_transaction_file():
    transactions = []
    transactions_dirty = False

    # Mobi CSV export file is UTF-8 with BOM signature
    with open(config.input_file, 'r', encoding='utf-8-sig') as theFile:
        reader = csv.DictReader(theFile)
        fields = list(reader.fieldnames)    # converting sequence to list
        for line in reader:
            line['Category'] = config.default_cat
            matched, replace_with, new_category, remove = check_names(line)
            if matched:
                line[name_field] = replace_with
                line['Category'] = new_category
                transactions_dirty = True
            if not remove:
                transactions.append(line)

    if transactions_dirty:
        write_transactions(transactions, fields)

    return transactions


def write_transactions(transactions, fields):
    # Adding newly created field
    fields.append('Category')

    # Excel hack
    text_encoding = "utf-8"
    if config.excel_bom:
        text_encoding = "utf-8-sig"

    with open(config.out_file, 'w', newline='', encoding=text_encoding) as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields, quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for item in transactions:
            # Another Excel hack, to prevent text data treated as numbers
            if config.excel_columns:
                for column in config.excel_columns:
                    if item[column]:
                        item[column] = '="' + item[column] + '"'
            writer.writerow(item)


def check_names(curr_line):
    global lookup_names, lookup_names_dirty

    search_key = curr_line[name_field]
    if not search_key:
        search_key = curr_line[name_field_alt]

    search_key_clean = search_key.lower().strip()
    found = False
    translate_to = None
    category = None
    remove = False

    for item in lookup_names:
        item_clean = item[headers[0]].lower().strip()
        if search_key_clean.startswith(item_clean):
            found = True
            translate_to = item[headers[1]]
            category = item[headers[2]]
            remove = (item[headers[3]].upper() == 'TRUE')

    if not found:
        lookup_names.append({headers[0]: search_key, headers[1]: search_key, headers[2]: config.default_cat,
                             headers[3]: 'FALSE'})
        lookup_names_dirty = True

    return found, translate_to, category, remove


def read_names():
    global lookup_names

    if not utils.file_exists(config.lookup_names):
        return

    with open(config.lookup_names, 'r', encoding='utf-8-sig') as theFile:
        reader = csv.DictReader(theFile)
        for line in reader:
            lookup_names.append(line)


def write_names():
    global lookup_names, headers

    with open(config.lookup_names, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers, quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for item in lookup_names:
            writer.writerow(item)
