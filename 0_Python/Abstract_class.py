from abc import ABC, abstractmethod

class absclasstest(ABC):

    @abstractmethod
    def do_some(self):
        print("I am in my abs class")


class myclass(absclasstest):

    def do_some(self):
        super().do_some()
        print('Addtion in code')

a = myclass()
a.do_some()

