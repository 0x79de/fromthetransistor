`timescale 1ns/1ns
`include "./uart_tx.v"
`include "./uart_rx.v"


module uart_tb ();
	

	parameter CLOCK_PERIOD_NS = 20;
	parameter TICKS_PER_BIT   = 3'd4;	

	parameter BIT_PERIOD_NS = CLOCK_PERIOD_NS*TICKS_PER_BIT;

	reg clk = 0;
	reg tx_start = 0;
	reg [7:0] tx_data = 0;
	wire tx_done, tx_busy, tx_dout_serial;

	reg rx_din_serial = 1;
	reg rx_enable = 1;
	wire [7:0] rx_data;
	wire rx_recv;
	wire rx_busy;

	task UART_SOFT_WRITE_BYTE;
		input [7:0] i_data;
		integer ii;
		begin
			rx_din_serial = 1'b0;
			#(BIT_PERIOD_NS);

			for (ii=0; ii<8; ii=ii+1) begin
				rx_din_serial = i_data[ii];
				#(BIT_PERIOD_NS);
			end
				
			rx_din_serial = 1'b1;
			#(BIT_PERIOD_NS);
		end
	endtask


	task UART_TX_WRITE_BYTE;
		input [7:0] i_data;
		begin
			@(posedge clk);
			@(posedge clk);
			tx_start <= 1;
			tx_data <= i_data;
			@(posedge clk);
			tx_start <= 0;
			@(posedge tx_done); 
		end
	endtask
		
	uart_rx #(
		.TICKS_PER_BIT(TICKS_PER_BIT),
		.TICKS_PER_BIT_SIZE($bits(TICKS_PER_BIT))
	)
	UART_RX_INST (	
		.i_clk(clk),
		.i_enable(rx_enable),
		.i_din(rx_din_serial),
		.o_rxdata(rx_data),
		.o_recvdata(rx_recv),
		.o_busy(rx_busy)
	);

	uart_tx #(
		.TICKS_PER_BIT(TICKS_PER_BIT), 
		.TICKS_PER_BIT_SIZE($bits(TICKS_PER_BIT))
	)
	UART_TX_INST (
		.i_clk(clk),
		.i_start(tx_start),
		.i_data(tx_data),
		.o_done(tx_done),
		.o_busy(tx_busy),
		.o_dout(tx_dout_serial)
	);

	always 
		#(CLOCK_PERIOD_NS/2) clk <= ~clk;

	initial begin
			$dumpfile("uart_tb.vcd");
			$dumpvars(0, uart_tb);
			
			@(posedge clk);
			@(posedge clk);
			UART_SOFT_WRITE_BYTE(8'hAB);
			@(posedge clk);
			#(BIT_PERIOD_NS);
			if (rx_data == 8'hAB)
				$display("[UART RX]: Frist Test Passed - Correct Byte Received\n");
			else
				$display("[UART RX]: Frist Test Failed - Incorrect Byte Received\n");

			assign rx_din_serial = tx_dout_serial;
			$display("[UART TX]: Sending data to UART RX module\n");
			UART_TX_WRITE_BYTE(8'h0D);
			@(posedge clk);
			#(BIT_PERIOD_NS);
			if (rx_data == 8'h0D)
				$display("[UART RX]: Second Test Passed - Correct Byte Received\n");
			else
				$display("[UART RX]: Second Test Failed - Incorrect Byte Received\n");
 
			$finish;
		end
endmodule
