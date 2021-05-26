import code.my_untils as until
import numpy as np
import torch
from torch import nn


def load_array(data_arrays, batch_size, is_train=True):
    """Construct a Pytorch data iterator"""

    dataset = torch.utils.data.TensorDataset(*data_arrays)
    return torch.utils.data.DataLoader(dataset, batch_size, shuffle=is_train)


if __name__ == '__main__':
    true_w = torch.tensor([2, -3.4])
    true_b = 4.2

    # Step 1: Prepare data
    features, labels = until.synthetic_data(true_w, true_b, 1000)

    batch_size = 10
    data_iter = load_array((features, labels), batch_size=batch_size)
    print(next(iter(data_iter)))

    # Step 2: defined model
    # Fully-connected layer is defined in the Linear class
    # Two arguments (input features dimension and output features dimension)
    net = nn.Sequential(nn.Linear(2, 1))

    # Step 3: Initializing model parameters

    net[0].weight.data.normal_(0, 0.01)
    net[0].bias.data.fill_(0)

    # Step 4: Defining the loss function
    loss = nn.MSELoss()

    # Step 5: Defining the optimization algorithm
    trainer = torch.optim.SGD(net.parameters(), lr=0.03)

    # Step 6:Training
    num_epochs = 3
    for i in range(num_epochs):
        for X, y_true in data_iter:
            l = loss(net(X), y_true)
            trainer.zero_grad()
            l.backward()
            trainer.step()
        l = loss(net(features), labels)
        print("Epoch {}, loss {}".format(i, l))

    w = net[0].weight.data
    b = net[0].bias.data
    print("w = ", w)
    print("b = ", b)
    print("error weight: ", true_w - w)
    print("error bias: ", true_b - b)






