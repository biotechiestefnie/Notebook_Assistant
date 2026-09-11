import nbformat

class NotebookParser:
    """
    NotebookParser loads a Jupyter notebook (.ipynb) and extracts code cells.
    It can generate simple explanations for each cell.
    """

    def __init__(self, notebook_path: str):
        self.notebook_path = notebook_path
        self.notebook = None
        self.code_cells = []

    def load_notebook(self):
        """Load the notebook file into memory."""
        with open(self.notebook_path, "r", encoding="utf-8") as f:
            self.notebook = nbformat.read(f, as_version=4)
        self.code_cells = [
            cell["source"] for cell in self.notebook.cells if cell["cell_type"] == "code"
        ]

    def explain_cells(self):
        """Generate simple explanations for each code cell."""
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
    parser = NotebookParser("e    parser = NotebookParse  parser.load_notebook()
    for idx, code, explanation in parser.explain_cells():
        print(f"Cell {idx}:\n{code}\n→ {explanation}\n")
