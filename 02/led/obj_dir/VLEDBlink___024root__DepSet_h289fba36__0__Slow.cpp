// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See VLEDBlink.h for the primary calling header

#include "verilated.h"

#include "VLEDBlink___024root.h"

VL_ATTR_COLD void VLEDBlink___024root___eval_static(VLEDBlink___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    VLEDBlink__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VLEDBlink___024root___eval_static\n"); );
}

VL_ATTR_COLD void VLEDBlink___024root___eval_initial(VLEDBlink___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    VLEDBlink__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VLEDBlink___024root___eval_initial\n"); );
    // Body
    vlSelf->__Vtrigrprev__TOP__clk = vlSelf->clk;
}

VL_ATTR_COLD void VLEDBlink___024root___eval_final(VLEDBlink___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    VLEDBlink__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VLEDBlink___024root___eval_final\n"); );
}

VL_ATTR_COLD void VLEDBlink___024root___eval_settle(VLEDBlink___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    VLEDBlink__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VLEDBlink___024root___eval_settle\n"); );
}

#ifdef VL_DEBUG
VL_ATTR_COLD void VLEDBlink___024root___dump_triggers__act(VLEDBlink___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    VLEDBlink__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VLEDBlink___024root___dump_triggers__act\n"); );
    // Body
    if ((1U & (~ (IData)(vlSelf->__VactTriggered.any())))) {
        VL_DBG_MSGF("         No triggers active\n");
    }
    if (vlSelf->__VactTriggered.at(0U)) {
        VL_DBG_MSGF("         'act' region trigger index 0 is active: @(posedge clk)\n");
    }
}
#endif  // VL_DEBUG

#ifdef VL_DEBUG
VL_ATTR_COLD void VLEDBlink___024root___dump_triggers__nba(VLEDBlink___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    VLEDBlink__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VLEDBlink___024root___dump_triggers__nba\n"); );
    // Body
    if ((1U & (~ (IData)(vlSelf->__VnbaTriggered.any())))) {
        VL_DBG_MSGF("         No triggers active\n");
    }
    if (vlSelf->__VnbaTriggered.at(0U)) {
        VL_DBG_MSGF("         'nba' region trigger index 0 is active: @(posedge clk)\n");
    }
}
#endif  // VL_DEBUG

VL_ATTR_COLD void VLEDBlink___024root___ctor_var_reset(VLEDBlink___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    VLEDBlink__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VLEDBlink___024root___ctor_var_reset\n"); );
    // Body
    vlSelf->clk = VL_RAND_RESET_I(1);
    vlSelf->LED = VL_RAND_RESET_I(1);
    vlSelf->LEDBlink__DOT__cnt = VL_RAND_RESET_I(32);
    vlSelf->__Vtrigrprev__TOP__clk = VL_RAND_RESET_I(1);
}
