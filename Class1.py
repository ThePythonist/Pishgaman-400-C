class Car :
    def __init__(self, n, m):
        self.name = n
        self.model = m

    def Break(self):
        print('Break!')

    def Tell_Info(self):
        print("Name :", self.name)
        print("Model :", self.model)

persia = Car('persia','1400')
persia.Tell_Info()
