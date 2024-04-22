module uart_tx 
	#(
		parameter TICKS_PER_BIT = 32,
		parameter TICKS_PER_BIT_SIZE = 6
	)

	(
		input i_clk,
		input i_start,
		input [7:0] i_data,
		output wire o_done,
		output wire o_busy,
		output wire o_dout
	);

	localparam	STATE_IDLE 			= 5'b00001,
				STATE_SEND_START 	= 5'b00010,
				STATE_SEND_BITS		= 5'b00100,
				STATE_SEND_STOP		= 5'b01000,
				STATE_DONE			= 5'b10000;
	
	reg [4:0] currentState, nextState;
	reg done_flag;
	reg busy_flag;
	reg tx_output;
	
	assign o_dout = tx_output;
	assign o_done = done_flag;
	assign o_busy = busy_flag;
	
	reg [7:0] tx_reg;
	reg [3:0] tx_bit_counter;
	reg [TICKS_PER_BIT_SIZE-1:0] ticks_counter;

	wire ticks_counter_ovf 		= (ticks_counter == TICKS_PER_BIT-1);
	wire tx_bit_counter_ovf 	= (tx_bit_counter[3]); 

	initial begin
		currentState = STATE_IDLE;
		tx_reg = 0;
		tx_bit_counter = 0;
		ticks_counter = 0;
	end
	
	always @(*) begin
		case(currentState)

			default: begin 
				nextState = STATE_IDLE;
				done_flag = 0;
				busy_flag = 0;
				tx_output = 1; 
			end

			STATE_IDLE: begin 
				done_flag = 0;
				busy_flag = 0;
				tx_output = 1; 
				
				if(i_start)
					nextState = STATE_SEND_START;
				else
					nextState = STATE_IDLE;
			end 
			
			STATE_SEND_START: begin 
				done_flag = 0;
				busy_flag = 1;
				tx_output = 0; 
				
				if(ticks_counter_ovf)
					nextState = STATE_SEND_BITS;
				else
					nextState = STATE_SEND_START;
					
			end 
			
			STATE_SEND_BITS: begin 
				done_flag = 0;
				busy_flag = 1;
				tx_output = tx_bit_counter_ovf ? 1'b1 : tx_reg[0];
				
				if(tx_bit_counter_ovf)
					nextState = STATE_SEND_STOP;
				else
					nextState = STATE_SEND_BITS;
					
			end 
			
			STATE_SEND_STOP: begin 
				done_flag = 0;
				busy_flag = 1;
				tx_output = 1; 
				
				if(ticks_counter_ovf)
					nextState = STATE_DONE;
				else
					nextState = STATE_SEND_STOP;
			end 
			
			STATE_DONE: begin 
				done_flag = 1;
				busy_flag = 1;
				tx_output = 1; 
				nextState = STATE_IDLE;
			end 
			
		endcase
	end
	
	always @(posedge i_clk) begin 
		currentState <= nextState;

		if (currentState == STATE_SEND_START || 
			currentState == STATE_SEND_BITS || 
			currentState == STATE_SEND_STOP) begin
			
			if(ticks_counter_ovf) begin
				ticks_counter <= 0;
			end	
			else 
				ticks_counter <= ticks_counter + 1;
		end
		
		if (currentState == STATE_SEND_BITS) begin 
			if(ticks_counter_ovf) begin
				tx_bit_counter <= tx_bit_counter + 1;
				tx_reg <= tx_reg >> 1; 
			end
		end

		if(currentState == STATE_IDLE) begin 
			if(i_start) begin 
				tx_reg <= i_data;
				tx_bit_counter <= 0;
			end
		end
	end

endmodule 
