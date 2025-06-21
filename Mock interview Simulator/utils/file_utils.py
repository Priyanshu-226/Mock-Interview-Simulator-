import os

def save_temp_file(file_bytes: bytes, filename: str = "temp.wav") -> str:
    filepath = os.path.join("temp", filename)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "wb") as f:
        f.write(file_bytes)
    return filepath