import random
import torch
import d2l.torch as d2l


def synthetic_data(w, b, num_example):
    """generating the dataset"""
    X = torch.normal(0, 1, (num_example, len(w)))
    y = torch.matmul(X, w) + b
    y += torch.normal(0, 0.01, y.shape)
    return X, y.reshape((-1, 1))


def data_iter(batch_size, features, labels):
    num_examples = len(labels)
    indices = list(range(num_examples))
    random.shuffle(indices)

    for i in range(0, num_examples, batch_size):
        batch_indices = torch.tensor(indices[i:min(i+batch_size, num_examples)])

        yield features[batch_indices], labels[batch_indices]


def linear_reg_model(X, w, b):
    """The linear regression model"""
    return torch.matmul(X, w) + b


def squared_loss(y_pre, y_true):
    """Squared Loss."""

    return (y_pre - y_true.reshape(y_pre.shape)) ** 2 / 2


def sgd(params, lr, batch_size):
    with torch.no_grad():
        for param in params:
            param -= (lr * param.grad)/batch_size
            param.grad.zero_()


if __name__ == '__main__':
    true_w = torch.tensor([10, -3.4])
    true_b = 0.2
    features, labels = synthetic_data(true_w, true_b, 200)

    # d2l.set_figsize()
    # print(label)
    # print(label.detach())
    # d2l.plt.scatter(features[:, 0].detach().numpy(), labels.detach().numpy(), 1)
    # d2l.plt.show()

    batch_size = 10

    for X, y in data_iter(batch_size, features, labels):
        print(X, "\n", y)
        break

    w = torch.normal(0, 0.01, size=(2, 1), requires_grad=True)
    b = torch.zeros(1, requires_grad=True)

    lr = 0.03
    num_epochs = 10
    net = linear_reg_model
    loss = squared_loss

    for epoch in range(num_epochs):
        for X, y_true in data_iter(batch_size, features, labels):
            l = loss(net(X, w, b), y_true)
            l.sum().backward()
            sgd([w, b], lr, batch_size)
        with torch.no_grad():
            train_l = loss(net(features, w, b), labels)
            print(f'epoch {epoch + 1} : loss {float(train_l.mean()): f}')
    print("w", w)
    print("b", b)
    print(w.reshape(true_w.shape) - true_w)
    print(b - true_b)

