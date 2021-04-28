import torch
import numpy as np

print(torch.cuda.is_available())

some_data = [[1, 2], [3, 4]]

print(np.array(some_data))

some_data = torch.tensor(some_data)
print(type(some_data))
print(some_data.dtype)

# convert numpy array to tensor
numpy_arr = np.random.rand(3, 4)
print(numpy_arr)
tensor_arr = torch.from_numpy(numpy_arr)
print(tensor_arr)

# Create some data test
print(torch.ones(3, 4))
print(torch.zeros(3, 4))
print(torch.rand(3, 4))

# operation on CPU or GPU
my_tensor = torch.rand(3, 4)
print(my_tensor.dtype)
print(my_tensor.device)
# my_tensor = my_tensor.to("cuda")

print(my_tensor.mul(my_tensor))
print(my_tensor * my_tensor)

print(my_tensor.matmul(my_tensor.T))
print(torch.matmul(my_tensor, my_tensor.T))
print(my_tensor @ my_tensor.T)

print(torch.max(my_tensor,dim=1))

print(torch.cat([my_tensor, my_tensor]))

print(torch.nn.functional.softmax(my_tensor, dim=1))

image_tensor = torch.rand(10, 3, 128, 128)
print(image_tensor.size())

# my_tensor.clip(0.1, 0.8)

# convert tensor to numpy array
print(my_tensor.cpu().detach().numpy())