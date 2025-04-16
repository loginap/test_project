from pathlib import Path
import os
(Path(Path.cwd()) / "test_folder").mkdir(parents=True, exist_ok=True)
for i in range(10):
    (Path(Path.cwd()) / "test_folder"/ f"txt_file{i+1}.txt").write_text(f"Привет n {i+1}")
    if i %2:
        os.remove(str((Path(Path.cwd()) / "test_folder"/ f"txt_file{i+1}.txt")))