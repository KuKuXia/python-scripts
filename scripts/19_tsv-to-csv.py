import csv


# import os


def convert_tsv_to_csv(input, out):
    # if os.path.exists(out):
    # raise ValueError("Output file already exists")

    reader = csv.reader(open(input, 'rU'), dialect=csv.excel_tab)
    writer = csv.writer(open(out, "w+"), dialect="excel")
    for row in reader:
        writer.writerow(row)


def convert_csv_to_tsv(input, out):
    # if os.path.exists(out):
    # raise ValueError("Output file already exists")

    reader = csv.reader(open(input, 'rU'), dialect='excel')
    writer = csv.writer(open(out, "w+"), dialect=csv.excel_tab)

    for row in reader:
        writer.writerow(row)


if __name__ == "__main__":
    csv_file = './data/sample_csv-1.csv'
    tsv_file = './data/csv_dmo.tsv'

    convert_csv_to_tsv(csv_file, tsv_file)
    print('csv to tsv, Done')

    convert_tsv_to_csv(tsv_file, csv_file)
    print('tsv to csv, Done')
