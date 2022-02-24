

def get_from_file(matrix, column, accuracy):
    print("Введите путь к файлу:")
    path = input()
    try:
        file = open(path, "r")
        text = file.read()
    except FileNotFoundError:
        print("Нет такого файла")
        return
    text = text.replace(',', '.')
    rows = text.split("\n")
    rowsCnt = int(rows[0])
    for i in range(rowsCnt):
        matrix.append([])
        for j in range(rowsCnt):
            matrix[i].append(0)
    for i in range(1, rowsCnt + 1):
        rows[i] = rows[i].split(' ')
    try:
        for i in range(rowsCnt):
            for j in range(rowsCnt):
                matrix[i][j] = float(rows[i+1][j])
        for i in range(1, rowsCnt):
            column.append(float(rows[i][rowsCnt]))
    except ValueError:
        print("Ошибка обработки файла")
        return
    print("Введите желаемую точность:")
    accuracy = float(input());