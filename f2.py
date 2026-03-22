content = open('index.html', encoding='utf-8').read()
# Add icons and better styling to stats
old_stat_css = '.stat { padding: 32px 24px; text-align: center; border-right: 1px solid var(--border); }\n.stat:last-child { border-right: none; }\n.stat-num { font-family: "Barlow", sans-serif; font-size: 32px; font-weight: 800; margin-bottom: 4px; }\n.stat-label { font-size: 11px; color: var(--gray); letter-spacing: 1px; text-transform: uppercase; }'
new_stat_css = '.stat { padding: 28px 24px; text-align: center; border-right: 1px solid var(--border); }\n.stat:last-child { border-right: none; }\n.stat-num { font-family: "Barlow", sans-serif; font-size: 36px; font-weight: 900; margin-bottom: 6px; letter-spacing: -1px; }\n.stat-label { font-size: 11px; color: var(--lgray); letter-spacing: 1.5px; text-transform: uppercase; margin-top: 2px; }'
if old_stat_css in content:
    content = content.replace(old_stat_css, new_stat_css, 1)
    print('OK stat css')
else:
    print('FAIL stat css')
open('index.html', 'w', encoding='utf-8', newline='\n').write(content)
