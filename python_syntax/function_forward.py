"""
https://facilecode.com/the-invisible-forward-function-in-pytorch/
"""

class Module:
    def __init__(self):
        pass
    def __call__(self, data):
        print("__call__ function, data =", data)

net = Module()
net([1,2,3])
# __call__ function, data = [1, 2, 3]

class Module:
    def __init__(self):
        pass
    def __call__(self, data):
        self.forward(data)

    def forward(self, data):
        print("forward function, data =", data)

net = Module()
net([1,2,3])
# forward function, data = [1, 2, 3]

# Net inherits from Module
class Net(Module):
    def __init__(self):
        super(Net, self).__init__()

    def forward(self, data):
        print("Net.forward, data =", data)

net = Net()
net([1,2,3,4])
# Net.forward, data = [1, 2, 3, 4]