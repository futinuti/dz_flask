def format_text(text: list):

    t = []
    for i in range(len(text)):
        n_text = '<h3>' + str(i+1) + '.  ' + text[i] + '</h3>'
        t.append(n_text)
    text = ('' .join(t))

    return text


def get_avr_data(file):
    sum_height = 0
    sum_weight = 0
    count = 0
    for lines in file[1::]:
        line = lines.replace(',', '').rstrip('\n')
        line = line.split(' ')
        if line[0] != "":
            sum_height += float(line[1])
            sum_weight += float(line[2])
            count += 1

    return sum_weight / count, sum_height / count


def set_sm(a):
    return a * 2.54


def set_kg(a):
    return a * 2.20462


if __name__ == '__main__':
    with open('hw.csv', 'rt') as f:
        f = f.readlines()
        get_avr_data(f)
