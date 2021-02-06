class Employees():
    def __init__(self, name, age, languages):
        self.name = name
        self.age = age
        self.languages = list(languages)
    def print_languages(self):
        for i in range(len(self.languages)):
            print(self.languages[i])

class Manager():
    def __init__(self, name, age, languages):
        self.name = name
        self.age = age
        self.languages = languages
    def print_languages(self):
        for i in range(len(self.languages)):
            print(self.languages[i])
