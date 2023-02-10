from mayor import Mayor as m

class Testmayor:

    def test_mayor1(self):
        assert m.mayor(self,2,1) == 2

    # def test_mayor2(self):
    #     assert m.mayor(self,1,2) == 2

    # def test_mayor3(self):
    #     assert m.mayor(self,2,2) == None

    # def test_mayor4(self):
    #     assert m.mayor(self,1,-1) == 1

    # def test_mayor5(self):
    #     assert m.mayor(self,-1,1) == 1

    # def test_mayor6(self):
    #     assert m.mayor(self,-1,-1) == None

    # def test_mayor7(self):
    #     assert m.mayor(self,-1,-2) == -1

    # def test_mayor8(self):
    #     assert m.mayor(self,-2,-1) == -1   

#py -m pytest -v test