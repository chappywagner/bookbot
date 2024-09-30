file = open('books/frankenstein.txt','r')
content = file.read()
unique_chars = {}

content = content.replace(' ','')
content = content.rstrip().lstrip()
content = content.replace('\t','')

for c in content:

    if c.isalpha():
        lc = c.lower()

        if lc in unique_chars.keys():
            unique_chars[lc] += 1
        else:
            unique_chars[lc] = 1


for k in unique_chars:
    print(f"The character '{k}' was found {unique_chars[k]} times")
#print(len(content.split()))
#print(content)
file.close()