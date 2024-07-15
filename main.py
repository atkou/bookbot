path_to_file = 'books/frankenstein.txt'

def print_out(contents):
    print(contents)

def count_words(contents):
    words = contents.split()
    print(f"There are {len(words)} words in the file")

def count_characters(contents):
    str = contents.lower()
    count_dict = {}

    for char in contents:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    print(count_dict)

def main():
    with open(path_to_file) as f:
        file_contents = f.read()
    
    #print_out(file_contents)
    #count_words(file_contents)
    count_characters(file_contents)

if __name__ == '__main__':
    main()