from deep_translator import GoogleTranslator

# Use any translator you like, in this example GoogleTranslator
text = 'happy coding'
# translated = GoogleTranslator(source='en', target='zh-CN').translate(text=text)
translated = GoogleTranslator(source='en', target='ja').translate(text=text)

print(translated)