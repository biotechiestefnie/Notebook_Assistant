import json
import nbformat
import os

class NotebookParser:
    def __init__(self, notebook_path: str):
        self.notebook_path = notebook_path
        self.notebook = None
        self.code_cells = []

    def load_notebook(self, use_nbformat=True):
        if use_nbformat:
            with open(self.notebook_path, "r", encoding="utf-8") as f:
                self.notebook = nbformat.read(f, as_version=4)
            cells = self.notebook.cells
        else:
            with open(self.notebook_path, "r", encoding="utf-8") as f:
                self.notebook = json.load(f)
            cells = self.notebook["cells"]

        self.code_cells = []
        for cell in cells:
            if cell["cell_type"] == "code":
                source = cell["source"]
                if isinstance(source, list):
                    source = "".join(source)
                self.code_cells.append(source)

    def explain_cells(self):
        explanations = []
        for i, code in enumerate(self.code_cells, start=1):
            if "import" in code:
                msg = "This cell imports libraries."
            elif "print" in code:
                msg = "This cell prints output."
            elif "def " in code:
                msg = "This cell defines a function."
            else:
                msg = "This cell runs computations or analysis."
            explanations.append((i, code.strip(), msg))
        return explanations


if __name__ == "__main__":
    # Go up one folder from src/ to project root
    base_dir = os.path.dirname(os.path.dirname(__file__))
    notebook_path = os.path.join(base_dir, "notebooks", "example_notebook.ipynb")

    parser = NotebookParser(notebook_path)
    parser.load_notebook(use_nbformat=True)
    for idx, code, explanation in parser.explain_cells():
        print(f"Cell {idx}:\n{code}\n→ {explanation}\n")

