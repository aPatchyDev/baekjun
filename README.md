# Repository for solutions to Baekjun

- Directory grouped by [solved.ac](https://solved.ac/) class

## Usage

Create and execute solution files by `./run.py <class #> <problem #>`

If `./class{class #}/{problem #}/{solution file}.py` is not found, a copy of `./template.py` is created.

### Optimized workflow

1. Open the folder in an editor with split view support.
2. Open 3 panels: solution file, `./in.txt`, terminal with shell
3. Create solution file with `./run.py`
4. Write code in solution file
5. Paste sample input in `./in.txt`
6. Execute solution with `./run.py`
7. Go back to #3 after completing a problem

### Options

- `-f / --file`: Set name of `{solution file}.py`
    - default = `sol.py`
- `-e / --editor`: Set command to execute when creating a new solution file
    - default = None
    - Command is executed as `[arg value, path of solution file]`
    - Useful for automatically opening the created file in the editor
