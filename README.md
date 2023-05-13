# python-develop-template

## Building development environment

### Setup Python

If `pyenv` is not installed, `pyenv` as follows:

```bash
curl https://pyenv.run | bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
```

Install and set the specified python version as follows:

```bash
pyenv install -l
pyenv install [python-version]
pyenv local [python-version]
```

### Install `Poetry`

```shell
pip install -r requirements.txt
```
