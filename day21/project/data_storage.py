FILEDATA = "iris.csv"


def read_colum(col):
    column_data = []

    with open(FILEDATA) as fo:
        next(fo)
        for line in fo:
            data = line.strip().split(',')
            column_data.append(data[col])

    return column_data
