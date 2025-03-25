#!/usr/bin/env python3
import struct

# ELF constants
ELF_MAGIC = b'\x7fELF'
ELF_CLASS_32 = 1            # 32-bit
ELF_DATA_2_LSB = 1          # Little-endian
ELF_VERSION = 1             # Current version
ELF_OSABI_SYSV = 0          # System V ABI
ELF_TYPE_EXEC = 2           # Executable file
ELF_MACHINE_ARM = 40        # ARM

# ELF header sizes
ELF_HEADER_SIZE = 52        # ELF header size (32-bit)
PROGRAM_HEADER_SIZE = 32    # Program header size (32-bit)
SECTION_HEADER_SIZE = 40    # Section header size (32-bit)

# Section flags
SHF_WRITE = 0x1             # Writable section
SHF_ALLOC = 0x2             # Memory allocated section
SHF_EXECINSTR = 0x4         # Executable section

# Section types
SHT_NULL = 0                # Null section
SHT_PROGBITS = 1            # Program information
SHT_SYMTAB = 2              # Symbol table
SHT_STRTAB = 3              # String table

# Program header types
PT_LOAD = 1        # Loadable segment

class ELFWriter:
    def __init__(self, filename):
        self.filename = filename
        self.sections = []
        self.entry_point = 0
        self.section_name_table = b'\0.text\0.data\0.bss\0.shstrtab\0'
        self.program_headers = []  # Yeni: Program başlıkları listesi
        
    def set_entry_point(self, address):
        self.entry_point = address
        
    def add_section(self, name, content, address):
        """
        Adds a section to the ELF file.
        
        Args:
            name (str): Section name
            content (bytes): Section content
            address (int): Memory address
        """
        if not isinstance(content, bytes):
            content = bytes(content)
            
        flags = 0
        if name == '.text':
            section_type = SHT_PROGBITS
            flags = SHF_ALLOC | SHF_EXECINSTR
        elif name == '.data':
            section_type = SHT_PROGBITS
            flags = SHF_ALLOC | SHF_WRITE
        elif name == '.bss':
            section_type = SHT_PROGBITS
            flags = SHF_ALLOC | SHF_WRITE
        else:
            section_type = SHT_PROGBITS
            flags = SHF_ALLOC
            
        # Calculate section name offset (index in string table)
        name_offset = self.section_name_table.find(name.encode() + b'\0')
        if name_offset == -1:
            name_offset = len(self.section_name_table)
            self.section_name_table += name.encode() + b'\0'
            
        self.sections.append({
            'name': name,
            'name_offset': name_offset,
            'content': content,
            'address': address,
            'size': len(content),
            'type': section_type,
            'flags': flags,
            'offset': 0  # Temporary value, will be calculated during writing
        })
        
    def add_program_header(self, vaddr, paddr, file_offset, file_size, mem_size, flags, align):
        """
        Adds a program header to the ELF file.
        
        Args:
            vaddr (int): Virtual address where segment is loaded
            paddr (int): Physical address (usually same as vaddr)
            file_offset (int): Offset in the file where segment data starts
            file_size (int): Size of segment in the file
            mem_size (int): Size of segment in memory (can be larger than file_size for .bss)
            flags (int): Segment flags (read/write/execute)
            align (int): Alignment of segment
        """
        self.program_headers.append({
            'type': PT_LOAD,
            'offset': file_offset,
            'vaddr': vaddr,
            'paddr': paddr,
            'filesz': file_size,
            'memsz': mem_size,
            'flags': flags,
            'align': align
        })
    
    def write(self):
        """
        Writes the ELF file to disk.
        """
        with open(self.filename, 'wb') as f:
            # Add string table section
            self.add_section('.shstrtab', self.section_name_table, 0)
            
            # Program header için uygun değerleri hesapla
            # Yüklenebilir bölümler için program başlıkları oluştur
            loadable_sections = [s for s in self.sections if s['name'] in ['.text', '.data', '.bss']]
            
            # Program başlıklarının başlangıç offsetini hesapla
            ph_offset = ELF_HEADER_SIZE
            
            # Program başlıkları sayısı
            num_phdrs = len(loadable_sections)
            
            # Section başlıklarının başlangıç offsetini hesapla 
            sh_offset = ph_offset + (num_phdrs * PROGRAM_HEADER_SIZE)
            
            # Bölüm sayısı (NULL bölüm dahil)
            num_sections = len(self.sections) + 1
            
            # Bölüm içeriklerinin başlangıç offsetini hesapla
            content_offset = sh_offset + (num_sections * SECTION_HEADER_SIZE)
            
            # Bölüm offset değerlerini hesapla
            for section in self.sections:
                # 4 byte hizalama
                content_offset = (content_offset + 3) & ~3
                section['offset'] = content_offset
                content_offset += section['size']
            
            # Program başlıklarını hesapla
            self.program_headers = []
            
            for section in loadable_sections:
                flags = 0
                if section['name'] == '.text':
                    flags = 0x5  # PF_X | PF_R (executable, readable)
                else:
                    flags = 0x6  # PF_W | PF_R (writable, readable)
                
                self.add_program_header(
                    vaddr=section['address'],
                    paddr=section['address'],
                    file_offset=section['offset'], 
                    file_size=section['size'],
                    mem_size=section['size'],
                    flags=flags,
                    align=4  # 4-byte hizalama
                )
            
            # ELF Header - mevcut kod ile benzer, ancak program header bilgileri değişecek
            f.write(ELF_MAGIC)
            f.write(struct.pack('B', ELF_CLASS_32))
            f.write(struct.pack('B', ELF_DATA_2_LSB))
            f.write(struct.pack('B', ELF_VERSION))
            f.write(b'\0' * 9)
            f.write(struct.pack('<H', ELF_TYPE_EXEC))
            f.write(struct.pack('<H', ELF_MACHINE_ARM))
            f.write(struct.pack('<I', ELF_VERSION))
            f.write(struct.pack('<I', self.entry_point))
            f.write(struct.pack('<I', ph_offset))  # Program header offset
            f.write(struct.pack('<I', sh_offset))  # Section header offset
            f.write(struct.pack('<I', 0))
            f.write(struct.pack('<H', ELF_HEADER_SIZE))
            f.write(struct.pack('<H', PROGRAM_HEADER_SIZE))
            f.write(struct.pack('<H', num_phdrs))  # Program header sayısı - değişti!
            f.write(struct.pack('<H', SECTION_HEADER_SIZE))
            f.write(struct.pack('<H', num_sections))
            f.write(struct.pack('<H', num_sections - 1))
            
            # Program header'ları yaz - bu bölüm yeni!
            for ph in self.program_headers:
                f.write(struct.pack('<I', ph['type']))      # Type
                f.write(struct.pack('<I', ph['offset']))    # Offset
                f.write(struct.pack('<I', ph['vaddr']))     # Virtual address
                f.write(struct.pack('<I', ph['paddr']))     # Physical address
                f.write(struct.pack('<I', ph['filesz']))    # Size in file
                f.write(struct.pack('<I', ph['memsz']))     # Size in memory
                f.write(struct.pack('<I', ph['flags']))     # Flags
                f.write(struct.pack('<I', ph['align']))     # Alignment
            
            # NULL section header - mevcut kod aynı kalacak
            f.write(struct.pack('<I', 0))
            f.write(struct.pack('<I', SHT_NULL))
            f.write(struct.pack('<I', 0))
            f.write(struct.pack('<I', 0))
            f.write(struct.pack('<I', 0))
            f.write(struct.pack('<I', 0))
            f.write(struct.pack('<I', 0))
            f.write(struct.pack('<I', 0))
            f.write(struct.pack('<I', 0))
            f.write(struct.pack('<I', 0))
            
            # Section headers - mevcut kod aynı kalacak
            for section in self.sections:
                f.write(struct.pack('<I', section['name_offset']))
                f.write(struct.pack('<I', section['type']))
                f.write(struct.pack('<I', section['flags']))
                f.write(struct.pack('<I', section['address']))
                f.write(struct.pack('<I', section['offset']))
                f.write(struct.pack('<I', section['size']))
                f.write(struct.pack('<I', 0))
                f.write(struct.pack('<I', 0))
                f.write(struct.pack('<I', 4))
                f.write(struct.pack('<I', 0))
            
            # Section contents - bölüm içeriklerini yazma kısmını güncelle
            for section in self.sections:
                # Dosyada doğru konuma git
                pos = f.tell()
                if pos < section['offset']:
                    padding = section['offset'] - pos
                    f.write(b'\0' * padding)
                
                # Bölüm içeriğini yaz
                f.write(section['content'])