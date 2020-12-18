import filecmp
import pytest
from binary_reverse import create_reversed_bytes_position_file


@pytest.mark.parametrize(
    "test_input, test_output, expected",
    [
        ("data/test_1b.in", "data/test_1b.out", "data/expected_1b"),
        ("data/test_1kb.in", "data/test_1kb.out", "data/expected_1kb"),
        ("data/test_50kb.in", "data/test_50kb.out", "data/expected_50kb"),
        ("data/test_500kb.in", "data/test_500kb.out", "data/expected_500kb"),
        ("data/test_1mb.in", "data/test_1mb.out", "data/expected_1mb"),
    ],
)
def test_can_create_new_file_with_reversed_bytes_position(
    test_input, test_output, expected
):

    create_reversed_bytes_position_file(test_input)

    assert filecmp.cmp(test_output, expected) == True


def test_reverse_byte_location_works_for_empty_file():

    create_reversed_bytes_position_file("data/test_empty.in")

    assert filecmp.cmp("data/test_empty.out", "data/expected_empty") == True


def test_reverse_byte_location_fails_gracefully_for_non_existing_file():
    try:
        create_reversed_bytes_position_file("non-existing-file.in")
        # Passed this line successfully.
        assert True
    except Exception:
        assert False
