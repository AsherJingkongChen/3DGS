"""
Prerequisites:
- `mmdc`: Mermaid CLI
  + Installation: `npm install -g @mermaid-js/mermaid-cli`
"""

from pathlib import Path
from subprocess import run

old_image_paths = Path.cwd().glob("**/*-*.svg")
original_markdown_paths = Path.cwd().glob("**/*.orig.md")
list(map(Path.unlink, old_image_paths))

for orig_path in original_markdown_paths:
    new_path = orig_path.parent / Path(orig_path.stem).with_suffix(".md")
    run(["mmdc", "-i", orig_path, "-o", new_path], check=True)
