class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse_string(self, input_str):
        """
        Reverses order of characters in string input_str.
        """
        return input_str[::-1]

    def is_english_vowel(self, character):
        """
        Returns True if character is an english vowel
        and False otherwise.
        """
        if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u' or character == 'A' or character == 'E' or character == 'I' or character == 'O' or character == 'U':
            return True
        else:
            return False

    def find_longest_word(self, sentence):
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        s = sentence.split(' ')
        l = 0
        op = []
        for i in s:
            if len(i) > l:
                l = len(i)
                op.append(i)
        return max(s, key=len)

    def get_word_lengths(self, text):
        """
        Returns a list of integers representing
        the word lengths in string text.
        """
        op = []
        s = text.split(' ')
        for i in s:
            op.append(len(i))
        return op