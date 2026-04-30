import pandas as pd

def read_cfd_data(file_path):
    """
    Read sample CFD/CPFD exported data.

    Parameters
    ----------
    file_path : str
        Path to the exported CSV file.

    Returns
    -------
    pandas.DataFrame
        Loaded simulation data.
    """
    data = pd.read_csv(file_path)
    return data

if __name__ == "__main__":
    data = read_cfd_data("../examples/sample_cfd_data.csv")
    print(data.head())
    print(data.describe())
