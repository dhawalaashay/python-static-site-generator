"""
The Site class will set the configuration values and
create the root structure of our static site.
We will create a command line tool using Typer Library
"""

from pathlib import Path


class Site:
    # class constructor
    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = self.dest / path.relative_to(self.source)
        # Path.mkdir(directory, parents=True, exist_ok=True)
        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        #Path.mkdir(self.dest, parents=True, exist_ok=True)
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
