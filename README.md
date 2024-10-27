# Thoughtful AI Technical Screen

Notes:

I use Enums instead of strings for the output to simplify refactoring, IDE
autocompletion, limit the location of typos (very DRY), and it feels more
readable.

Also, for storage I'm using float but if we needed it to be exact then we could
use Decimal to store the measurements instead.

On my own time and for fun I added a cli with rich to make the output pretty.
Then I spent time to make this work in replit, which I haven't used before.

## PROJECT STRUCTURE

The
[flat vs src layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
debate. Using `src` dirs does not work for scripts because python's import
module's path, aka `sys.path` by default does not know about `src`.

The work around is to install your project. But this is not a great development
experience. So you can change the python path manually with an env var or
runtime command like `PYTHONPATH=src`.

or use `poetry install` which is similar to `pip`'s editable installs.

## INSTALLATION: Poetry setup via pyproject.toml

Run `poetry install`

### Verify it's installed

Run `poetry run pip list` which will show all packages including this one.

> thoughtful-ai 0.1.0 /home/runner/ThoughtfulAutomation

You can see packages installed with `poetry show`

## RUNNING

### Adhoc in the replit shell

You can run adhoc commands against the main/sort function by creating a python
shell and importing `main`

1. In the replit shell type `python`
1. Enter `import main`
1. Use the function `main.sort()` as you want

```bash
~/ThoughtfulAutomation$ python
Python 3.11.9 (main, Apr  2 2024, 08:25:04) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import main
>>> main.sort()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sort() missing 4 required positional arguments: 'width', 'height', 'length', and 'mass'
```

### Adhoc using the cli script

`poetry run sort {weight} {height} {length} {mass}` e.g.
`poetry run sort 1 2 3 4`

## TESTING

Run `poetry run pytest`
