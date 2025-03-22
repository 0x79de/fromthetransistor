# fat

This project provides a basic implementation of the FAT16 filesystem format in rust.

## Setup

```bash
git clone https://github.com/0x79de/fromthetransistor.git
cd fromthetransistor/05/fat

cargo build

cargo run
```

## Usage

The main program creates a FAT16 filesystem image representing a 1.44MB floppy disk:

```rust
let image_path = Path::new("fat_image.img");
let mut disk = DiskImage::new(image_path, 512)?;
    
// Format disk with 2880 sectors (1.44MB)
let total_sectors = 2880;
disk.format(total_sectors)?;
```
## Structure 

- src/
    - main.rs - Entry point, demonstrates creating and formatting a FAT filesystem
    - fat.rs - FAT structures including BiosParameterBlock and FatType
    - disk.rs - Disk I/O operations for reading and writing sectors
    - directory.rs - FAT directory entry structures and operations
    - error.rs - Custom error types for the filesystem
    - lib.rs - Library exports and module organization

## Resources

- [Microsoft FAT Specification ](https://academy.cba.mit.edu/classes/networking_communications/SD/FAT.pdf)
- [OSDev Wiki FAT](https://wiki.osdev.org/FAT)