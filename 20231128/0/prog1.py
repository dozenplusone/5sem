C = type("C", (), {"var": 100500, "__init__": lambda self, val: setattr(self, "var", val)})
