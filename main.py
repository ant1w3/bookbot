def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  # print(text)
  count = word_count(text)
  print(count)

  
def get_book_text(path):
  with open("books/frankenstein.txt") as file:
    text = file.read()
  return text

def word_count(text):
  words = text.split()
  return len(words)
    
  
main()

