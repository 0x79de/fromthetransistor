use std::fs::{File, OpenOptions};
use std::io::{Read, Write, Seek, SeekFrom};
use std::path::Path;
use crate::error::Result;

pub struct DiskImage {
    file: File,
    sector_size: u32,
}

impl DiskImage {
    pub fn new<P: AsRef<Path>>(path: P, sector_size: u32) -> Result<Self> {
        let file = OpenOptions::new()
            .read(true)
            .write(true)
            .create(true)
            .open(path)?;
        
        Ok(DiskImage {
            file,
            sector_size,
        })
    }
    
    pub fn read_sector(&mut self, sector: u32, buffer: &mut [u8]) -> Result<()> {
        let offset = (sector as u64) * (self.sector_size as u64);
        self.file.seek(SeekFrom::Start(offset))?;
        self.file.read_exact(buffer)?;
        Ok(())
    }
    
    pub fn write_sector(&mut self, sector: u32, buffer: &[u8]) -> Result<()> {
        let offset = (sector as u64) * (self.sector_size as u64);
        self.file.seek(SeekFrom::Start(offset))?;
        self.file.write_all(buffer)?;
        Ok(())
    }
    
    pub fn format(&mut self, total_sectors: u32) -> Result<()> {
        let size = (total_sectors as u64) * (self.sector_size as u64);
        self.file.set_len(size)?;
        
        let zeros = vec![0u8; self.sector_size as usize];
        for sector in 0..total_sectors {
            self.write_sector(sector, &zeros)?;
        }
        
        Ok(())
    }
}