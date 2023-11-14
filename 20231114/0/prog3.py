class Asker:
    @staticmethod
    def askall(lst):
        for elem in lst:
            elem.report()


class Sender:
    first = True

    @classmethod
    def report(cls):
        if cls.first:
            print('Greetings!')
            cls.first = False
        else:
            print('Get away!')


Asker.askall([Sender() for i in range(3)])
