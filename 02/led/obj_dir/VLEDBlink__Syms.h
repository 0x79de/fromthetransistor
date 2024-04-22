// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Symbol table internal header
//
// Internal details; most calling programs do not need this header,
// unless using verilator public meta comments.

#ifndef VERILATED_VLEDBLINK__SYMS_H_
#define VERILATED_VLEDBLINK__SYMS_H_  // guard

#include "verilated.h"

// INCLUDE MODEL CLASS

#include "VLEDBlink.h"

// INCLUDE MODULE CLASSES
#include "VLEDBlink___024root.h"

// SYMS CLASS (contains all model state)
class VLEDBlink__Syms final : public VerilatedSyms {
  public:
    // INTERNAL STATE
    VLEDBlink* const __Vm_modelp;
    bool __Vm_didInit = false;

    // MODULE INSTANCE STATE
    VLEDBlink___024root            TOP;

    // CONSTRUCTORS
    VLEDBlink__Syms(VerilatedContext* contextp, const char* namep, VLEDBlink* modelp);
    ~VLEDBlink__Syms();

    // METHODS
    const char* name() { return TOP.name(); }
} VL_ATTR_ALIGNED(VL_CACHE_LINE_BYTES);

#endif  // guard
