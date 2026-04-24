import os
cwd = os.getcwd()
print("Current Working Directory:",  cwd)

folder_name = "test_folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Folder created:", folder_name)
else:
    print("Folder already exists:", folder_name)

print("Does folder exist?", os.path.exists(folder_name))
print("\nFiles and directories:")
for item in os.listdir():
    print(item)