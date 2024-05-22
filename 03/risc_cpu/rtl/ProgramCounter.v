module ProgramCounter(
    input wire clk,
    input wire rst,
    input wire enable,
    input wire loda,
    input wire [31:0] addr,
    input wire [31:0] pc,
);

always @(posedge clk or posedge rst) begin
    if (rst) begin
        pc <= 32'b0; 
    end else if (enable) begin
        if (load) begin
            pc <= addr; 
        end else begin
            pc <= pc + 32'b1; 
        end
    end
end

endmodule
