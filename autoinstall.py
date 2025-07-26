import subprocess
import os
import sys

REQUIREMENTS_FILE = "requirements.txt"
OFFLINE_DIR = "offline_libs"

def install_package(pkg_name):
    try:
        print(f"🔄 Installing {pkg_name} from PyPI...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg_name])
        print(f"✅ Installed: {pkg_name}")
    except subprocess.CalledProcessError:
        print(f"❌ Failed to install {pkg_name} from PyPI. Trying offline fallback...")
        try_offline_install(pkg_name)

def try_offline_install(pkg_name):
    wheel_files = os.listdir(OFFLINE_DIR)
    match = [f for f in wheel_files if pkg_name.lower() in f.lower()]
    if match:
        wheel_path = os.path.join(OFFLINE_DIR, match[0])
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", wheel_path])
            print(f"📦 Offline installed: {pkg_name} → {match[0]}")
        except subprocess.CalledProcessError:
            print(f"❌ Offline install failed for {pkg_name}")
    else:
        print(f"⚠ No offline .whl found for {pkg_name}")

def main():
    if not os.path.exists(REQUIREMENTS_FILE):
        print(f"❌ No {REQUIREMENTS_FILE} found.")
        return

    with open(REQUIREMENTS_FILE, "r") as f:
        packages = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    for pkg in packages:
        install_package(pkg)

if __name__ == "__main__":
    main()
