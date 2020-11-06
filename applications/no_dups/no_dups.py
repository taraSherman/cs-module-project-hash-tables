def no_dups(s):
    # Your code here
    # create dictionary
    words = {}
    # split string, store in variable
    words_list = s.split()
    # create empty array
    no_dupes_list = []
    # loop over
    for word in words_list:
        # if word not found in dictionary, add it to array
        if word not in words:
            words[word] = 1
            no_dupes_list.append(word)
    # use join on words in array to make string and return that
    return ' '.join(no_dupes_list)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
