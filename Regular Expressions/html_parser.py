import re

html_content = input()
pattern = re.compile(r"(?:<title>)(?P<title_html>.+)(?:</title>).*(?:<body>)(?P<body_html>.+)(?:</body>)")
m_space, tabs_n, between = r"[ ]+", r"\\n|\\t", r"<[^>]*>"
result = re.finditer(pattern, html_content)
for show in result:
    print(f'Title: {re.sub(m_space, " ", re.sub(tabs_n, "", re.sub(between, "", show["title_html"])))}')
    print(f'Content: {re.sub(m_space, " ", re.sub(tabs_n, "", re.sub(between, "", show["body_html"])))}')
