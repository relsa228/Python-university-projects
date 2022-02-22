import TextModule
import os


class UserInterface(object):
    text_in_proc = TextModule.WorkWithText
    original_text = ""

    def start_word_count(self):
        print(self.text_in_proc.word_count(self.text_in_proc))

    def start_average_words(self):
        print(self.text_in_proc.average_words(self.text_in_proc))

    def start_top_engrams(self):
        print("Желаете самостоятельно ввести значения N и K? (Y/AnyKey)")
        if input() == "Y":
            print("Введите N: ")
            n = int(input())
            print("Введите K: ")
            k = int(input())
            print(self.text_in_proc.top_engrams(self.text_in_proc, k, n))
        else:
            print("Запускаем функцию со стандартными параметрами: K = 10, N = 4")
            print(self.text_in_proc.top_engrams(self.text_in_proc, 10, 4))

    def start_interface(self):
        print("Введите текст: ")
        self.original_text = input()
        self.text_in_proc.text = self.original_text
        while True:
            os.system('cls||clear')
            print("Выберите действие:\n1. Статистика по словам\n2. Среднее и медианное количество слов в предложении"
                  "\n3. Топ n-грам\n4. Получить рабочую строку\n5. Выйти")
            choose = input()
            match choose:
                case "1":
                    os.system('cls||clear')
                    self.start_word_count(self)
                    input()
                case "2":
                    os.system('cls||clear')
                    self.start_average_words(self)
                    input()
                case "3":
                    os.system('cls||clear')
                    self.start_top_engrams(self)
                    input()
                case "4":
                    os.system('cls||clear')
                    print(f"Ваша строка: {self.original_text}")
                    input()
                case "5":
                    break
                case _:
                    os.system('cls||clear')
                    print("Неверный ввод.")
                    input()
