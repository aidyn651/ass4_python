import csv


class DataLoader:

    def __init__(self, filename):

        self.filename = filename
        self.students = []

    def load(self):

        with open(self.filename, 'r', encoding='utf-8') as file:

            reader = csv.DictReader(file)

            self.students = list(reader)

        print(f'Loaded {len(self.students)} students.')

    def preview(self, limit=3):

        print('Preview:')

        for student in self.students[:limit]:

            print(student)
