import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal, getcontext

# ----------------------------
# Chudnovsky pi computation
# ----------------------------
def compute_pi(digits):
    getcontext().prec = digits + 5

    C = 426880 * Decimal(10005).sqrt()
    M = Decimal(1)
    L = Decimal(13591409)
    X = Decimal(1)
    K = Decimal(6)
    S = Decimal(L)

    for i in range(1, digits // 14 + 2):
        M = (M * (K**3 - 16*K)) / (Decimal(i)**3)
        L += Decimal(545140134)
        X *= Decimal(-262537412640768000)
        S += (M * L) / X
        K += Decimal(12)

    return C / S


# ----------------------------
# Spiral coordinates
# ----------------------------
def get_spiral_coords(n_points):
    theta = np.linspace(0, 50 * np.pi, n_points)
    r = np.sqrt(theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y


# ----------------------------
# Generate pi digits
# ----------------------------
digits = 100000
pi_val = compute_pi(digits)

pi_str = str(pi_val).replace('.', '')[:digits]
digit_values = [int(d) for d in pi_str]


# ----------------------------
# Plot
# ----------------------------
x, y = get_spiral_coords(digits)

plt.figure(figsize=(10, 10))
plt.title(rf"First ${digits}$ digits of $\pi$ on a spiral", fontsize=16, pad=20)
scatter = plt.scatter(x, y, c=digit_values, cmap="tab10", s=25, vmin=0, vmax=9, alpha=1.0, edgecolors='none')

cbar = plt.colorbar(scatter, pad=0.02, shrink=0.8)
cbar.set_label("Digit", fontsize=12)

plt.axis("equal")
plt.axis("off")
plt.tight_layout()
plt.margins(0.01)
plt.savefig("spiral.png", dpi=300, bbox_inches="tight", pad_inches=0.05)
