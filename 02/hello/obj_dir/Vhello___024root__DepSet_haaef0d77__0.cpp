// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See Vhello.h for the primary calling header

#include "verilated.h"

#include "Vhello__Syms.h"
#include "Vhello___024root.h"

#ifdef VL_DEBUG
VL_ATTR_COLD void Vhello___024root___dump_triggers__act(Vhello___024root* vlSelf);
#endif  // VL_DEBUG

void Vhello___024root___eval_triggers__act(Vhello___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    Vhello__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vhello___024root___eval_triggers__act\n"); );
    // Body
#ifdef VL_DEBUG
    if (VL_UNLIKELY(vlSymsp->_vm_contextp__->debug())) {
        Vhello___024root___dump_triggers__act(vlSelf);
    }
#endif
}
