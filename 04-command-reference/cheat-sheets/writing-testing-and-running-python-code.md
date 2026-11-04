| Command | What you can do with it |
| --- | --- |
| `python3 --version` | Print the Python version. |
| `python3 -m venv .venv` | Create a project-local virtual environment. |
| `. .venv/bin/activate` | Activate that environment in the current shell. |
| `python3 -m pip --version` | Identify pip for the selected Python interpreter. |
| `python3 -m pip list` | List installed Python packages. |
| `python3 -m pip show PACKAGE` | Inspect installed package metadata. |
| `python3 -m pip install PACKAGE` | Install a package into the selected Python environment. |
| `python3 -m pip install -r requirements.txt` | Install dependencies listed in a requirements file. |
| `python3 -m pip check` | Check installed package dependency compatibility. |
| `python3 -m pip freeze` | Print installed package requirements in freeze format. |
| `python3 -m compileall -q DIRECTORY` | Compile Python files to bytecode, writing cache files. |
| `python3 SCRIPT.py` | Run a Python script. |
| `python3 -m unittest discover` | Discover and run unittest tests. |
| `python3 -m pytest` | Run tests with the optional pytest package. |
| `python3 -m pdb SCRIPT.py` | Run a script under Python's interactive debugger. |
| `python3 -m cProfile SCRIPT.py` | Profile a script's function calls. |
| `python3 -m timeit 'sum(range(1000))'` | Measure a short Python expression's execution time. |
| `python3 -m http.server --bind 127.0.0.1 8000` | Serve the current directory over HTTP bound only to loopback. |
| `python3 -c 'import sys; print(sys.executable)'` | Print the selected Python executable path. |
