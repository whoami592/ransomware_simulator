import os
import time

def print_banner():
    banner = """
    ╔════════════════════════════════════════════╗
    ║   Ransomware Simulator (File Rename Only)   ║
    ║   Coded by Pakistani Ethical Hacker        ║
    ║   Mr Sabaz Ali Khan                        ║
    ╚════════════════════════════════════════════╝
    """
    print(banner)

def simulate_ransomware(directory, extension=".locked"):
    print_banner()
    print("[*] Starting Ransomware Simulation...")
    time.sleep(1)
    
    try:
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path) and not filename.endswith(extension):
                new_filename = filename + extension
                new_file_path = os.path.join(directory, new_filename)
                os.rename(file_path, new_file_path)
                print(f"[+] Renamed: {filename} -> {new_filename}")
                time.sleep(0.1)  # Small delay for visibility
    except Exception as e:
        print(f"[!] Error during simulation: {e}")
    
    print("[*] Simulation complete. Files have been 'locked' with .locked extension.")

if __name__ == "__main__":
    target_directory = input("Enter the target directory path for simulation: ")
    if os.path.isdir(target_directory):
        simulate_ransomware(target_directory)
    else:
        print("[!] Invalid directory path. Please try again.")