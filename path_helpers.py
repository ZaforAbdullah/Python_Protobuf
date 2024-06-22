# path_helpers.py

from pathlib import Path
import os

def get_protobuf_output_dir(base_dir: str, output_dir: str) -> str:
    """
    Helper function to get the absolute path to the protobuf output directory.

    Args:
    - base_dir (str): Base directory name.
    - output_dir (str): Output directory name.

    Returns:
    - str: Absolute path to the protobuf output directory.
    """
    cwd_abs = Path().absolute()
    base_dir_path = Path(base_dir)
    abs_path_base_dir = os.path.join(cwd_abs, base_dir_path)
    return os.path.join(abs_path_base_dir, output_dir)
