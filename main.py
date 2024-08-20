def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  count = word_count(text)
  char_frequencies = count_char_frequencies(text)
  
  print_report(book_path, count, char_frequencies)

  
def get_book_text(path):
  with open(path) as file:
    text = file.read()
  return text


def word_count(text):
  words = text.split()
  return len(words)


def count_char_frequencies(s):
  d = {}
  
  for c in s:
    lowered_c = c.lower()
    
    if lowered_c not in d:
      d[lowered_c] = 1
    else:
      d[lowered_c] += 1
  
  return d
  

def print_report(path, count, dict):

  s = sorted(dict.items(), key= lambda item: item[1], reverse=True)
  
  print(f"--- Begin report of {path} ---")
  print(f"{count} words found in the document")
  print()
  
  for item in s:
    if item[0].isalpha():
      print(f"The '{item[0]}' character was found {item[1]} times")
  
  print(f"--- End report ---")
  
      
main()

