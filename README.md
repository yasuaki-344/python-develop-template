# python-develop-template

## Building development environment

### Setup Python

If `pyenv` is not installed, you can install `pyenv` as follows:

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

### Install dependency packages

If `poetry` is not installed, you can install as follows:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Install dependency packages as follows:

```bash
poetry shell
poetry install
```
