#!/usr/bin/env python3
import argparse
import os
from elf_writer import ELFWriter
from object_parser import ObjectParser

# Add this function to parse hexadecimal values properly
def auto_int(x):
    return int(x, 0)  # Automatically detects base (hex, octal, decimal)

def main():
    parser = argparse.ArgumentParser(description='Simple ELF linker')
    parser.add_argument('input_files', nargs='+', help='Object files')
    parser.add_argument('-o', '--output', default='a.out', help='Output file')
    parser.add_argument('--entry-point', default=0x10000, type=auto_int, help='Entry point address')
    parser.add_argument('--base-address', default=0x10000, type=auto_int, help='Base address')
    args = parser.parse_args()
    
    # 1. Read all object files and combine symbol tables
    all_symbols = {}  # global symbol table
    all_sections = {}  # combined sections
    
    for input_file in args.input_files:
        print(f"Reading object file: {input_file}")
        obj_parser = ObjectParser(input_file)
        obj_symbols, obj_sections = obj_parser.parse()
        
        for section_name, section_data in obj_sections.items():
            if section_name not in all_sections:
                all_sections[section_name] = {
                    'content': bytearray(),
                    'address': 0,  # Temporary, will be updated later
                    'size': 0,
                    'symbols': []
                }
            

            current_offset = len(all_sections[section_name]['content'])
            
            all_sections[section_name]['content'].extend(section_data['content'])
            all_sections[section_name]['size'] += section_data['size']
            
            for symbol_name, symbol_data in obj_symbols.items():
                # If symbol is in this section, adjust its offset
                if symbol_data['section_idx'] == list(obj_sections.keys()).index(section_name):
                    symbol_offset = symbol_data['address'] - section_data['address']
                    
                    global_address = current_offset + symbol_offset
                    
                    # Add symbol to global table
                    if symbol_name in all_symbols:
                        print(f"Warning: Symbol '{symbol_name}' already defined, redefining.")
                    
                    all_symbols[symbol_name] = {
                        'address': global_address,
                        'section': section_name
                    }
                    
                    # Add to section symbol list
                    all_sections[section_name]['symbols'].append({
                        'name': symbol_name,
                        'offset': global_address
                    })
    
    # 2. Place sections and assign addresses
    current_address = args.base_address
    
    # First place .text section (executable code)
    if '.text' in all_sections:
        all_sections['.text']['address'] = current_address
        current_address += all_sections['.text']['size']
        # 4-byte alignment
        current_address = (current_address + 3) & ~3
    
    # Then place .data section (initialized data)
    if '.data' in all_sections:
        all_sections['.data']['address'] = current_address
        current_address += all_sections['.data']['size']
        current_address = (current_address + 3) & ~3
    
    # Finally place .bss section (uninitialized data)
    if '.bss' in all_sections:
        all_sections['.bss']['address'] = current_address
        current_address += all_sections['.bss']['size']
    
    # 3. Update symbols' absolute addresses
    for symbol_name, symbol_data in all_symbols.items():
        section_name = symbol_data['section']
        section_base = all_sections[section_name]['address']
        symbol_offset = symbol_data['address']
        
        # Update symbol's absolute address
        all_symbols[symbol_name]['address'] = section_base + symbol_offset
    
    # 4. Create ELF file
    print(f"Creating ELF file: {args.output}")
    elf = ELFWriter(args.output)
    
    # Set entry point (usually the main function)
    entry_point = args.entry_point
    if 'main' in all_symbols:
        entry_point = all_symbols['main']['address']
    
    elf.set_entry_point(entry_point)
    
    # Add sections to ELF
    for section_name, section_data in all_sections.items():
        elf.add_section(
            section_name, 
            bytes(section_data['content']), 
            section_data['address']
        )
    
    # 5. Write ELF file
    elf.write()
    
    print(f"Linking completed: {args.output}")
    print(f"Entry point: 0x{entry_point:08x}")
    
    # 6. Display symbol table
    print("\nSymbol Table:")
    print("-" * 50)
    print(f"{'Symbol':<20} {'Address':<10} {'Section':<10}")
    print("-" * 50)
    
    for name, data in all_symbols.items():
        print(f"{name:<20} 0x{data['address']:08x} {data['section']:<10}")

if __name__ == "__main__":
    main()