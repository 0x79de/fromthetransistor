module uart_rx 
	#(
		parameter TICKS_PER_BIT = 32,
		parameter TICKS_PER_BIT_SIZE = 6
	)
	
	(
		input i_clk,
		input i_enable,
		
		input i_din,
		
		output [7:0] o_rxdata,
		output reg o_recvdata,
		output reg o_busy
	);
	
	localparam TICKS_TO_BIT		= TICKS_PER_BIT-1;
	localparam TICKS_TO_MIDLE	= TICKS_TO_BIT/2;
	
	reg [7:0] rx_data;
	assign o_rxdata = rx_data;

	reg din_buff;
	wire din_negedge_signal = ~i_din & din_buff;
	
	reg [3:0] bit_counter;
	reg [TICKS_PER_BIT_SIZE-1:0] bit_ticks_counter;
	
	reg [TICKS_PER_BIT_SIZE-1:0] bit_ticks_comparator;
	
	wire bit_ticks_ovf_signal			= (bit_ticks_counter == bit_ticks_comparator);
	wire bit_counter_ovf_signal 		= (bit_counter[3]); 

	initial begin
		currentState = STATE_IDLE;
		bit_ticks_counter = 0;
		bit_counter = 0;
		din_buff = 1;
		rx_data = 0;
	end
	
	localparam	STATE_IDLE			= 5'b00001,
				STATE_RECEIVE_START	= 5'b00010,
				STATE_RECEIVE_DATA	= 5'b00100,
				STATE_RECEIVE_STOP	= 5'b01000,
				STATE_DONE			= 5'b10000;
	
	reg [4:0] currentState, nextState;
	
	always@(*) begin
		case (currentState)

			default: begin
				nextState = STATE_IDLE;
				o_recvdata = 0;
				o_busy = 0;
				bit_ticks_comparator = TICKS_TO_MIDLE;
			end

			STATE_IDLE: begin 
				o_recvdata = 0;
				o_busy = 0;
				bit_ticks_comparator = TICKS_TO_MIDLE;
				
				if(i_enable)
					if(din_negedge_signal)
						nextState = STATE_RECEIVE_START;
					else 
						nextState = STATE_IDLE;
				else
					nextState = STATE_IDLE;
			end 
			
			STATE_RECEIVE_START: begin
				o_recvdata = 0;
				o_busy = 1;
				bit_ticks_comparator = TICKS_TO_MIDLE;

				if(bit_ticks_ovf_signal) begin 
					if(!din_buff)
						nextState = STATE_RECEIVE_DATA;
					else
						nextState = STATE_IDLE;
				end 
				else
					nextState = STATE_RECEIVE_START;
			end 
			
			STATE_RECEIVE_DATA: begin 
				o_recvdata = 0;
				o_busy = 1;
				bit_ticks_comparator = TICKS_TO_BIT;

				if(bit_counter_ovf_signal)
					nextState = STATE_RECEIVE_STOP;
				else
					nextState = STATE_RECEIVE_DATA;
			end 
			
			STATE_RECEIVE_STOP: begin
				o_recvdata = 0;
				o_busy = 1;
				bit_ticks_comparator = TICKS_TO_BIT;
				
				if(bit_ticks_ovf_signal)
					nextState = STATE_DONE;
				else
					nextState = STATE_RECEIVE_STOP;
			end 
			
			STATE_DONE: begin 
				o_recvdata = 1;
				o_busy = 1;
				bit_ticks_comparator = TICKS_TO_BIT;
				nextState = STATE_IDLE;
			end 
		endcase
	end
	
	always @(posedge i_clk) begin 
		currentState <= nextState;
		din_buff <= i_din;
		
		if(currentState == STATE_IDLE) begin 
			bit_ticks_counter <= 0;
			bit_counter <= 0;
		end
		
		if(	currentState == STATE_RECEIVE_START || 
			currentState == STATE_RECEIVE_DATA	||
			currentState == STATE_RECEIVE_STOP) begin 
			
			if(bit_ticks_ovf_signal)
				bit_ticks_counter <= 0;
			else
				bit_ticks_counter <= bit_ticks_counter + 1;
		end
		
		
		if(currentState == STATE_RECEIVE_DATA) begin 
			if(bit_ticks_ovf_signal) begin
				bit_counter <= bit_counter + 1;
				rx_data <= rx_data[7:1]; 
				rx_data[7] <= din_buff;
			end
		end
	end
endmodule 
