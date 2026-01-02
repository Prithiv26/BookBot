import sys, time

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
        return contents

def count_words(contents):
    length =  len(contents.split())
    return length

def count_chars(contents):
    contents = contents.lower()
    charMap = {}
    for i in contents:
        if i in charMap:
            charMap[i] += 1
        else:
            charMap[i] = 1
    return charMap

def sort_on(dict):
    return dict['num']

def transform_charmap(charMap):
    char_list = []
    for k, v in charMap.items():
        char_list.append({'char' : k, 'num' : v})
    char_list.sort(reverse=True, key=sort_on)
    return char_list


def main():
    path = sys.argv[1]
    contents = get_book_text(path)
    words = count_words(contents)
    final_list = transform_charmap(count_chars(contents))

    print("=" * 8 + 'BOOK REPORT' + "=" * 8)
    print(f"Analyzing books found at {path}...")
    time.sleep(0.6)
    print("-" * 8 + "WORD COUNT" + "-" * 8)
    print(f"Found {words} total words")
    print("-" * 8 + "CHARACTER COUNT" + "-" * 8)
    for pair in final_list:
        if not pair['char'].isalpha():
            continue
        print(f"{pair['char']}:  {pair['num']}")


main()