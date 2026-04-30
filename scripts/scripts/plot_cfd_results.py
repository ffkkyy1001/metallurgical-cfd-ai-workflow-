import pandas as pd
import matplotlib.pyplot as plt

def plot_velocity_temperature(file_path):
    """
    Plot velocity and temperature profiles from sample CFD data.
    """
    data = pd.read_csv(file_path)

    plt.figure()
    plt.plot(data["x"], data["velocity"], marker="o")
    plt.xlabel("Position x")
    plt.ylabel("Velocity")
    plt.title("Sample Velocity Profile")
    plt.tight_layout()
    plt.savefig("../examples/sample_velocity_profile.png", dpi=300)

    plt.figure()
    plt.plot(data["x"], data["temperature"], marker="o")
    plt.xlabel("Position x")
    plt.ylabel("Temperature")
    plt.title("Sample Temperature Profile")
    plt.tight_layout()
    plt.savefig("../examples/sample_temperature_profile.png", dpi=300)

if __name__ == "__main__":
    plot_velocity_temperature("../examples/sample_cfd_data.csv")
