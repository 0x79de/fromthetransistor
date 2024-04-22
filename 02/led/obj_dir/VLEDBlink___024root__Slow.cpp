// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See VLEDBlink.h for the primary calling header

#include "verilated.h"

#include "VLEDBlink__Syms.h"
#include "VLEDBlink___024root.h"

void VLEDBlink___024root___ctor_var_reset(VLEDBlink___024root* vlSelf);

VLEDBlink___024root::VLEDBlink___024root(VLEDBlink__Syms* symsp, const char* v__name)
    : VerilatedModule{v__name}
    , vlSymsp{symsp}
 {
    // Reset structure values
    VLEDBlink___024root___ctor_var_reset(this);
}

void VLEDBlink___024root::__Vconfigure(bool first) {
    if (false && first) {}  // Prevent unused
}

VLEDBlink___024root::~VLEDBlink___024root() {
}
