import string
import random


class String:
    """String class"""

    def __init__(self, length: int):
        self.length = length
        self.value = self.generate()

    def generate(self) -> str:
        """Generate random string"""
        result_str = ""
        word_size_count = 0
        random_word_size = random.randint(3, 4)

        for _ in range(self.length):
            word_size_count += 1
            if word_size_count > random_word_size:
                result_str += " "
                random_word_size = random.randint(3, 4)
                word_size_count = 0
            else:
                result_str += random.choice(string.ascii_lowercase + string.digits)

        return result_str

    def average_word_length(self) -> float:
        """Average word length in string"""
        words = self.value.split()
        average_length = sum(len(word) for word in words) / len(words)
        return average_length

    def remove_words(self):
        """Remove words from string starts with digit"""
        words_list = []
        for word in self.value.split():
            if not word[0].isdigit():
                words_list.append(word)

        self.value = " ".join(words_list)

    def sort(self):
        """Sort string"""
        words = self.value.split()
        words.sort()
        self.value = " ".join(words)


if __name__ == '__main__':
    # generate random string
    str_gen = String(100)

    # get average word length
    print(str_gen.average_word_length())

    # remove words from string starts with digit"
    str_gen.remove_words()

    # sort generated string
    str_gen.sort()
