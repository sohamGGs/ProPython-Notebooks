import argparse
import os

def bulk_rename(prefix, folder):
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    for i, filename in enumerate(files):
        ext = filename.split(".")[-1]
        new_name = f"{prefix}_{i}.{ext}"
        os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
    print(f"Renamed {len(files)} files.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bulk File Renamer")
    parser.add_argument("prefix", help="Prefix for the new filenames")
    parser.add_argument("--dir", default=".", help="Directory to process (default: current)")
    
    args = parser.parse_args()
    # bulk_rename(args.prefix, args.dir) # Uncomment to use safely
    print(f"Ready to rename files in '{args.dir}' with prefix '{args.prefix}'")