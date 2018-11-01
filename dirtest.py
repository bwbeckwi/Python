

def replace_single_slash(slash):
    return slash.replace("\\","\\\\")


current_dir = input("Enter current directory to copy from: ")
target_dir = input("Enter target directory to copy to: ")

if "\\\\" not in current_dir:
    current_dir = replace_single_slash(current_dir)

if "\\\\" not in target_dir:
    target_dir = replace_single_slash(target_dir)

print("Current directory: " + current_dir)
print("Target directory: " + target_dir)
