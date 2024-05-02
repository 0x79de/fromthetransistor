.section .text
.globl _start

_start:
    call setup_uart
    li t0, 0x80000000

read_loop:
    call uart_data_available
    beqz a0, read_loop
    
    call uart_read_byte
    sb a0, 0(t0)
    addi t0, t0, 1

    j read_loop

setup_uart
    ret 

uart_data_available:
    li ti, 0x40000000
    lbu a0, 0(ti)
    ret

uart_read_byte:
    li ti, 0x40000000
    lbu a0, 0(ti)
    ret
