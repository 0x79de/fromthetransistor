#!/usr/bin/env python3
import struct
import os
import sys

def create_test_object(filename, section_name, section_content, symbols):
    """
    Create a simple object file for testing
    
    Args:
        filename: Name of the file to create
        section_name: Section name
        section_content: Section content (bytes)
        symbols: Symbol table (dict)
    """
    with open(filename, 'wb') as f:
        # Magic number: "OBJF"
        f.write(b'OBJF')
        
        # Number of symbols
        f.write(struct.pack('<I', len(symbols)))
        
        # Write symbols
        for name, data in symbols.items():
            # Symbol name length
            f.write(struct.pack('<I', len(name)))
            # Symbol name
            f.write(name.encode('utf-8'))
            # Symbol value (address)
            f.write(struct.pack('<I', data['address']))
            # Symbol section index
            f.write(struct.pack('<I', data['section_idx']))
        
        # Number of sections (only 1 section)
        f.write(struct.pack('<I', 1))
        
        # Section name length
        f.write(struct.pack('<I', len(section_name)))
        # Section name
        f.write(section_name.encode('utf-8'))
        # Section start address
        f.write(struct.pack('<I', 0x1000))
        # Section size
        f.write(struct.pack('<I', len(section_content)))
        # Section content
        f.write(section_content)

def main():
    # Test object 1: .text section containing main function
    text_content = bytes([
        # ARM assembly: MOV r0, #1; BX lr (simple function returning 1)
        0x01, 0x00, 0xa0, 0xe3, 
        0x1e, 0xff, 0x2f, 0xe1
    ])
    
    symbols1 = {
        'main': {'address': 0x1000, 'section_idx': 0}
    }
    
    create_test_object('test1.o', '.text', text_content, symbols1)
    print("test1.o created: 'main' function")
    
    # Test object 2: .data section containing hello_world string
    data_content = b'Hello, World!\0'
    
    symbols2 = {
        'hello_string': {'address': 0x1000, 'section_idx': 0}
    }
    
    create_test_object('test2.o', '.data', data_content, symbols2)
    print("test2.o created: 'hello_string' data")

if __name__ == "__main__":
    main() 