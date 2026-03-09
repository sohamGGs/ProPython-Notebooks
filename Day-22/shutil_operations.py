import shutil
import os

# Create a dummy file
with open("source.txt", "w") as f: f.write("Hello Automation!")

# Copy file
shutil.copy("source.txt", "destination.txt")

# Move file into the folder we created in script 1
shutil.move("destination.txt", "Day_22_Test/destination.txt")

print("File moved successfully.")