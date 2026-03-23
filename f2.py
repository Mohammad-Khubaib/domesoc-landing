content = open('index.html', encoding='utf-8').read()
content = content.replace(
    'href="https://stats.uptimerobot.com/ff3Xhbfv6L"',
    'href="/status.html"'
)
open('index.html', 'w', encoding='utf-8', newline='\n').write(content)
print('OK')
