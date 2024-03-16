#! /usr/bin/env python3

"""
Usage: python3 -m anafile <filenames...>

Note: Not all function bodies are parsed completely.
"""

from pathlib import Path
from sys import argv
import re2 as re


def get_cpp_function_impls_name_and_body(code: str) -> list[tuple[str, str]]:
    """Extracts the implemented functions' name and body from a C++ code snippet."""
    return re.findall(r"(\w+)\s*\([^)]*\)\s*\{([^}]*)\}", code)


def get_cpp_invocations(body: str) -> list[str]:
    """Extracts the function invocations from a C++ function body."""
    return re.findall(r"(\w+)\s*\([^)]*\)\s*;", body)


def is_cpp_statement_keywords(term: str) -> bool:
    """Returns True if the term is a C++ statement keyword."""
    return term in {
        "if",
        "else",
        "while",
        "for",
        "do",
        "switch",
        "case",
        "default",
        "break",
        "continue",
        "return",
        "goto",
        "try",
        "catch",
        "throw",
        "using",
        "namespace",
        "typedef",
        "static_assert",
        "asm",
    }


if __name__ == "__main__":
    # Define the state
    cpp_invocation_relations: dict[str, dict[str, set[str]]] = {}
    cpp_function_names: set[str] = set()

    # Build the state
    for path in argv[1:]:
        cpp_invocation_relations[path] = {}
        for name, body in get_cpp_function_impls_name_and_body(Path(path).read_text()):
            if is_cpp_statement_keywords(name):
                continue
            invocations = set(get_cpp_invocations(body))

            cpp_function_names.add(name)
            cpp_invocation_relations[path][name] = invocations

    # Organize the state
    for functions in cpp_invocation_relations.values():
        for name, invocations in functions.items():
            functions[name] = list(filter(cpp_function_names.__contains__, invocations))

    # Print the state
    for path, functions in cpp_invocation_relations.items():
        print(f"[{path}]: ")
        for name in sorted(functions.keys()):
            print(f"  {name}")
        print("  ")
        for name, invocations in functions.items():
            for invocation in invocations:
                print(f"  {name} --> {invocation}")
        print()
