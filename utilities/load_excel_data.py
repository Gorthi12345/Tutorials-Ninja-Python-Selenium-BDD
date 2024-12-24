import openpyxl


def load_data_from_excel(file_path):
    """Loads data from the Excel file into a list of dictionaries."""
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    # Read headers (first row)
    headers = [cell.value for cell in sheet[1]]

    # Read each row after the headers
    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        data.append(dict(zip(headers, row)))

    return data