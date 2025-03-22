#![allow(dead_code)]

use chrono::{DateTime, Local, Datelike, Timelike};
use crate::error::{FatError, Result};

#[derive(Debug, Clone)]
#[allow(dead_code)]
pub struct DirectoryEntry {
    pub filename: [u8; 8],
    pub extension: [u8; 3],
    pub attributes: u8,
    pub reserved: u8,
    pub creation_time_tenths: u8,
    pub creation_time: u16,
    pub creation_date: u16,
    pub last_access_date: u16,
    pub first_cluster_high: u16,
    pub last_write_time: u16,
    pub last_write_date: u16,
    pub first_cluster_low: u16,
    pub file_size: u32,
}

impl DirectoryEntry {
    pub fn new_file(name: &str, extension: &str, cluster: u32, size: u32) -> Result<Self> {
        let now = Local::now();
        let (filename, ext) = Self::format_name(name, extension)?;
        
        Ok(DirectoryEntry {
            filename,
            extension: ext,
            attributes: 0x00,
            reserved: 0,
            creation_time_tenths: 0,
            creation_time: Self::encode_time(&now),
            creation_date: Self::encode_date(&now),
            last_access_date: Self::encode_date(&now),
            first_cluster_high: ((cluster >> 16) & 0xFFFF) as u16,
            last_write_time: Self::encode_time(&now),
            last_write_date: Self::encode_date(&now),
            first_cluster_low: (cluster & 0xFFFF) as u16,
            file_size: size,
        })
    }
    
    pub fn new_directory(name: &str, cluster: u32) -> Result<Self> {
        let now = Local::now();
        let (filename, ext) = Self::format_name(name, "")?;
        
        Ok(DirectoryEntry {
            filename,
            extension: ext,
            attributes: 0x10,
            reserved: 0,
            creation_time_tenths: 0,
            creation_time: Self::encode_time(&now),
            creation_date: Self::encode_date(&now),
            last_access_date: Self::encode_date(&now),
            first_cluster_high: ((cluster >> 16) & 0xFFFF) as u16,
            last_write_time: Self::encode_time(&now),
            last_write_date: Self::encode_date(&now),
            first_cluster_low: (cluster & 0xFFFF) as u16,
            file_size: 0,
        })
    }
    
    fn format_name(name: &str, extension: &str) -> Result<([u8; 8], [u8; 3])> {
        let mut filename = [0x20u8; 8];
        let mut ext = [0x20u8; 3];
        
        let name_upper = name.to_uppercase();
        let ext_upper = extension.to_uppercase();
        
        for (i, c) in name_upper.bytes().enumerate() {
            if i >= 8 { break; }
            if Self::is_valid_char(c) {
                filename[i] = c;
            } else {
                return Err(FatError::InvalidFormat(format!("Invalid character in filename: {}", c as char)));
            }
        }
        
        for (i, c) in ext_upper.bytes().enumerate() {
            if i >= 3 { break; }
            if Self::is_valid_char(c) {
                ext[i] = c;
            } else {
                return Err(FatError::InvalidFormat(format!("Invalid character in extension: {}", c as char)));
            }
        }
        
        Ok((filename, ext))
    }
    
    fn is_valid_char(c: u8) -> bool {
        (c >= b'A' && c <= b'Z') || 
        (c >= b'0' && c <= b'9') ||
        c == b'$' || c == b'%' || c == b'\'' || c == b'-' || 
        c == b'_' || c == b'@' || c == b'~' || c == b'`' || 
        c == b'!' || c == b'(' || c == b')' || c == b'{'  || 
        c == b'}' || c == b'^' || c == b'#' || c == b'&'
    }
    
    fn encode_time(dt: &DateTime<Local>) -> u16 {
        let hour = dt.hour() as u16;
        let min = dt.minute() as u16;
        let sec = dt.second() as u16 / 2;
        
        (hour << 11) | (min << 5) | sec
    }
    
    fn encode_date(dt: &DateTime<Local>) -> u16 {
        let year = (dt.year() - 1980) as u16;
        let month = dt.month() as u16;
        let day = dt.day() as u16;
        
        (year << 9) | (month << 5) | day
    }
}