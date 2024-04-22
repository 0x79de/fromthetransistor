// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See Vhello.h for the primary calling header

#include "verilated.h"

#include "Vhello__Syms.h"
#include "Vhello___024root.h"

void Vhello___024root___ctor_var_reset(Vhello___024root* vlSelf);

Vhello___024root::Vhello___024root(Vhello__Syms* symsp, const char* v__name)
    : VerilatedModule{v__name}
    , vlSymsp{symsp}
 {
    // Reset structure values
    Vhello___024root___ctor_var_reset(this);
}

void Vhello___024root::__Vconfigure(bool first) {
    if (false && first) {}  // Prevent unused
}

Vhello___024root::~Vhello___024root() {
}
