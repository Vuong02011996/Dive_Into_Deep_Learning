import torch
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

class CustomDataset:
    def __init__(self, data, targets):
        self.data = data
        self.targets = targets

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        current_sample = self.data[idx, :]
        current_targets = self.targets[idx]

        return {
            "sample": torch.tensor(current_sample, dtype=torch.float),
            "target": torch.tensor(current_targets, dtype=torch.long)
        }


data, targets = make_classification(n_samples=1000)

train_data, test_data, train_target, test_target = train_test_split(data, targets, stratify=targets)
print(train_data.shape)
print(test_data.shape)
train_dataset = CustomDataset(train_data, train_target)
test_dataset = CustomDataset(test_data, test_target)

print(train_dataset[1:2])
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=4, num_workers=4)
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=4, num_workers=4)

model = lambda x, w, b: torch.matmul(x, w) + b
w = torch.randn(20, 1, requires_grad=True)
b = torch.randn(1, requires_grad=True)

# test not train
with torch.no_grad():
    y_true = []
    y_predict = []
    for data in test_loader:
        x_test = data["sample"]
        y_test = data["target"]

        output_test = model(x_test, w, b)
        y_true.append(y_test)
        y_predict.append(output_test)

    score = roc_auc_score(torch.cat(y_true).view(-1), torch.cat(y_predict).view(-1))
    print(score)

lr = 0.001
for epoch in range(10):
    epoch_loss = 0
    counter = 0
    for data in train_loader:
        x_train = data["sample"]
        y_train = data["target"]
        output_train = model(x_train, w, b)
        loss = torch.mean((y_train.view(-1) - output_train.view(-1))**2)
        # print(w.grad)
        epoch_loss += loss.item()
        loss.backward()
        with torch.no_grad():
            # not using w -= lr_w.grad
            w = w - lr * w.grad
            b = b - lr * b.grad

        w.requires_grad_(True)
        b.requires_grad_(True)

        counter += 1
    print(epoch, epoch_loss/counter)

print(w)
print(b)

# test model

with torch.no_grad():
    y_true = []
    y_predict = []
    for data in test_loader:
        x_test = data["sample"]
        y_test = data["target"]

        output_test = model(x_test, w, b)
        y_true.append(y_test)
        y_predict.append(output_test)

    score = roc_auc_score(torch.cat(y_true).view(-1), torch.cat(y_predict).view(-1))
    print(score)

