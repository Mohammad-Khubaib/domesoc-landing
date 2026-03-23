content = open('index.html', encoding='utf-8').read()
old = '<div class="footer-copy">© 2026 DomeSOC. All rights reserved.</div>'
new = '<div class="footer-copy">© 2026 DomeSOC · <a href="/terms.html" style="color:#64748B;text-decoration:none;">Terms</a> · <a href="/privacy.html" style="color:#64748B;text-decoration:none;">Privacy</a></div>'
if old in content:
    content = content.replace(old, new, 1)
    print('OK footer')
else:
    print('FAIL footer')
open('index.html', 'w', encoding='utf-8', newline='\n').write(content)
