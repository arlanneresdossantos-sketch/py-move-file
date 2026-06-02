import os
from pathlib import Path


def move_file(command: str) -> None:
    arguments = command.split()

    if len(arguments) != 3:
        return

    operation, src, dest = arguments

    if operation != "mv":
        return

    src_path = Path(src)
    dest_path = Path(dest)

    if not src_path.is_file():
        return

    if dest.endswith("/") or dest.endswith("\\") or dest_path.is_dir():
        dest_path = dest_path / src_path.name

    dest_dir = str(dest_path.parent)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    with open(src_path, "rb") as file_in, open(dest_path, "wb") as file_out:
        file_out.write(file_in.read())

    os.remove(str(src_path))