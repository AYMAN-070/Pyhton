import sys
import importlib


def check_dependencies() -> dict:
    required = ["pandas", "numpy", "matplotlib", "requests"]
    versions = {}
    print("Loading status: Loading programs...")
    for program in required:
        try:
            """Like using classic import"""
            module = importlib.import_module(program)
            """Looking for __version__ attribut in module"""
            version = getattr(module, "__version__", "Unknown")
            versions[program] = version
            print(f"[OK] {program} ({version}) ready")
        except ImportError:
            print(f"[ERROR] {program} is missing from the construct!")
            print("Use pip install -r requirements.txt or poetry install")
            sys.exit(1)
    return versions


def matrix_analysis() -> None:
    """Analyse matrix data and generate a visualisation"""
    try:
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        print("Analyzing Matrix data")
        """Generate 1000 random numbers centred at 0 with standard
        deviation of 1"""
        data = np.random.normal(0, 1, 1000)
        """Creat like Excel table of data"""
        df = pd.DataFrame(data, columns=['Signal_intensity'])
        print(f"Processing {len(df)} data points...")
        """Count how many times each value appears and draw a histogram"""
        plt.figure(figsize=(10, 6))
        plt.hist(df['Signal_intensity'], bins=30, color='lime',
                 edgecolor='black')
        plt.title("Matrix Neural Load Analysis")
        plt.grid(True, alpha=0.3)
        """Save result"""
        output_file = "Matrix_analysis.png"
        plt.savefig(output_file)
        print(f"Analysis complete! Results saved to: {output_file}")
    except Exception as e:
        print(f"CRITICAL ERROR: The simulation collapsed: {e}")


if __name__ == "__main__":
    versions = check_dependencies()
    matrix_analysis()
