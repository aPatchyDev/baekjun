#!/usr/bin/python3

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("-f", "--file", default="sol.py", help="Solution file to run, default='sol.py'")
parser.add_argument("problemClass", metavar="class", type=int, help="Solved.ac Problem Class #")
parser.add_argument("problemID", metavar="id", type=int, help="Problem number")
parser.add_argument("-e", "--editor", metavar="editor", type=str, help="Editor to launch upon file creation")

args = parser.parse_args()

from pathlib import Path
prob_dir = Path(__file__).parent / f"class{args.problemClass}/{args.problemID}"
prob_file = prob_dir / Path(args.file).name
prob_in = Path(__file__).parent / "in.txt"

template_sol = Path(__file__).parent / "template.py"

if not prob_file.exists():
    prob_dir.mkdir(exist_ok=True, parents=True)
    if prob_file.exists() and input(f"Overwrite '{prob_file}' ? (y/n) ").strip() != 'y':
        raise FileExistsError(f"{prob_file} exists!")

    import shutil, subprocess
    shutil.copy(template_sol, prob_file)

    if args.editor is not None:
        subprocess.run([args.editor, prob_file])
else:
    import os, sys
    with open(prob_in) as f_in:
        os.dup2(f_in.fileno(), sys.stdin.fileno())

    py_path = sys.executable
    os.execv(py_path, [py_path, prob_file])
