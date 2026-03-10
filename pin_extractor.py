"""This is a function that takes some poem, for which you shall
determine the pin based on the ith letter of the ith line"""
def pin_extractor(poem):
    secret_code = ''
    lines = poem.split('\n')
    for line_index, line in enumerate(lines):
        print(line_index, line)
        words = line.split()
        
        if line_index > len(words[line_index]):
            secret_code = secret_code + words[line_index][0]
        else:
            secret_code = secret_code + words[line_index][line_index]
        # print(secret_code)
        print(words)
    print(secret_code)

poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

pin_extractor(poem)

