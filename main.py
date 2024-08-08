with open("books/frankenstein.txt") as f:
        file_content = f.read()
def number_of_words():
        words = file_content.split()
        return len(words)
def lower_string(string):
    return string.lower()
def number_of_characters():
    characters = {}
    file = lower_string(file_content)
    
    for i in range(0,77986):
        w = file[i]
        if(characters.__contains__(w)):
            q = characters[w]
            q+=1
            characters[w]=q
        else:
            characters[w]=1
    return characters
def report():
     print("--- Begin report of frankenstein ---")
     print(f"{number_of_words()} words was found in this document")
     ch = number_of_characters()
     keys = ch.keys()
     for key in keys:
          print(f"The {key} character was found {ch[key]} times")
     print("--- End report ---")
report()