content = open('index.html', encoding='utf-8').read()

# Fix duplicate SOAR - find and remove second occurrence
soar_line = '    <div class="stat"><div class="stat-num" style="color:var(--green)">26</div><div class="stat-label">SOAR actions</div></div>'
idx1 = content.find(soar_line)
idx2 = content.find(soar_line, idx1 + 10)
if idx2 > 0:
    content = content[:idx2] + content[idx2+len(soar_line):]
    print('duplicate removed')

# Also update audit coverage to decisions explained
content = content.replace(
    '<div class="stat-label">Audit coverage</div>',
    '<div class="stat-label">Decisions explained</div>'
)
content = content.replace(
    '<div class="stat-num" style="color:var(--blue)">3</div><div class="stat-label">AI networks</div>',
    '<div class="stat-num" style="color:var(--blue)">3</div><div class="stat-label">AI networks</div>'
)

# Verify final state
import re
stats = re.findall(r'stat-label">(.*?)</div>', content)
print('Stats:', stats[:8])

open('index.html', 'w', encoding='utf-8', newline='\n').write(content)
print('Done')
