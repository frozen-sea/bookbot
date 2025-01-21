import string

def wc_w(s):
    return len(s.split())

def char_map(s):
    counts = dict(zip(list(string.ascii_lowercase), [0]*len(string.ascii_lowercase)))
    for c in s:
        l = c.lower()
        if l in counts:
            counts[l] += 1
    return counts

def main():
    FILE_NAME = "books/frankenstein.txt"

    with open(FILE_NAME) as f:
        file_contents = f.read()

    print(f"--- Begin report of {FILE_NAME} ---")
    print(f"{wc_w(file_contents)} words found in the document")
    print("")
    char_counts = char_map(file_contents).items()
    sorted_by_count = dict(sorted(char_counts, key=lambda x: x[1], reverse = True)).items()
    for k, v in sorted_by_count:
        print(f"The '{k}' character was found {v} times")
    print("--- End report ---")

main()
