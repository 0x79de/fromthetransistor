# linker

A lightweight ELF linker implementation in Python that demonstrates linking object files into executable programs for ARM architecture.
## Usage

Create and Link

```bash
# Create test object files
python3 create_test_object.py

# Link into an executable
python3 linker.py test1.o test2.o -o program.elf

# Optional: Specify custom addresses
python3 linker.py test1.o test2.o -o program.elf --entry-point 0x10000 --base-address 0x10000

# Test with QEMU
qemu-arm -semihosting program.elf 
````

## resources

- https://lwn.net/Articles/276782/
- https://www.airs.com/blog/archives/38
- http://www.skyfree.org/linux/references/ELF_Format.pdf