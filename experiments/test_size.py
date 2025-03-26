
from torch import nn
import torch
import pandas as pd

class MDN(nn.Module):
    """A mixture density network layer
    The input maps to the parameters of a MoG probability distribution, where
    each Gaussian has O dimensions and diagonal covariance.
    Arguments:
        in_features (int): the number of dimensions in the input
        out_features (int): the number of dimensions in the output
        num_gaussians (int): the number of Gaussians per output dimensions
    Input:
        minibatch (BxD): B is the batch size and D is the number of input
            dimensions.
    Output:
        (pi, sigma, mu) (BxG, BxGxO, BxGxO): B is the batch size, G is the
            number of Gaussians, and O is the number of dimensions for each
            Gaussian. Pi is a multinomial distribution of the Gaussians. Sigma
            is the standard deviation of each Gaussian. Mu is the mean of each
            Gaussian.
    """

    def __init__(self, in_features, out_features, device):
        super(MDN, self).__init__()
        self.in_features = in_features
        self.out_features = out_features
        self.pi = nn.Sequential(
            nn.Linear(in_features, out_features), nn.Softmax(dim=1)
        )
        self.sigma = nn.Linear(in_features, out_features )
        self.mu = nn.Linear(in_features, out_features )

        self.pi = self.pi.to(device)
        self.mu = self.mu.to(device)
        self.sigma = self.sigma.to(device)

    def forward(self, minibatch):
        pi = self.pi(minibatch)
        sigma = torch.exp(self.sigma(minibatch))
        sigma = sigma.view(-1, self.num_gaussians, self.out_features)
        mu = self.mu(minibatch)
        mu = mu.view(-1, self.num_gaussians, self.out_features)
        return pi, sigma, mu

device = 'cpu'

# n_mdn_layer_node = 310 #  832.15 KB
# n_mdn_layer_node = 315 #  857.87 KB
# n_mdn_layer_node = 320 #  883.98 KB
# n_mdn_layer_node = 330 #  937.38 KB
# n_mdn_layer_node = 340 #  992.34 KB
# n_mdn_layer_node = 350 # 1048.87 KB
# n_mdn_layer_node = 360 # 1106.95 KB
# n_mdn_layer_node = 380 # 1227.81 KB
# n_mdn_layer_node = 390 # 1290.59 KB
# n_mdn_layer_node = 400 # 1354.92 KB
n_mdn_layer_node = 410 # 1420.82 KB
# n_mdn_layer_node = 420 # 1488.28 KB
# n_mdn_layer_node = 430 # 1557.30 KB
# n_mdn_layer_node = 440 # 1627.89 KB
# n_mdn_layer_node = 450 # 1700.04 KB
# n_mdn_layer_node = 460 # 1773.75 KB
# n_mdn_layer_node = 470 # 1849.02 KB
# n_mdn_layer_node = 490 # 2004.26 KB
# n_mdn_layer_node = 500 # 2084.22 KB
# n_mdn_layer_node = 510 # 2165.74 KB
# n_mdn_layer_node = 520 # 2248.83 KB
# n_mdn_layer_node = 530 # 2333.48 KB
# n_mdn_layer_node = 550 # 2507.46 KB
# n_mdn_layer_node = 560 # 2596.80 KB
# n_mdn_layer_node = 570 # 2687.70 KB
# n_mdn_layer_node = 590 # 2874.18 KB
# n_mdn_layer_node = 600 # 2969.77 KB
# n_mdn_layer_node = 610 # 3066.91 KB
# n_mdn_layer_node = 620 # 3165.62 KB
# n_mdn_layer_node = 650 # 3471.13 KB
# n_mdn_layer_node = 700 # 4011.56 KB

# n_mdn_layer_node = 840 # 5732.58 KB
# n_mdn_layer_node = 850 # 5867.23 KB
# n_mdn_layer_node = 870 # 6141.21 KB
# n_mdn_layer_node = 890 # 6421.45 KB
# n_mdn_layer_node = 900 # 6563.91 KB
# n_mdn_layer_node = 920 # 6853.52 KB
# n_mdn_layer_node = 950 # 7299.65 KB
# n_mdn_layer_node = 960 # 7451.48 KB
# n_mdn_layer_node = 970 # 7604.88 KB
# n_mdn_layer_node = 980 # 7759.84 KB
# n_mdn_layer_node = 1000 # 8074.45 KB

unit2size = []
for n_mdn_layer_node in range(310, 1000, 10):
    reg = nn.Sequential(
        nn.Linear(1, n_mdn_layer_node),
        nn.Tanh(),
        nn.Linear(n_mdn_layer_node, n_mdn_layer_node),
        nn.Tanh(),
        nn.Dropout(0.1),
        MDN(n_mdn_layer_node, 20, device),
    )

    kde = nn.Sequential(
        nn.Linear(2, n_mdn_layer_node),  # self.dim_input
        nn.Tanh(),
        nn.Linear(n_mdn_layer_node, n_mdn_layer_node),
        nn.Tanh(),
        nn.Dropout(0.1),
        MDN(n_mdn_layer_node, 5, device),
    )

    size = sum([p.nelement() * p.element_size() for p in reg.parameters()])
    size += sum([p.nelement() * p.element_size() for p in kde.parameters()])

    # print(f"Model size: {size / 1024:.2f} KB")
    unit2size.append({"units": n_mdn_layer_node, "size": round(size / 1024, 2)})

# Save the results
df = pd.DataFrame(unit2size)
df.to_csv("unit2size.csv", index=False)

