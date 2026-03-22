content = open('index.html', encoding='utf-8').read()

old = '''    <div class="stat"><div class="stat-num" style="color:var(--green)">26</div><div class="stat-label">SOAR actions</div></div>
    <div class="stat"><div class="stat-num" style="color:var(--cyan)">12</div><div class="stat-label">Native integrations</div></div>
    <div class="stat"><div class="stat-num" style="color:var(--white)">100%</div><div class="stat-label">Decisions explained</div></div>'''

new = '''    <div class="stat"><div class="stat-num" style="color:var(--green)">26</div><div class="stat-label">SOAR actions</div></div>
    <div class="stat"><div class="stat-num" style="color:var(--cyan)">12</div><div class="stat-label">Native integrations</div></div>
    <div class="stat"><div class="stat-num" style="color:var(--blue)">3</div><div class="stat-label">AI networks</div></div>
    <div class="stat"><div class="stat-num" style="color:var(--white)">100%</div><div class="stat-label">Decisions explained</div></div>'''

if old in content:
    content = content.replace(old, new, 1)
    print('OK')
else:
    print('FAIL')
    idx = content.find('SOAR actions')
    print(repr(content[max(0,idx-100):idx+200]))

open('index.html', 'w', encoding='utf-8', newline='\n').write(content)
print('Done')
