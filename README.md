# Red-Teaming-notebooks README
Red Teaming Notebooks

## Conda Environment Installation
```
conda create -n redTA-env python=3.12 -y
conda activate redTA-env
pip install -r ./infra/requirements.txt
jupyter kernelspec uninstall redTA-env -y
python -m ipykernel install --user --name=redTA-env
```
