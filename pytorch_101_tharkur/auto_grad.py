import torch

a = torch.tensor([5.], requires_grad=True)
b = torch.tensor([6.], requires_grad=True)

print(a)
print(b)

y = a**3 - b**2
print(y)

# dy/da = 3*a**2 = 75
# dy/db = -2*b = 12
print(a.grad)
print(b.grad)

y.backward()

print(a.grad)
print(b.grad)

W = torch.randn(10, 1, requires_grad=True)
b = torch.randn(1, requires_grad=True)
print(W)
print(b)

x = torch.rand(1, 10)
print(x)

output = torch.matmul(x, W) + b

print(output)
print(W.grad)
output.backward()
print(W.grad)
lr = 0.001
with torch.no_grad():
    W = W - lr*W.grad.data
print(W)
print(W.grad)