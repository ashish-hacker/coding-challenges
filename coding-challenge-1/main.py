import sys

def count_words(text):
    return len(text.split())

def count_bytes(text):
    return len(text.encode('utf-8'))

def count_lines(text):
    return len(text.split('\n'))

def main(args=sys.argv):

    word_count_enabled = args[1] == '-c' or args[1] == '--count-words'
    bytes_count_enabled = args[1] == '-b' or args[1] == '--count-bytes'
    lines_count_enabled = args[1] == '-l' or args[1] == '--count-lines'

    with open('test.txt', 'r') as file:
        text = file.read()
        if word_count_enabled:
            print(count_words(text))
        elif bytes_count_enabled:
            print(count_bytes(text))
        elif lines_count_enabled:
            print(count_lines(text))



if __name__ == '__main__':
    main()