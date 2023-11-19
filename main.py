def getBook():
    with open("./book.txt") as f:
        return f.read()
    
def countWords(text):
    words = text.split()
    return len(words)

def countLetters(text):
    text = text.lower()
    total_count = {}
    for i in range(len(text)):
        total_count[text[i]] = total_count.get(text[i], 0) + 1
    return total_count

def buildReport(text):
    total_count = countWords(text)
    print("--- Begin report of book.txt ---")

    print(f"{total_count} words found in the document")

    for i in range(len(text)):
        if text[i] in total_count:
            total_count[text[i]] += 1
        else:
            total_count[text[i]] = 1
    
    print(total_count) 

print(buildReport(getBook()))