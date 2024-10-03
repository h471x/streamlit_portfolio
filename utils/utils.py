import base64

# Convert a file to base64
def file_to_base64(file_path: str) -> str:
    with open(file_path, "rb") as file:
        data = file.read()
        encoded_file = base64.b64encode(data).decode("utf-8")
    return encoded_file

# generate customized link
def custom_link(link: str) -> str:
    return f"""<span style="font-size: 18px;">{link}</span>"""