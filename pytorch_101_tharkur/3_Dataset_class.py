import torch
from sklearn.datasets import make_classification


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
            "targets": torch.tensor(current_targets, dtype=torch.long)
        }


data , target = make_classification(1000, 10)
print(target.shape)
print(data.shape)

custom_dataset = CustomDataset(data, target)

print(len(custom_dataset))
print(custom_dataset[20:30])
