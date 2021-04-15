import torch
from sklearn.datasets import make_classification


class CustomDataset:
    def __init__(self, data, targets):
        self.data = data
        self.target = targets

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        current_sample = self.data[idx]
        current_target = self.target[idx]
        return {
            "sample": torch.tensor(current_sample, dtype=torch.float),
            "target": torch.tensor(current_target, dtype=torch.long)
        }


data, targets = make_classification(n_samples=1000)

custom_dataset = CustomDataset(data, targets)

train_loader = torch.utils.data.DataLoader(custom_dataset, batch_size=4, num_workers=0)

print(train_loader)
for data in train_loader:
    print(data["sample"].shape)
    print(data["target"].shape)
    break

# train
model = None
for epoch in range(10):
    for data in train_loader:
        x = data["sample"]
        y = data["targer"]
        output = model(x, y)
        # Loss
        # Loss.backward()
        # ...
