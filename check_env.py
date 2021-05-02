
# Standard library imports
import importlib.util
import subprocess
import sys

package_list_name = ['psutil', 'python-dotenv']

for package in package_list_name:
    spec = importlib.util.find_spec(package)
    if spec is None:
        try:
            print(f"Package: {package} isn't installed in Python environment, it will be installed")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package])
            print(f"Package {package} was installed successfully")
        except EnvironmentError as e:
            print(f"Error during the installation of {package}: {e}")
    else:
        print(f"Package {package} it is already installed, skipping installation")
