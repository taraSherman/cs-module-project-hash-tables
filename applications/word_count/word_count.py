ignore_chars = "\" : ; , . - + = / \ | [ ] { } ( ) * ^ &".split()

def word_count(s):
    sentence = {}
    # split string into separate strings (words) on spaces
    words = s.split()
    # for each word
    for word in words:
        # make all lowercase
        word = word.lower()
        # for each character that is to be ignored,
        for i in ignore_chars:
            # remove it
            word = word.replace(i, "")
        # so long as input is not an ignored character, do one or the other of the following
        if word != "":
            # if input is empty
            if word not in sentence:
                # return empty
                sentence[word] = 0
            # if input is not empty, add and move to next
            sentence[word] += 1
    return sentence


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
