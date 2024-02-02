class A:
    def __init__(self) -> None:
        print("in Init A")

    def feature1(self):
        print("features 1")

    def feature2(self):
        print("features 2")

class B:
    def __init__(self) -> None:
        print("in Init B")

    def feature3(self):
        print("features 3")

    def feature4(self):
        print("features 4") 

class C(A,B):
    def __init__(self) -> None:
        super().__init__()
        print("in Init C")

    def feature5(self):
        print("features 5")

    def feature6(self):
        print("features 6") 

c = C()
c.feature3()

