favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'huskell'],
    'anna': ['java script']
}

for name, languages in sorted(favorite_languages.items()):
    if len(languages) > 1:
        print(f"{name}'s favorite coding languages:")
        for language in languages:
            print("\t" + language)
    else:
        print(f"{name} only uses:")
        for i in languages:
            print("\t" + i)




