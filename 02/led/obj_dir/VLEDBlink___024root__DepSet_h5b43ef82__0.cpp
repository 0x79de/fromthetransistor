// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See VLEDBlink.h for the primary calling header

#include "verilated.h"

#include "VLEDBlink__Syms.h"
#include "VLEDBlink___024root.h"

#ifdef VL_DEBUG
VL_ATTR_COLD void VLEDBlink___024root___dump_triggers__act(VLEDBlink___024root* vlSelf);
#endif  // VL_DEBUG

void VLEDBlink___024root___eval_triggers__act(VLEDBlink___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    VLEDBlink__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VLEDBlink___024root___eval_triggers__act\n"); );
    // Body
    vlSelf->__VactTriggered.at(0U) = ((IData)(vlSelf->clk) 
                                      & (~ (IData)(vlSelf->__Vtrigrprev__TOP__clk)));
    vlSelf->__Vtrigrprev__TOP__clk = vlSelf->clk;
#ifdef VL_DEBUG
    if (VL_UNLIKELY(vlSymsp->_vm_contextp__->debug())) {
        VLEDBlink___024root___dump_triggers__act(vlSelf);
    }
#endif
}
