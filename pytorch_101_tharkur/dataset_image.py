import torch
import numpy as np
import cv2


class CustomDataset:
    def __init__(self, image_paths, targets, argumentation=None):
        self.image_paths = image_paths
        self.targets = targets
        self.argumentation = argumentation

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        target = self.targets[idx]
        image = cv2.imread(self.image_paths[idx])
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        if self.argumentation is not None:
            argumented = self.argumentation(image=image)
            image = argumented["image"]

        image = np.transpose(image, (2, 0, 1))

        return {
            "image": torch.tensor(image),
            "target": torch.tensor(target)
        }

