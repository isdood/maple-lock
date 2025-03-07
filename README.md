# maple-lock
A tool which can be installed to a USB to manage logins, passwords, etc. Pluggin in an active maple-lock USB should launch it's interface on Linux, Android, IOS and Windows.

## Installation

### Linux
1. Clone the repository:
   ```sh
   git clone https://github.com/isdood/maple-lock.git
   cd maple-lock
   ```
2. Install the required dependencies:
   ```sh
   sudo apt-get install python3-pip
   pip3 install -r requirements.txt
   ```
3. Run the tool:
   ```sh
   python3 src/main.py
   ```

### Android
1. Clone the repository to your Android device.
2. Install the required dependencies using a Python environment like Termux.
3. Run the tool using the Python environment.

### IOS
1. Clone the repository to your IOS device.
2. Install the required dependencies using a Python environment like Pythonista.
3. Run the tool using the Python environment.

### Windows
1. Clone the repository:
   ```sh
   git clone https://github.com/isdood/maple-lock.git
   cd maple-lock
   ```
2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the tool:
   ```sh
   python src/main.py
   ```

## Usage

1. Plug in the active maple-lock USB.
2. The tool will automatically launch its interface on the supported platform.

## Evolving Theme Engine

The tool incorporates an evolving theme engine that adapts to users' wallpapers and color preferences. To enable this feature, follow the instructions below:

1. Ensure that the tool has access to the user's wallpaper and color preferences.
2. The theme engine will automatically adapt the interface based on the detected preferences.

## Driver Management

The tool now supports saving and loading OS-specific drivers. This feature allows you to quickly set up any OS with your credentials, logins, and drivers.

### Saving OS-specific drivers

To save your OS-specific drivers, follow these steps:

1. Ensure that the tool is running on the target OS.
2. Use the `save_driver` function to save the drivers to a specified location.

### Loading OS-specific drivers

To load your OS-specific drivers, follow these steps:

1. Ensure that the tool is running on the target OS.
2. Use the `load_driver` function to load the drivers from the specified location.
