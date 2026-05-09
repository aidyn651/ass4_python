class DataAnalyser:

    def __init__(self, students):

        self.students = students
        self.result = {}

    def analyse(self):

        print('Not implemented — use a child class')

    def print_results(self):

        for key, value in self.result.items():

            print(f'{key}: {value}')

    def __str__(self):

        return f'DataAnalyser: base class, {len(self.students)} students'


# ==========================================
# Variant D
# ==========================================
class TopStudentsAnalyser(DataAnalyser):

    def __init__(self, students):

        super().__init__(students)

    def analyse(self):

        sorted_students = sorted(
            self.students,
            key=lambda x: float(x['final_exam_score']),
            reverse=True
        )

        top_10 = []

        for student in sorted_students[:10]:

            top_10.append({

                'score': student['final_exam_score'],
                'gpa': student['GPA'],
                'country': student['country']

            })

        self.result = {

            'total_students': len(self.students),
            'top_10': top_10

        }

    def print_results(self):

        print('==============================')
        print('TOP STUDENTS REPORT')
        print('==============================')

        super().print_results()

        print('==============================')

    def __str__(self):

        return f'TopStudentsAnalyser: Top Students Analysis, {len(self.students)} students'


# ==========================================
# Additional analyser for polymorphism
# ==========================================
class CountryAnalyser(DataAnalyser):

    def __init__(self, students):

        super().__init__(students)

    def analyse(self):

        countries = {}

        for student in self.students:

            country = student['country']

            if country in countries:

                countries[country] += 1

            else:

                countries[country] = 1

        sorted_countries = sorted(
            countries.items(),
            key=lambda x: x[1],
            reverse=True
        )

        self.result = {

            'total_students': len(self.students),
            'total_countries': len(countries),
            'top_3': sorted_countries[:3]

        }

    def print_results(self):

        print('==============================')
        print('COUNTRY ANALYSIS REPORT')
        print('==============================')

        super().print_results()

        print('==============================')

    def __str__(self):

        return f'CountryAnalyser: Country Analysis, {len(self.students)} students'
