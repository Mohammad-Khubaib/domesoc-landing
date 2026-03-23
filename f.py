content = open('index.html', encoding='utf-8').read()
old = '      <a href="/status.html" target="_blank">Status'
new = '      <a href="/status.html" target="_blank">Status</a>\n      <a href="/terms.html">Terms</a>\n      <a href="/privacy.html">Privacy</a>'
# Find exact end of Status link
idx = content.find(old)
if idx >= 0:
    end = content.find('</a>', idx) + 4
    current = content[idx:end]
    print('current:', repr(current))
    content = content[:idx] + new + content[end:]
    print('OK')
else:
    print('FAIL')
open('index.html', 'w', encoding='utf-8', newline='\n').write(content)
