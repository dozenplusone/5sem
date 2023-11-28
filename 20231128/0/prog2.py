class sole(type):
    def __new__(metacls, name, parents, namespace):
        if len(parents) > 1:
            raise TypeError("at most one parent is allowed")
        return super().__new__(metacls, name, parents, namespace)
