import yaml

# 讀取 environment.yml
with open('environment.yml', 'r') as env_file:
    env_content = yaml.safe_load(env_file)

# 讀取 requirements.txt
with open('requirements.txt', 'r') as req_file:
    req_lines = req_file.readlines()

# 提取 Conda 套件名稱和版本
conda_packages = {}
for pkg in env_content['dependencies']:
    if isinstance(pkg, str):
        name, version = pkg.split('=')
        conda_packages[name] = version

# 提取 Pip 套件名稱和版本
pip_packages = {}
for line in req_lines:
    line = line.strip()
    if '==' in line:
        pkg, version = line.split('==')
        if pkg not in conda_packages:
            pip_packages[pkg] = version
    else:
        print(f"Skipping invalid line in requirements.txt: {line}")

# 合併 Conda 和 Pip 套件到 requirements.txt
with open('combined_requirements.txt', 'w') as combined_file:
    for pkg, version in conda_packages.items():
        combined_file.write(f"{pkg}=={version}\n")
    for pkg, version in pip_packages.items():
        combined_file.write(f"{pkg}=={version}\n")

print("合併完成，生成的文件為 combined_requirements.txt")