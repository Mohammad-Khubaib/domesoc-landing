content = open('index.html', encoding='utf-8').read()
old = '          <div class="pricing-feature">Dedicated onboarding &amp; configuration</div>'
new = '          <div class="pricing-feature">Dedicated onboarding &amp; configuration</div>\n          <a href="https://calendly.com/rahima2014k/30min" target="_blank" style="display:inline-block;margin-top:8px;font-size:12px;color:#3B82F6;text-decoration:none;">Schedule onboarding call</a>'
if old in content:
    content = content.replace(old, new, 1)
    print('OK')
else:
    print('FAIL')
open('index.html', 'w', encoding='utf-8', newline='\n').write(content)
