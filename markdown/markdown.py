import re

STRONG_TAG_REG = r'(.*)__(.*)__(.*)'
LIST_TAG_REG = r'\* (.*)'
ITALIC_TAG_REG = r'(.*)_(.*)_(.*)'


def parse(markdown):
    ''' Parses text in Markdown '''
    lines = markdown.split('\n')

    return parse_page(lines)


def parse_page(lines):
    ''' Parses Markdown lines with no context '''
    parsed = ''
    index = 0

    while index < len(lines):
        line = lines[index]
        line = parse_header_line(line)

        if re.match(LIST_TAG_REG, line):
            parsed_list, index = parse_list(index, lines)
            parsed += parsed_list

            continue

        line = line_text_into_paragraph(line)
        line = parse_text_decoration(line)
        parsed += line

        index += 1

    return parsed


def parse_list(index, lines):
    ''' Parses Markdown lines that represent a list '''
    parsed = '<ul>'
    in_list = True

    while index < len(lines):
        line = lines[index]
        line, in_list = parse_list_element(line)
        if not in_list:
            break
        parsed += line
        index += 1
    parsed += '</ul>'

    return parsed, index


def parse_list_element(line):
    ''' Parses single list element '''
    if m := re.match(r'\* (.*)', line):
        content = m.group(1)
        content = parse_text_decoration(content)
        line = '<li>' + content + '</li>'

    return line, m is not None


def parse_header_line(line):
    ''' Parses a header '''
    if re.match('###### (.*)', line) is not None:
        line = '<h6>' + line[7:] + '</h6>'
    elif re.match('## (.*)', line) is not None:
        line = '<h2>' + line[3:] + '</h2>'
    elif re.match('# (.*)', line) is not None:
        line = '<h1>' + line[2:] + '</h1>'

    return line


def line_text_into_paragraph(line):
    ''' Wraps a block of decorated text into a paragraph '''
    is_wrapped = re.match('<h|<ul|<p|<li', line)

    if not is_wrapped:
        line = '<p>' + line + '</p>'

    return line


def parse_text_decoration(line):
    ''' Parses italics and strong emphasis '''
    line = parse_strong(line)
    line = parse_italic(line)

    return line


def parse_strong(line):
    strong = re.match(STRONG_TAG_REG, line)

    if strong:
        line = strong.group(1)
        line += '<strong>' + strong.group(2) + '</strong>' + strong.group(3)

    return line


def parse_italic(line):
    italic = re.match(ITALIC_TAG_REG, line)

    if italic:
        line = italic.group(1)
        line += '<em>' + italic.group(2) + '</em>' + italic.group(3)

    return line
