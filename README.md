# pygbm

## Installation

To install, run:
```bash
git clone https://github.com/yourusername/pygbm_package.git
cd pygbm_package
pip install -e .
```

The **pygbm** package is a Python package designed to simulate Geometric Brownian Motion.

## Features

- Base `GBMSimulator` class with core attributes and methods


## Usage

### Python Interface

Here's a quick example of how to use the package:

```python
from pygbm.gbm_simulation import GBMSimulator
simulator = GBMSimulator(y0=1.0, mu=0.05, sigma=0.2)
t_values, y_values = simulator.simulate_path(T=1.0, N=100)
simulator.plot_path(t_values, y_values, output="gbm_plot.png")
```

### Command-line Interface

```bash
pygbm  --y0 1.0 --mu 0.05 --sigma 0.2 --T 1.0 --N 100 --output gbm_plot.png
```


## Documentation

Visit our [documentation page](https://your-readthedocs-url-here).

## Contributing

Contributions are welcome! Fork our repository and submit a pull request.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
