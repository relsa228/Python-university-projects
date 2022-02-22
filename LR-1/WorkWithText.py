import string
import re


class WorkWithText(object):
    text = ""

    def wordcount(self):
        self.text = self.text.lower()
        tuple_text = self.text.translate(self.text.maketrans('', '', string.punctuation)).split()
        dict_text = dict((word, tuple_text.count(word)) for word in set(tuple_text) if tuple_text.count(word) >= 1)
        result = "\nСписок слов и их повторения в тексте:\n"
        for i in set(tuple_text):
            result = result + f"{i} -- {dict_text[i]}\n"
        return result

    def averagewords(self):
        self.text = self.text.lower()
        tuple_text = re.split(r"[!?.]\s*", self.text)
        tuple_text = [value for value in tuple_text if value != ""]
        sent_count = []
        average = 0
        for sent in tuple_text:
            sent = sent.translate(self.text.maketrans('', '', string.punctuation)).split()
            sent_count.append(len(sent))
        for i in sent_count:
            average = average + i
        result = f"Среднее количество слов в предложениях: {average/len(sent_count)}\nМедианное количество слов в предло" \
                 f"жениях: {(len(sent_count)+1)/2}\n"
        return result

    def topengrams(self, k, n):
        self.text = self.text.lower()
        tuple_text = self.text.translate(self.text.maketrans('', '', string.punctuation)).replace(' ', '')
        i = 0
        n_grams = []
        while n <= len(tuple_text):
            n_grams.append(tuple_text[i:n])
            n = n + 1
            i = i + 1
        n_grams = dict((word, n_grams.count(word)) for word in set(n_grams) if n_grams.count(word) >= 1)
        sorted_tuple = sorted(n_grams.items(), key=lambda x: x[1])




