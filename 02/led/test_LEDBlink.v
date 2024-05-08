#! /usr/bin/vvp
:ivl_version "11.0 (stable)";
:ivl_delay_selection "TYPICAL";
:vpi_time_precision + 0;
:vpi_module "/usr/lib/x86_64-linux-gnu/ivl/system.vpi";
:vpi_module "/usr/lib/x86_64-linux-gnu/ivl/vhdl_sys.vpi";
:vpi_module "/usr/lib/x86_64-linux-gnu/ivl/vhdl_textio.vpi";
:vpi_module "/usr/lib/x86_64-linux-gnu/ivl/v2005_math.vpi";
:vpi_module "/usr/lib/x86_64-linux-gnu/ivl/va_math.vpi";
S_0x55c304b8adc0 .scope module, "LEDBlink" "LEDBlink" 2 1;
 .timescale 0 0;
    .port_info 0 /INPUT 1 "clk";
    .port_info 1 /OUTPUT 1 "LED";
v0x55c304b8c7f0_0 .var "LED", 0 0;
o0x7ff8d6ac0048 .functor BUFZ 1, C4<z>; HiZ drive
v0x55c304b8cc00_0 .net "clk", 0 0, o0x7ff8d6ac0048;  0 drivers
v0x55c304bd1a70_0 .var "cnt", 31 0;
E_0x55c304b8b790 .event posedge, v0x55c304b8cc00_0;
    .scope S_0x55c304b8adc0;
T_0 ;
    %wait E_0x55c304b8b790;
    %load/vec4 v0x55c304bd1a70_0;
    %addi 1, 0, 32;
    %assign/vec4 v0x55c304bd1a70_0, 0;
    %load/vec4 v0x55c304bd1a70_0;
    %parti/s 1, 22, 6;
    %assign/vec4 v0x55c304b8c7f0_0, 0;
    %jmp T_0;
    .thread T_0;
# The file index is used to find the file name in the following table.
:file_names 3;
    "N/A";
    "<interactive>";
    "LEDBlink.v";
