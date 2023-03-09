#!/usr/bin/python3
import dis
import marshal

with open('hidden.pyc', 'rb') as f:
    magic = f.read(4)  # Read the magic number
    timestamp = f.read(4)  # Read the timestamp
    code = marshal.load(f)  # Load the code object from the file
    dis.disassemble(code)  # Disassemble the code object to print all names defined
