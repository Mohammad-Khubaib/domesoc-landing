content = open('index.html', encoding='utf-8').read()

# Add subtitle line to each stat
old_stats = '    <div class="stat"><div class="stat-num" style="color:var(--green)">26</div><div class="stat-label">SOAR actions</div></div>\n    <div class="stat"><div class="stat-num" style="color:var(--cyan)">12</div><div class="stat-label">Native integrations</div></div>\n    <div class="stat"><div class="stat-num" style="color:var(--blue)">3</div><div class="stat-label">AI networks</div></div>\n    <div class="stat"><div class="stat-num" style="color:var(--white)">100%</div><div class="stat-label">Decisions explained</div></div>'

new_stats = '    <div class="stat"><div class="stat-num" style="color:var(--green)">26</div><div class="stat-label">SOAR actions</div><div class="stat-sub">Auto-execute or require approval</div></div>\n    <div class="stat"><div class="stat-num" style="color:var(--cyan)">12</div><div class="stat-label">Native integrations</div><div class="stat-sub">CrowdStrike, Okta, Jira &amp; more</div></div>\n    <div class="stat"><div class="stat-num" style="color:var(--blue)">3</div><div class="stat-label">AI networks</div><div class="stat-sub">Running in parallel on every detection</div></div>\n    <div class="stat"><div class="stat-num" style="color:var(--white)">100%</div><div class="stat-label">Decisions explained</div><div class="stat-sub">Plain-English reasoning on every action</div></div>'

if old_stats in content:
    content = content.replace(old_stats, new_stats, 1)
    print("OK stats")
else:
    print("FAIL")
    idx = content.find("SOAR actions")
    print(repr(content[max(0,idx-100):idx+300]))

# Add stat-sub CSS
old_css = '.stat-label { font-size: 11px; color: var(--lgray); letter-spacing: 1.5px; text-transform: uppercase; margin-top: 2px; }'
new_css = '.stat-label { font-size: 11px; color: var(--lgray); letter-spacing: 1.5px; text-transform: uppercase; margin-top: 2px; }\n.stat-sub { font-size: 12px; color: var(--gray); margin-top: 6px; line-height: 1.4; }'
if old_css in content:
    content = content.replace(old_css, new_css, 1)
    print("OK css")
else:
    print("FAIL css")

open('index.html', 'w', encoding='utf-8', newline='\n').write(content)
print('Done')
