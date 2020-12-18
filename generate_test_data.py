from random import randrange
from binary_reverse import create_reversed_bytes_position_file


def generate_file(file_name, size):
    """Generate file of given size with random bytes.
    
    Args:
        file_name: str -> name for the file.
        size: int -> desired byte size of the file.
    """
    with open(file_name, 'wb') as f:
        for i in range(0, size):
            f.write(bytes(randrange(0, 254)))


if __name__ == "__main__":
    file_names = ['data/test_empty.in', 'data/test_1b.in', 'data/test_1kb.in', 'data/test_50kb.in', 'data/test_500kb.in', 'data/test_10mb.in']
    kb = pow(2, 10)
    mb = pow(2, 20)
    sizes = [0, 1, kb * 1, kb * 50, kb * 500, mb * 10]

    for file_name, size in zip(file_names, sizes):
        generate_file(file_name, size)
        create_reversed_bytes_position_file(file_name)
