import os

from random import sample


def to_hex_string(the_bytes):
    hex_string = ''
    in_line = 0
    for b in the_bytes:
        hex_string += format(b, '#x')
        in_line += 1
        if in_line in range(1, 8):
            hex_string += '-'
        if in_line in range(9, 16):
            hex_string += '-'
        if in_line == 8:
            hex_string += '  '
        if in_line == 16:
            in_line = 0
            hex_string += '\r\n'
    return hex_string


def bxor(b1, b2):
    result = bytearray(b1)
    for i, b in enumerate(b2):
        result[i] ^= b
    return bytes(result)


def screw(block, errors=1):
    size = len(block) * 8;
    to_invert = sample(range(0, size - 1, 1), errors)
    inverted = 0
    for pos in to_invert:
        inverted += pow(2, pos)
    return bxor(block, inverted.to_bytes(len(block), byteorder='big'))


def screw_file(source, destination=None, errors=1):
    source_file = open(source, 'rb')
    source_file.seek(0, os.SEEK_END)
    size = source_file.tell()
    source_file.seek(0, 0)
    data = bytearray(source_file.read())

    # inverted_bits is a list of errors random bit positions to invert
    inverted_bits = sample(range(0, size - 1, 1), errors)

    for bit_pos in inverted_bits:
        # locate the byte to invert
        byte_pos = bit_pos // 8
        # locate the bit to invert within the byte
        in_byte_pos = bit_pos % 8
        # invert
        data[byte_pos] ^= (1 << in_byte_pos)

    source_file.close()

    if destination is None:
        destination = source

    destination_file = open(destination, 'wb')
    destination_file.write(data)
    destination_file.close()


def display_size(file_object):
    file_object.seek(0, os.SEEK_END)
    return file_object.tell()


def to_file(file, block_1, block_2):
    file_out = open(file, 'wb')
    [file_out.write(x) for x in (block_1, block_2)]
    file_out.close()


def from_file(file, block_1_size):
    file_in = open(file, 'rb')
    block_1, block_2 = [file_in.read(x) for x in (block_1_size, -1)]
    return block_1, block_2

def to_file3(file, block_1, block_2, block_3):
    file_out = open(file, 'wb')
    [file_out.write(x) for x in (block_1, block_2, block_3)]
    file_out.close()

def from_file3(file, block_1_size, block_2_size):
    file_in = open(file, 'rb')
    block_1, block_2, block_3 = [file_in.read(x) for x in (block_1_size, block_2_size, -1)]
    return block_1, block_2, block_3
