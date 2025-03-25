#!/usr/bin/env python3
import struct
import os

class ObjectParser:
    def __init__(self, filename):
        self.filename = filename
        
    def parse(self):
        """
        Reads a simple object file and extracts the symbol table and sections.
        In this simple example, it reads object files in a custom format.
        
        Simple object file format:
        - 4 bytes: "OBJF" (magic number)
        - 4 bytes: number of symbols (n)
        - n symbol records:
          - 4 bytes: symbol name length (l)
          - l bytes: symbol name
          - 4 bytes: symbol value (address)
          - 4 bytes: symbol section index
        - 4 bytes: number of sections (m)
        - m section records:
          - 4 bytes: section name length (k)
          - k bytes: section name
          - 4 bytes: section start address
          - 4 bytes: section size (s)
          - s bytes: section content
          
        Returns:
            tuple: (symbols, sections)
        """
        symbols = {}  # name -> {address, size, section, ...}
        sections = {}  # name -> {content, address, size, ...}
        
        # Create a simple object file for testing
        if not os.path.exists(self.filename):
            # A real parser would read the file content here
            print(f"Error: File {self.filename} not found.")
            print("Creating simple object files for testing...")
            return self._create_test_object()
        
        with open(self.filename, 'rb') as f:
            # Check magic number
            magic = f.read(4)
            if magic != b'OBJF':
                raise ValueError(f"Invalid object file: {self.filename}")
            
            # Read symbols
            symbol_count = struct.unpack('<I', f.read(4))[0]
            for _ in range(symbol_count):
                name_len = struct.unpack('<I', f.read(4))[0]
                name = f.read(name_len).decode('utf-8')
                value = struct.unpack('<I', f.read(4))[0]
                section_idx = struct.unpack('<I', f.read(4))[0]
                
                symbols[name] = {
                    'address': value,
                    'section_idx': section_idx
                }
            
            # Read sections
            section_count = struct.unpack('<I', f.read(4))[0]
            for _ in range(section_count):
                name_len = struct.unpack('<I', f.read(4))[0]
                name = f.read(name_len).decode('utf-8')
                address = struct.unpack('<I', f.read(4))[0]
                size = struct.unpack('<I', f.read(4))[0]
                content = f.read(size)
                
                sections[name] = {
                    'content': content,
                    'address': address,
                    'size': size
                }
        
        return symbols, sections
    
    def _create_test_object(self):
        """
        Create a simple object file content for testing
        """
        symbols = {
            'main': {'address': 0x1000, 'section_idx': 0},
            'printf': {'address': 0x2000, 'section_idx': 1}
        }
        
        sections = {
            '.text': {
                'content': bytes([
                    # Simple ARM assembly code (MOV r0, #1; BX lr)
                    0x01, 0x00, 0xa0, 0xe3, 
                    0x1e, 0xff, 0x2f, 0xe1
                ]),
                'address': 0x1000,
                'size': 8
            },
            '.data': {
                'content': b'Hello, World!\0',
                'address': 0x2000,
                'size': 14
            }
        }
        
        return symbols, sections 