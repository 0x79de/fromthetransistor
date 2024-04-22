// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design internal header
// See VLEDBlink.h for the primary calling header

#ifndef VERILATED_VLEDBLINK___024ROOT_H_
#define VERILATED_VLEDBLINK___024ROOT_H_  // guard

#include "verilated.h"

class VLEDBlink__Syms;

class VLEDBlink___024root final : public VerilatedModule {
  public:

    // DESIGN SPECIFIC STATE
    VL_IN8(clk,0,0);
    VL_OUT8(LED,0,0);
    CData/*0:0*/ __Vtrigrprev__TOP__clk;
    CData/*0:0*/ __VactContinue;
    IData/*31:0*/ LEDBlink__DOT__cnt;
    IData/*31:0*/ __VactIterCount;
    VlTriggerVec<1> __VactTriggered;
    VlTriggerVec<1> __VnbaTriggered;

    // INTERNAL VARIABLES
    VLEDBlink__Syms* const vlSymsp;

    // CONSTRUCTORS
    VLEDBlink___024root(VLEDBlink__Syms* symsp, const char* v__name);
    ~VLEDBlink___024root();
    VL_UNCOPYABLE(VLEDBlink___024root);

    // INTERNAL METHODS
    void __Vconfigure(bool first);
} VL_ATTR_ALIGNED(VL_CACHE_LINE_BYTES);


#endif  // guard
