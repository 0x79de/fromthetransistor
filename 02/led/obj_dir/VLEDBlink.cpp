// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Model implementation (design independent parts)

#include "VLEDBlink.h"
#include "VLEDBlink__Syms.h"

//============================================================
// Constructors

VLEDBlink::VLEDBlink(VerilatedContext* _vcontextp__, const char* _vcname__)
    : VerilatedModel{*_vcontextp__}
    , vlSymsp{new VLEDBlink__Syms(contextp(), _vcname__, this)}
    , clk{vlSymsp->TOP.clk}
    , LED{vlSymsp->TOP.LED}
    , rootp{&(vlSymsp->TOP)}
{
    // Register model with the context
    contextp()->addModel(this);
}

VLEDBlink::VLEDBlink(const char* _vcname__)
    : VLEDBlink(Verilated::threadContextp(), _vcname__)
{
}

//============================================================
// Destructor

VLEDBlink::~VLEDBlink() {
    delete vlSymsp;
}

//============================================================
// Evaluation function

#ifdef VL_DEBUG
void VLEDBlink___024root___eval_debug_assertions(VLEDBlink___024root* vlSelf);
#endif  // VL_DEBUG
void VLEDBlink___024root___eval_static(VLEDBlink___024root* vlSelf);
void VLEDBlink___024root___eval_initial(VLEDBlink___024root* vlSelf);
void VLEDBlink___024root___eval_settle(VLEDBlink___024root* vlSelf);
void VLEDBlink___024root___eval(VLEDBlink___024root* vlSelf);

void VLEDBlink::eval_step() {
    VL_DEBUG_IF(VL_DBG_MSGF("+++++TOP Evaluate VLEDBlink::eval_step\n"); );
#ifdef VL_DEBUG
    // Debug assertions
    VLEDBlink___024root___eval_debug_assertions(&(vlSymsp->TOP));
#endif  // VL_DEBUG
    if (VL_UNLIKELY(!vlSymsp->__Vm_didInit)) {
        vlSymsp->__Vm_didInit = true;
        VL_DEBUG_IF(VL_DBG_MSGF("+ Initial\n"););
        VLEDBlink___024root___eval_static(&(vlSymsp->TOP));
        VLEDBlink___024root___eval_initial(&(vlSymsp->TOP));
        VLEDBlink___024root___eval_settle(&(vlSymsp->TOP));
    }
    // MTask 0 start
    VL_DEBUG_IF(VL_DBG_MSGF("MTask0 starting\n"););
    Verilated::mtaskId(0);
    VL_DEBUG_IF(VL_DBG_MSGF("+ Eval\n"););
    VLEDBlink___024root___eval(&(vlSymsp->TOP));
    // Evaluate cleanup
    Verilated::endOfThreadMTask(vlSymsp->__Vm_evalMsgQp);
    Verilated::endOfEval(vlSymsp->__Vm_evalMsgQp);
}

//============================================================
// Events and timing
bool VLEDBlink::eventsPending() { return false; }

uint64_t VLEDBlink::nextTimeSlot() {
    VL_FATAL_MT(__FILE__, __LINE__, "", "%Error: No delays in the design");
    return 0;
}

//============================================================
// Utilities

const char* VLEDBlink::name() const {
    return vlSymsp->name();
}

//============================================================
// Invoke final blocks

void VLEDBlink___024root___eval_final(VLEDBlink___024root* vlSelf);

VL_ATTR_COLD void VLEDBlink::final() {
    VLEDBlink___024root___eval_final(&(vlSymsp->TOP));
}

//============================================================
// Implementations of abstract methods from VerilatedModel

const char* VLEDBlink::hierName() const { return vlSymsp->name(); }
const char* VLEDBlink::modelName() const { return "VLEDBlink"; }
unsigned VLEDBlink::threads() const { return 1; }
