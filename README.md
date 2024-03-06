# Python PyCryptodome Lab

## Python Configuration
Pyton needs an interpreter, as it is an interpreted language.
Any 3.x **interpreter** can be used (e.g., 3.12). It is recommended to use a so-called virtual environment. This let you have a project specific configuration.
Python features a package manager system. Use it to install the [Cryptodome](https://www.pycryptodome.org/)` package.

## Python Cheat Sheet

See for example [here](https://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf).

## Support Functions
The starter code contains only support functions gathered into `Utility/Utility.py`.

`to_hex_string(the_bytes)`:   generates a printable string out of a list of bytes.

 `bxor(b1, b2)`:  returns the bit-per-bit XOR of bytes `b1` and `b2`.
     
`screw(text, errors=1)`:  introduces `errors` random errors (by default 1) into `text`. The modified `text` is returned.
    
`screw_file(source, destination=None, errors=1)`:  introduces `errors` errors into the file `source`. If the `destination` file is not specified, the `source` file is overwritten.

`display_size(file_object)`:  returns the size of the file identified by `file_object`.
    
`to_file(file, block_1, block_2)`:  concatenates the list of bytes `block_1` and `block_2` into the file `file`.

`from_file(file, block_1_size)`:  returns two lists of bytes: the first has the size `block_1_size`, and the second has the remaining bytes in the file.
  
 `to_file3(file, block_1, block_2, block_3)`:  concatenates the three lists of bytes `block_1`, `block_2` and `block_3` in the file `file`.
  
`from_file3(file, block_1_size, block_2_size)`:  returns three list of bytes. The first contains `block_1_size` bytes, the second `block_2_size` bytes, and the third the remaining bytes.
 
