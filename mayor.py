class Mayor:
    def __init__(self) -> None:
        pass

    def mayor(self, numero1: int, numero2: int) -> int or None:
        # result = None
        if numero1 > numero2:
            result = numero1
        elif numero2 > numero1:
            result = numero2
        else:
            return None
        return result


# pytest -v  mayor.py

# print(mayor(2,1))#2
# print(mayor(1,2))#2
# print(mayor(2,2))#None


# || = or
# && = and
