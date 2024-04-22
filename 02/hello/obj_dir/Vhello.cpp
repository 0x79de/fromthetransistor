// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Model implementation (design independent parts)

#include "Vhello.h"
#include "Vhello__Syms.h"

//============================================================
// Constructors

Vhello::Vhello(VerilatedContext* _vcontextp__, const char* _vcname__)
    : VerilatedModel{*_vcontextp__}
    , vlSymsp{new Vhello__Syms(contextp(), _vcname__, this)}
    , rootp{&(vlSymsp->TOP)}
{
    // Register model with the context
    contextp()->addModel(this);
}

Vhello::Vhello(const char* _vcname__)
    : Vhello(Verilated::threadContextp(), _vcname__)
{
}

//============================================================
// Destructor

Vhello::~Vhello() {
    delete vlSymsp;
}

//============================================================
// Evaluation function

#ifdef VL_DEBUG
void Vhello___024root___eval_debug_assertions(Vhello___024root* vlSelf);
#endif  // VL_DEBUG
void Vhello___024root___eval_static(Vhello___024root* vlSelf);
void Vhello___024root___eval_initial(Vhello___024root* vlSelf);
void Vhello___024root___eval_settle(Vhello___024root* vlSelf);
void Vhello___024root___eval(Vhello___024root* vlSelf);

void Vhello::eval_step() {
    VL_DEBUG_IF(VL_DBG_MSGF("+++++TOP Evaluate Vhello::eval_step\n"); );
#ifdef VL_DEBUG
    // Debug assertions
    Vhello___024root___eval_debug_assertions(&(vlSymsp->TOP));
#endif  // VL_DEBUG
    if (VL_UNLIKELY(!vlSymsp->__Vm_didInit)) {
        vlSymsp->__Vm_didInit = true;
        VL_DEBUG_IF(VL_DBG_MSGF("+ Initial\n"););
        Vhello___024root___eval_static(&(vlSymsp->TOP));
        Vhello___024root___eval_initial(&(vlSymsp->TOP));
        Vhello___024root___eval_settle(&(vlSymsp->TOP));
    }
    // MTask 0 start
    VL_DEBUG_IF(VL_DBG_MSGF("MTask0 starting\n"););
    Verilated::mtaskId(0);
    VL_DEBUG_IF(VL_DBG_MSGF("+ Eval\n"););
    Vhello___024root___eval(&(vlSymsp->TOP));
    // Evaluate cleanup
    Verilated::endOfThreadMTask(vlSymsp->__Vm_evalMsgQp);
    Verilated::endOfEval(vlSymsp->__Vm_evalMsgQp);
}

//============================================================
// Events and timing
bool Vhello::eventsPending() { return false; }

uint64_t Vhello::nextTimeSlot() {
    VL_FATAL_MT(__FILE__, __LINE__, "", "%Error: No delays in the design");
    return 0;
}

//============================================================
// Utilities

const char* Vhello::name() const {
    return vlSymsp->name();
}

//============================================================
// Invoke final blocks

void Vhello___024root___eval_final(Vhello___024root* vlSelf);

VL_ATTR_COLD void Vhello::final() {
    Vhello___024root___eval_final(&(vlSymsp->TOP));
}

//============================================================
// Implementations of abstract methods from VerilatedModel

const char* Vhello::hierName() const { return vlSymsp->name(); }
const char* Vhello::modelName() const { return "Vhello"; }
unsigned Vhello::threads() const { return 1; }
