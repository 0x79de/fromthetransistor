#include <iostream>
#include "verilated.h"  
#include "VLEDBlink.h"     

int main(int argc, char** argv) {
    Verilated::commandArgs(argc, argv);

    VLEDBlink* top = new VLEDBlink;

    for (int i = 0; i < 50; ++i) {
        top->clk = !top->clk;

        top->eval();

        std::cout << "LED: " << top->LED << std::endl;

        top->clk = !top->clk;
        top->eval();
    }

    delete top;

    return 0;
}

