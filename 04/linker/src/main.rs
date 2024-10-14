use std::fs;

#[derive(Debug)]
struct Section {
    #[allow(dead_code)]
    name: String,
    content: String,
}

#[derive(Debug)]
struct ObjectFile {
    sections: Vec<Section>,
}

const ELF_HEADER: [u8; 64] = [
    0x7f, 0x45, 0x4c, 0x46, // ELF magic
    0x02, 0x01, 0x01, 0x00, // ELF class, data, version, and OS ABI
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, // Padding
    0x02, 0x00, // e_type (Executable file)
    0x3e, 0x00, // e_machine (x86-64)
    0x01, 0x00, 0x00, 0x00, // e_version
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, // e_entry (Entry point address)
    0x40, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, // e_phoff (Program header table offset)
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, // e_shoff (Section header table offset)
    0x00, 0x00, 0x00, 0x00, // e_flags
    0x40, 0x00, // e_ehsize (ELF header size)
    0x38, 0x00, // e_phentsize (Program header table entry size)
    0x01, 0x00, // e_phnum (Number of program header entries)
    0x40, 0x00, // e_shentsize (Section header table entry size)
    0x00, 0x00, // e_shnum (Number of section header entries)
    0x00, 0x00, // e_shstrndx (Section header string table index)
];

const PROGRAM_HEADER: [u8; 56] = [
    0x01, 0x00, 0x00, 0x00, // p_type (Loadable segment)
    0x00, 0x00, 0x00, 0x00, // p_flags (Segment flags)
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, // p_offset (Offset in file)
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, // p_vaddr (Virtual address in memory)
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, // p_paddr (Physical address, not used)
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, // p_filesz (Size of segment in file)
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, // p_memsz (Size of segment in memory)
    0x00, 0x00, 0x00, 0x00, // p_align (Segment alignment)
    0x00, 0x00, 0x00, 0x00, // Additional padding to reach 56 bytes
];

fn main() {
    let object_file = read_object_file("input.obj");

    let mut elf_content = ELF_HEADER.to_vec();
    elf_content.extend_from_slice(&PROGRAM_HEADER);

    for section in object_file.sections {
        elf_content.extend(section.content.as_bytes());
    }

    fs::write("output.elf", &elf_content).expect("Failed to write ELF file");
}

fn read_object_file(path: &str) -> ObjectFile {
    let content = fs::read_to_string(path).expect("Failed to read object file");
    let mut sections = Vec::new();
    let mut lines = content.lines();

    while let Some(line) = lines.next() {
        if line.starts_with(".text") {
            sections.push(Section {
                name: ".text".to_string(),
                content: lines.next().unwrap_or("").to_string(),
            });
        } else if line.starts_with(".data") {
            sections.push(Section {
                name: ".data".to_string(),
                content: lines.next().unwrap_or("").to_string(),
            });
        }
    }

    ObjectFile { sections }
}
