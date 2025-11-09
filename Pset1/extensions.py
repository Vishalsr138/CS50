def main():
    file = input("File name: ").strip().lower()
    process(file)

def process(x):
    if "." in x:
        f_type = x.rsplit(".",1)[1]
    else:
        f_type = ""

    if f_type in ("gif", "jpeg", "png"):
        print(f"image/{f_type}", end="")
    elif f_type == "jpg":
        print("image/jpeg", end="")
    elif f_type == "pdf":
        print("application/pdf", end="")
    elif f_type == "txt":
        print("text/plain", end="")
    elif f_type == "zip":
        print("application/zip", end="")
    else:
        print("application/octet-stream", end="")

main()