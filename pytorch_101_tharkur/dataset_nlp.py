import torch


# classification/ regression problems - text/nlp problem
class CustomDataset:
    def __init__(self, data, targets, tokenizer):
        self.data = data
        self.targets = targets
        self.tokenizer = tokenizer

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        text = self.data[idx]
        target = self.targets[idx]
        input_ids = self.tokenizer(text)

        return {
            "input_ids": torch.tensor(input_ids, dtype=torch.long),
            "target": torch.tensor(target, dtype=torch.long)
        }