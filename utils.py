def format_text(text: list):

    t = []
    for i in range(len(text)):
        n_text = '<h3>' + str(i+1) + '.  ' + text[i] + '</h3>'
        t.append(n_text)
    text = ('' .join(t))

    return text
