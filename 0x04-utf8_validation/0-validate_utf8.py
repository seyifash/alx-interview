#!/usr/bin/python3
"""A method that checks if a given data represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """A function Return True if data is a valid 
        UTF-8 encoding, else return False
    """
    def isValidUtf(byte):
        # Check if the byte starts with 0 or 10 (for continuation bytes)
        return byte >> 6 == 0b00 or byte >> 6 == 0b10

    # Initialize a variable to keep track of the number of continuation bytes expected
    num_continuation_bytes = 0

    # Iterate through each byte in the data set
    for byte in data:
        # If no continuation bytes are expected, check the leading bits to determine the length of the UTF-8 character
        if num_continuation_bytes == 0:
            if byte >> 7 == 0:  # Single byte character (starts with 0)
                continue
            elif byte >> 5 == 0b110:  # Two byte character (starts with 110)
                num_continuation_bytes = 1
            elif byte >> 4 == 0b1110:  # Three byte character (starts with 1110)
                num_continuation_bytes = 2
            elif byte >> 3 == 0b11110:  # Four byte character (starts with 11110)
                num_continuation_bytes = 3
            else:
                return False  # Invalid leading byte

        else:
            # Check if the byte is a continuation byte
            if not isValidUtf(byte):
                return False  # Invalid continuation byte

            # Decrease the count of expected continuation bytes
            num_continuation_bytes -= 1

    # Check if there are any remaining expected continuation bytes
    return num_continuation_bytes == 0
