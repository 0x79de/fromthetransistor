// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See VLEDBlink.h for the primary calling header

#include "verilated.h"

#include "VLEDBlink___024root.h"

void VLEDBlink___024root___eval_act(VLEDBlink___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    VLEDBlink__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VLEDBlink___024root___eval_act\n"); );
}

VL_INLINE_OPT void VLEDBlink___024root___nba_sequent__TOP__0(VLEDBlink___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    VLEDBlink__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VLEDBlink___024root___nba_sequent__TOP__0\n"); );
    // Init
    IData/*31:0*/ __Vdly__LEDBlink__DOT__cnt;
    __Vdly__LEDBlink__DOT__cnt = 0;
    // Body
    __Vdly__LEDBlink__DOT__cnt = vlSelf->LEDBlink__DOT__cnt;
    __Vdly__LEDBlink__DOT__cnt = ((IData)(1U) + vlSelf->LEDBlink__DOT__cnt);
    vlSelf->LED = (1U & (vlSelf->LEDBlink__DOT__cnt 
                         >> 0x16U));
    vlSelf->LEDBlink__DOT__cnt = __Vdly__LEDBlink__DOT__cnt;
}

void VLEDBlink___024root___eval_nba(VLEDBlink___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    VLEDBlink__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VLEDBlink___024root___eval_nba\n"); );
    // Body
    if (vlSelf->__VnbaTriggered.at(0U)) {
        VLEDBlink___024root___nba_sequent__TOP__0(vlSelf);
    }
}

void VLEDBlink___024root___eval_triggers__act(VLEDBlink___024root* vlSelf);
#ifdef VL_DEBUG
VL_ATTR_COLD void VLEDBlink___024root___dump_triggers__act(VLEDBlink___024root* vlSelf);
#endif  // VL_DEBUG
#ifdef VL_DEBUG
VL_ATTR_COLD void VLEDBlink___024root___dump_triggers__nba(VLEDBlink___024root* vlSelf);
#endif  // VL_DEBUG

void VLEDBlink___024root___eval(VLEDBlink___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    VLEDBlink__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VLEDBlink___024root___eval\n"); );
    // Init
    VlTriggerVec<1> __VpreTriggered;
    IData/*31:0*/ __VnbaIterCount;
    CData/*0:0*/ __VnbaContinue;
    // Body
    __VnbaIterCount = 0U;
    __VnbaContinue = 1U;
    while (__VnbaContinue) {
        __VnbaContinue = 0U;
        vlSelf->__VnbaTriggered.clear();
        vlSelf->__VactIterCount = 0U;
        vlSelf->__VactContinue = 1U;
        while (vlSelf->__VactContinue) {
            vlSelf->__VactContinue = 0U;
            VLEDBlink___024root___eval_triggers__act(vlSelf);
            if (vlSelf->__VactTriggered.any()) {
                vlSelf->__VactContinue = 1U;
                if (VL_UNLIKELY((0x64U < vlSelf->__VactIterCount))) {
#ifdef VL_DEBUG
                    VLEDBlink___024root___dump_triggers__act(vlSelf);
#endif
                    VL_FATAL_MT("LEDBlink.v", 1, "", "Active region did not converge.");
                }
                vlSelf->__VactIterCount = ((IData)(1U) 
                                           + vlSelf->__VactIterCount);
                __VpreTriggered.andNot(vlSelf->__VactTriggered, vlSelf->__VnbaTriggered);
                vlSelf->__VnbaTriggered.set(vlSelf->__VactTriggered);
                VLEDBlink___024root___eval_act(vlSelf);
            }
        }
        if (vlSelf->__VnbaTriggered.any()) {
            __VnbaContinue = 1U;
            if (VL_UNLIKELY((0x64U < __VnbaIterCount))) {
#ifdef VL_DEBUG
                VLEDBlink___024root___dump_triggers__nba(vlSelf);
#endif
                VL_FATAL_MT("LEDBlink.v", 1, "", "NBA region did not converge.");
            }
            __VnbaIterCount = ((IData)(1U) + __VnbaIterCount);
            VLEDBlink___024root___eval_nba(vlSelf);
        }
    }
}

#ifdef VL_DEBUG
void VLEDBlink___024root___eval_debug_assertions(VLEDBlink___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    VLEDBlink__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VLEDBlink___024root___eval_debug_assertions\n"); );
    // Body
    if (VL_UNLIKELY((vlSelf->clk & 0xfeU))) {
        Verilated::overWidthError("clk");}
}
#endif  // VL_DEBUG
