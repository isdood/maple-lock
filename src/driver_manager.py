import os
import shutil

def save_driver(driver_path, save_location):
    """
    Save OS-specific drivers to a specified location.

    :param driver_path: Path to the driver to be saved.
    :param save_location: Location where the driver should be saved.
    """
    if not os.path.exists(driver_path):
        raise FileNotFoundError(f"Driver not found at {driver_path}")

    if not os.path.exists(save_location):
        os.makedirs(save_location)

    driver_name = os.path.basename(driver_path)
    destination = os.path.join(save_location, driver_name)

    shutil.copy2(driver_path, destination)
    print(f"Driver saved to {destination}")

def load_driver(driver_path):
    """
    Load OS-specific drivers from a specified location.

    :param driver_path: Path to the driver to be loaded.
    """
    if not os.path.exists(driver_path):
        raise FileNotFoundError(f"Driver not found at {driver_path}")

    # Placeholder for actual implementation to load the driver
    print(f"Driver loaded from {driver_path}")
