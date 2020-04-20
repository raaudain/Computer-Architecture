"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256    # Holds 256 bytes of memory 
        self.reg = [0] * 8 # Holds 8 general-purpose registers
        self.pc = 0 # Adds properties for any internal registers needed
        
        

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        # Instruction Register (IR), contains a copy of the currently executing instruction
        
        running = True
        
        while running:
            # Instruction Register (IR), contains a copy of the currently executing instruction
            ir = self.ram_read(self.pc)
            operand_a = self.ram_read(self.pc+1)
            operand_b = self.ram_read(self.pc+2)
            
            if ir == 130:
                self.reg[operand_a] = operand_b
                self.pc += 3
            elif ir == 71:
                print(self.reg[operand_a])
                self.pc += 2
            elif ir == 1:
                # HALT
                running = False
            else:
                print("Unknown instructions")
                break
            
    
    def ram_read(self, mar):
        # Memory Address Register (MAR): holds the memory address we're reading or writing
        return self.ram[mar]
    
    def ram_write(self, mar, mdr):
        # Memory Data Register (mdr), holds the value to write or the value just read
        self.ram[mar] = mdr