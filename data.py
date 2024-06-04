import pandas
from random import choice


class Data:

    def __init__(self):
        self.data = self.check_word_to_learn()
        self.random_pick()

    def random_pick(self):
        data = self.convert_to_dic()
        if len(data) < 1:
            word = 0
        else:
            word = choice(data)
            print(word)

        return word

    def convert_to_dic(self):
        data = self.data
        new_dict = data.to_dict(orient="records")
        return new_dict

    @staticmethod
    def words_to_learn(word):
        try:
            data = pandas.read_csv("data/words_to_learn.csv")
        except FileNotFoundError:
            data = pandas.read_csv("data/english_words.csv")
            data.to_csv("data/words_to_learn.csv", mode="w", index=False)
        finally:
            list_of_words = data.values.tolist()
            if [word["English"], word["Spanish"]] in list_of_words:
                list_of_words.remove([word["English"], word["Spanish"]])
            new_data = pandas.DataFrame(list_of_words, columns=["English", "Spanish"])
            new_data.to_csv("data/words_to_learn.csv", mode="w", index=False)

    @staticmethod
    def check_word_to_learn():
        # Check if exits file words to learn
        try:
            # Checks for file
            file = pandas.read_csv("data/words_to_learn.csv")
        except FileNotFoundError:
            file = pandas.read_csv("data/english_words.csv")
        finally:
            return file

    def reset_words(self):
        data = pandas.read_csv("data/english_words.csv")
        data.to_csv("data/words_to_learn.csv", mode="w", index=False)
        self.data = pandas.read_csv("data/words_to_learn.csv")



