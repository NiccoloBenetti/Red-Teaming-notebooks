def print_conda_commands(env_name):
    print("conda deactivate\n")
    print(f"conda create -n {env_name} python=3.13\n")
    print(f"conda activate {env_name}\n")
    print("pip install -r infra/requirements.txt\n")
    print(f"python -m ipykernel install --name {env_name} --user\n")

if __name__ == "__main__":
    env_name = input("Inserisci il nome dell'environment: ").strip()
    print_conda_commands(env_name)
