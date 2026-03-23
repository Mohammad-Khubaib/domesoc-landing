content = open('index.html', encoding='utf-8').read()
old = '      <a href="#pricing">Pricing</a>'
new = '      <a href="#pricing">Pricing</a>\n      <a href="https://stats.uptimerobot.com/ff3Xhbfv6L" target="_blank">Status</a>'
if old in content:
    content = content.replace(old, new, 1)
    print('OK')
else:
    print('FAIL')
open('index.html', 'w', encoding='utf-8', newline='\n').write(content)
