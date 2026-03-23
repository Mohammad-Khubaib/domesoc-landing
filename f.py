content = open('index.html', encoding='utf-8').read()

# Add Terms and Privacy to nav
old_nav = '      <a href="https://stats.uptimerobot.com/ff3Xhbfv6L" target="_blank">Status</a>'
new_nav = '      <a href="https://stats.uptimerobot.com/ff3Xhbfv6L" target="_blank">Status</a>
      <a href="/terms.html">Terms</a>
      <a href="/privacy.html">Privacy</a>'
if old_nav in content:
    content = content.replace(old_nav, new_nav, 1)
    print('OK nav')
else:
    print('FAIL nav')

open('index.html', 'w', encoding='utf-8', newline='\n').write(content)
