def format_text(text: list):

    t = []
    for i in range(1, 7):
        n_text = '<h' + str(i) + '>' + text[i - 1] + '</h' + str(i) + '>'
        t.append(n_text)
    text = ('' .join(t))

    return text
