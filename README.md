# Snell\_ND

> A collection of Python scripts to compute and visualize the generalized Snell's Law, tailored for nondestructive testing and refractive index analysis.

## 📄 Project Overview

This repository provides tools to:

* **Calculate refraction angles** according to the generalized Snell's Law for different media.
* **Generate plots** illustrating incident vs. refracted angles over a range of refractive indices.

These scripts are useful for researchers and engineers working on optical/acoustic wave propagation in nondestructive evaluation (NDE) contexts.

## 🛠 Repository Structure

```bash
snell_ND/
├── generalized_snell.py        # Computes refracted angle based on user inputs
├── generalized_snell_plot.py   # Plots incident vs. refracted angles for given media
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

## 🔧 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/vhrm19/snell_ND.git
   cd snell_ND
   ```

2. **Create a virtual environment** (recommended)

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\\Scripts\\activate # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   * **Primary libraries:** `numpy`, `matplotlib`

## 🚀 Usage

### 1. Calculate a single refraction angle

```bash
python generalized_snell.py --incident-angle 30 --n1 1.0 --n2 1.5
```

**Parameters:**

* `--incident-angle`: Angle of incidence in degrees.
* `--n1`: Refractive index of the first medium.
* `--n2`: Refractive index of the second medium.

**Output:**

* Prints the computed refracted angle in degrees.

### 2. Plot incident vs. refracted angles

```bash
python generalized_snell_plot.py --n1 1.0 --n2 1.5 --max-angle 90
```

**Parameters:**

* `--n1`: Refractive index of the first medium.
* `--n2`: Refractive index of the second medium.
* `--max-angle`: Maximum incident angle to plot (in degrees).

**Output:**

* Displays a plot of incident vs. refracted angles.
* Saves the plot to `snell_plot.png` by default.

## 📈 Example Output

![Snell Plot](snell_plot.png)
*Example plot of incident vs. refracted angles.*

## 📝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## 📜 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

*Developed by Victor H. R. Machado*
