from functions import encode, decode
import os


def encode_non_text_file(path: str, output_file: str | None = None, o_encoding: str = "UTF-8") -> str | None:
    d: list[bytes] = []
    try:
        with open(path, 'rb') as f:
            d = f.readlines()
    except FileNotFoundError:
        print("File " + path + " not found")
        return

    str_data = [b.hex(' ') for b in d]
    estr_data = '\n'.join([encode(sd) for sd in str_data])

    if output_file is not None:
        os.makedirs(os.path.dirname(output_file), 0o777, exist_ok=True)
        with open(output_file, 'w', encoding=o_encoding) as f:
            f.write(estr_data)

    return estr_data


def decode_non_text_file(path: str, output_file: str = "./output", i_encoding: str = "UTF-8") -> None:
    d: list[str] = []
    try:
        with open(os.path.abspath(path), 'r', encoding=i_encoding) as f:
            d = f.readlines()
    except FileNotFoundError:
        print("File " + path + " not found.")
        return

    data = ''.join(d).split("\n")
    hex_data = [decode(dat) for dat in data]
    bytes_data = [bytes.fromhex(hd) for hd in hex_data]

    os.makedirs(os.path.dirname(output_file), 0o777, exist_ok=True)
    with open(os.path.abspath(output_file), 'wb') as bf:
        bf.writelines(bytes_data)


if __name__ == "__main__":
    print("Encoding...")
    encode_non_text_file(r"/home/igor/Music/Toby Fox/Undertale/Toby Fox - 001. Once Upon a Time (UNDERTALE Soundtrack) - Toby Fox.m4a", output_file="/home/igor/Desktop/OnceUponATime.txt")
    print("Done!")
    print("Decoding...")
    decode_non_text_file(r"/home/igor/Desktop/OnceUponATime.txt")
    print("Done!")
