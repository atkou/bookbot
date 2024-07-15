path_to_file = 'books/frankenstein.txt'

def print_out(contents):
    print(contents)

def count_words(contents):
    words = contents.split()
    return len(words)

def count_characters(contents):
    contents = contents.lower()
    count_dict = {}

    for char in contents:
        if not char.isalpha(): continue

        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    return count_dict

def sort_on(dict):
    return dict["count"]

def dict_to_list_of_dicts(char_dict):
    result = []
    for char, count in char_dict.items():
        result.append({"char": char, "count": count})
    return result

def count_report(list):
    for item in list:
        print(f"The '{item['char']}' character was found {item['count']} times")


def main():
    with open(path_to_file) as f:
        file_contents = f.read()
    
    words = count_words(file_contents)
    count_dict = count_characters(file_contents)
    count_list = dict_to_list_of_dicts(count_dict)
    count_list.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document\n")
    count_report(count_list)
    print("--- End report ---")

if __name__ == '__main__':
    main()