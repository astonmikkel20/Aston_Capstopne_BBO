import re
import ast
from pathlib import Path
import numpy as np


def parse_inputs_txt(txt_path):
    """
    Parse an inputs.txt file that may contain multiple blocks like:
    [array([...]), array([...]), ...]
    [array([...]), array([...]), ...]

    It extracts the LAST block and returns a list of 8 numpy arrays.
    """
    text = Path(txt_path).read_text(encoding="utf-8")

    # Split into non-empty lines
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    # Group consecutive lines into bracketed blocks
    blocks = []
    current_block = []

    for line in lines:
        if line.startswith("["):
            current_block = [line]
        elif current_block:
            current_block.append(line)

        if current_block and line.endswith("]"):
            block_text = " ".join(current_block)
            blocks.append(block_text)
            current_block = []

    if not blocks:
        raise ValueError(f"No valid input blocks found in {txt_path}")

    # Use the last full block only
    last_block = blocks[-1]

    # Extract every array([...]) from the last block
    matches = re.findall(r"array\((\[[^\)]*?\])\)", last_block, flags=re.DOTALL)

    parsed = []
    for m in matches:
        arr = np.array(ast.literal_eval(m), dtype=float)
        parsed.append(arr)

    return parsed


def parse_outputs_txt(txt_path):
    """
    Parse an outputs.txt file that may contain multiple blocks like:
    [np.float64(...), ...]
    [np.float64(...), ...]

    It extracts the LAST block and returns a list of floats.
    """
    text = Path(txt_path).read_text(encoding="utf-8")

    # Replace np.float64(x) -> x
    text = re.sub(r"np\.float64\((.*?)\)", r"\1", text)

    lines = [line.strip() for line in text.splitlines() if line.strip()]

    blocks = []
    current_block = []

    for line in lines:
        if line.startswith("["):
            current_block = [line]
        elif current_block:
            current_block.append(line)

        if current_block and line.endswith("]"):
            block_text = " ".join(current_block)
            blocks.append(block_text)
            current_block = []

    if not blocks:
        raise ValueError(f"No valid output blocks found in {txt_path}")

    # Use the last block only
    last_block = blocks[-1]
    values = ast.literal_eval(last_block)

    return [float(v) for v in values]


def update_week_data(prev_week, new_week, inputs_txt_path, outputs_txt_path, project_root):
    """
    Build the new week's accumulated .npy data by appending the new returned
    input/output for each function to the previous week's dataset.
    """
    project_root = Path(project_root)
    prev_root = project_root / "data" / f"week_{prev_week}"
    new_root = project_root / "data" / f"week_{new_week}"

    new_inputs = parse_inputs_txt(inputs_txt_path)
    new_outputs = parse_outputs_txt(outputs_txt_path)

    if len(new_inputs) != 8 or len(new_outputs) != 8:
        raise ValueError(
            f"Expected 8 inputs and 8 outputs, got {len(new_inputs)} inputs and {len(new_outputs)} outputs."
        )

    for fn in range(1, 9):
        prev_function_folder = prev_root / f"function_{fn}"
        new_function_folder = new_root / f"function_{fn}"
        new_function_folder.mkdir(parents=True, exist_ok=True)

        old_inputs_path = prev_function_folder / "initial_inputs.npy"
        old_outputs_path = prev_function_folder / "initial_outputs.npy"

        if not old_inputs_path.exists():
            raise FileNotFoundError(f"Missing file: {old_inputs_path}")
        if not old_outputs_path.exists():
            raise FileNotFoundError(f"Missing file: {old_outputs_path}")

        X_old = np.load(old_inputs_path)
        y_old = np.load(old_outputs_path)

        x_new = np.array(new_inputs[fn - 1], dtype=float).reshape(1, -1)
        y_new = np.array([new_outputs[fn - 1]], dtype=float)

        if X_old.shape[1] != x_new.shape[1]:
            raise ValueError(
                f"Dimension mismatch in function {fn}: "
                f"previous data has dim {X_old.shape[1]}, "
                f"new input has dim {x_new.shape[1]}"
            )

        X_updated = np.vstack([X_old, x_new])
        y_updated = np.concatenate([y_old, y_new])

        np.save(new_function_folder / "initial_inputs.npy", X_updated)
        np.save(new_function_folder / "initial_outputs.npy", y_updated)

        print(
            f"Function {fn}: "
            f"{X_old.shape[0]} -> {X_updated.shape[0]} points saved in {new_function_folder}"
        )

    print(f"\nWeek {new_week} data created successfully.")


if __name__ == "__main__":
    PROJECT_ROOT = Path(r"D:\Capstone_BBO")

    # Change only this each week
    NEW_WEEK = 21
    PREV_WEEK = NEW_WEEK - 1

    INPUTS_TXT = PROJECT_ROOT / "data" / f"week_{NEW_WEEK}" / "inputs.txt"
    OUTPUTS_TXT = PROJECT_ROOT / "data" / f"week_{NEW_WEEK}" / "outputs.txt"

    if not INPUTS_TXT.exists():
        raise FileNotFoundError(f"Missing inputs file: {INPUTS_TXT}")
    if not OUTPUTS_TXT.exists():
        raise FileNotFoundError(f"Missing outputs file: {OUTPUTS_TXT}")

    print(f"Project root: {PROJECT_ROOT}")
    print(f"Previous week: {PREV_WEEK}")
    print(f"New week: {NEW_WEEK}")
    print(f"Inputs txt: {INPUTS_TXT}")
    print(f"Outputs txt: {OUTPUTS_TXT}\n")

    update_week_data(
        prev_week=PREV_WEEK,
        new_week=NEW_WEEK,
        inputs_txt_path=INPUTS_TXT,
        outputs_txt_path=OUTPUTS_TXT,
        project_root=PROJECT_ROOT,
    )