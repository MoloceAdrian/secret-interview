import os
import sys

BUFSIZE = 1 << 15

def output_file_name(file_name: str):
    """Remove file extension and replace it with '.out'.
    
    Args:
        file_name: str -> name of the file containing extension.
    Returns:
        str: given file name with its extension changed to '.out'
    """
    return file_name.split('.')[0] + '.out'

# Implementation for O(n) time, O(1) space.
def create_reversed_bytes_position_file(file_name: str):
    """Create a new file which contains the bytes from a given file in reverse location.
    
    Args:
        file_name: str -> name of the file to read data from.
    """
    try:
        with open(file_name, 'rb') as file_in, open(output_file_name(file_name), 'wb') as file_out:
            # Go to the end of the file.
            file_in.seek(0, os.SEEK_END)   
            for position in reversed(range(0, file_in.tell(), BUFSIZE)):
                file_in.seek(position, os.SEEK_SET)
                file_out.write(file_in.read(BUFSIZE)[::-1])
    except FileNotFoundError as e:
        print(e)


def main():
    # Ignore the first argument as it's the name of the module.
    for file_name in sys.argv[1:]:
        create_reversed_bytes_position_file(file_name)


if __name__ == "__main__":
    main()  