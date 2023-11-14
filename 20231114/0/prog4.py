class C:
    @property
    def age(self):
        if self._data == 42:
            print('secret value!')
            return -1
        else:
            return self._data

    @age.setter
    def age(self, value):
        if value <= 128:
            self._data = value
        else:
            print('too old!')
            raise ValueError()
