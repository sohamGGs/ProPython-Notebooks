import os

# Get current directory
print(f"Current Dir: {os.getcwd()}")

# List files in the current Colab session
print(f"Files: {os.listdir('.')}")

# Create a new directory
if not os.path.exists("Day_22_Test"):
    os.makedirs("Day_22_Test")
    print("Directory created!")