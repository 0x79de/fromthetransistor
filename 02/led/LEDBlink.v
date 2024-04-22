module LEDBlink(
  input clk,
  output reg LED
);

reg [31:0] cnt;

always @(posedge clk) begin 
    cnt <= cnt + 1;
    LED <= cnt[22];
end

endmodule
