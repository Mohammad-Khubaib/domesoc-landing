
page = open('index.html', encoding='utf-8').read()

# We will replace the full body content but keep the head styles
# First let's see what the current CTA button says
idx = page.find('signup')
print(repr(page[max(0,idx-100):idx+100]))
