mod fat;
mod disk;
mod directory;
mod error;

use std::path::Path;
use disk::DiskImage;
use fat::{FatFilesystem, BiosParameterBlock};
use error::Result;

fn main() -> Result<()> {
    println!("FAT Filesystem Implementation");
    
    let image_path = Path::new("fat_image.img");
    let mut disk = DiskImage::new(image_path, 512)?;
    
    let total_sectors = 2880;
    disk.format(total_sectors)?;
    
    println!("Disk formatted with basic structure");
    
    let _bpb = BiosParameterBlock::new_fat16();
    let mut boot_sector = vec![0u8; 512];
    
    boot_sector[0] = 0xEB;
    boot_sector[1] = 0x3C;
    boot_sector[2] = 0x90;
    
    let oem_name = b"MSWIN4.1";
    boot_sector[3..11].copy_from_slice(oem_name);
    
    disk.write_sector(0, &boot_sector)?;
    
    let _filesystem = FatFilesystem::new(disk)?;
    
    println!("FAT filesystem initialized successfully!");
    
    Ok(())
}
