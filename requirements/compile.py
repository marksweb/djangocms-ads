#!/usr/bin/env python
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

if __name__ == "__main__":
    os.chdir(Path(__file__).parent)
    os.environ["CUSTOM_COMPILE_COMMAND"] = "requirements/compile.py"
    os.environ.pop("PIP_REQUIRE_VIRTUALENV", None)
    common_args = [
        "-m",
        "piptools",
        "compile",
        "--generate-hashes",
        "--allow-unsafe",
    ] + sys.argv[1:]
    subprocess.run(
        [
            "python3.8",
            *common_args,
            "--upgrade-package",
            "Django>=2.2,<2.3",
            "--upgrade-package",
            "django-cms==3.7",
            "-o",
            "py38-cms37-django22.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "python3.8",
            *common_args,
            "--upgrade-package",
            "Django>=2.2,<2.3",
            "--upgrade-package",
            "django-cms==3.7",
            "-o",
            "py38-cms37-django31.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "python3.8",
            *common_args,
            "--upgrade-package",
            "Django>=2.2,<2.3",
            "--upgrade-package",
            "django-cms==3.9",
            "-o",
            "py38-cms39-django22.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "python3.8",
            *common_args,
            "--upgrade-package",
            "Django>=3.1,<3.2",
            "--upgrade-package",
            "django-cms==3.9",
            "-o",
            "py38-cms39-django31.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "python3.8",
            *common_args,
            "--upgrade-package",
            "Django>=3.2,<4.0",
            "--upgrade-package",
            "django-cms==3.9",
            "-o",
            "py38-cms39-django32.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "python3.9",
            *common_args,
            "--upgrade-package",
            "Django>=2.2,<2.3",
            "--upgrade-package",
            "django-cms==3.9",
            "-o",
            "py39-cms39-django22.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "python3.9",
            *common_args,
            "--upgrade-package",
            "Django>=3.1,<3.2",
            "--upgrade-package",
            "django-cms==3.9",
            "-o",
            "py39-cms39-django31.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "python3.9",
            *common_args,
            "--upgrade-package",
            "Django>=3.2a1,<3.3",
            "--upgrade-package",
            "django-cms==3.9",
            "-o",
            "py39-cms39-django32.txt",
        ],
        check=True,
        capture_output=True,
    )
