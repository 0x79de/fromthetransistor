use thiserror::Error;
use std::io;

#[derive(Error, Debug)]
#[allow(dead_code)]
pub enum FatError {
    #[error("I/O error: {0}")]
    IoError(#[from] io::Error),
    
    #[error("Invalid FAT format: {0}")]
    InvalidFormat(String),
    
    #[error("File not found: {0}")]
    FileNotFound(String),
    
    #[error("Directory not found: {0}")]
    DirectoryNotFound(String),
    
    #[error("Not enough space")]
    NotEnoughSpace,
    
    #[error("Invalid operation: {0}")]
    InvalidOperation(String),
}

pub type Result<T> = std::result::Result<T, FatError>;