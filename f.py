content = open('index.html', encoding='utf-8').read()

old = '      <a href="#how-it-works">How it works</a>\n      <a href="#autonomous">Autonomous AI</a>\n      <a href="#explainable">Explainable AI</a>\n      <a href="#integrations">Integrations</a>\n      <a href="#pricing">Pricing</a>\n      <a href="/status.html" target="_blank">Status</a>\n      <a href="/terms.html">Terms</a>\n      <a href="/privacy.html">Privacy</a>'

new = '      <a href="#how-it-works">How it works</a>\n      <a href="#pricing">Pricing</a>\n      <a href="#integrations">Integrations</a>\n      <a href="/status.html">Status</a>'

if old in content:
    content = content.replace(old, new, 1)
    print('OK')
else:
    print('FAIL')
    idx = content.find('nav-links">')
    print(repr(content[idx:idx+400]))

open('index.html', 'w', encoding='utf-8', newline='\n').write(content)
