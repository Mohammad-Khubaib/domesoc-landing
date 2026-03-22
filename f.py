content = open('index.html', encoding='utf-8').read()
old = 'Threat contained in <span class="t-score">2.1 seconds</span> — 0 analyst interventions required — full audit trail saved'
new = 'Threat contained — 0 analyst interventions required — full audit trail saved — <span class="t-score">decision reasoning logged</span>'
if old in content:
    content = content.replace(old, new, 1)
    print('OK')
else:
    print('FAIL')
    idx = content.find('2.1')
    print(repr(content[max(0,idx-50):idx+100]))
open('index.html', 'w', encoding='utf-8', newline='\n').write(content)
