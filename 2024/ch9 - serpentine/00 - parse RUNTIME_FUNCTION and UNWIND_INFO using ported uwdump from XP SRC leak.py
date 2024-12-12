import struct
import enum
from dataclasses import dataclass
from typing import List, BinaryIO

class UnwindOpCodes(enum.IntEnum):
    UWOP_PUSH_NONVOL = 0
    UWOP_ALLOC_LARGE = 1
    UWOP_ALLOC_SMALL = 2
    UWOP_SET_FPREG = 3
    UWOP_SAVE_NONVOL = 4
    UWOP_SAVE_NONVOL_FAR = 5
    UWOP_SAVE_XMM = 6
    UWOP_SAVE_XMM_FAR = 7
    UWOP_SAVE_XMM128 = 8
    UWOP_SAVE_XMM128_FAR = 9
    UWOP_PUSH_MACHFRAME = 10

REGISTERS = [
    "rax", "rcx", "rdx", "rbx", "rsp", "rbp", "rsi", "rdi",
    "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15",
    "xmm0", "xmm1", "xmm2", "xmm3", "xmm4", "xmm5", "xmm6",
    "xmm7", "xmm8", "xmm9", "xmm10", "xmm11", "xmm12",
    "xmm13", "xmm14", "xmm15"
]

@dataclass
class FunctionInfo:
    start: int
    end: int
    unwind_info: int
    calculated_offset: int

@dataclass
class UnwindCode:
    code_offset: int
    unwind_op: UnwindOpCodes
    op_info: int

    @classmethod
    def from_buffer(cls, buffer: BinaryIO) -> 'UnwindCode':
        data = buffer.read(2)
        code_struct = struct.unpack("<H", data)[0]
        code_offset = code_struct & 0xFF
        unwind_op = (code_struct >> 8) & 0x0F
        op_info = (code_struct >> 12) & 0x0F
        return cls(code_offset, UnwindOpCodes(unwind_op), op_info)

class UnwindInfo:
    def __init__(self, buffer: BinaryIO):
        byte1 = struct.unpack("<B", buffer.read(1))[0]
        self.version = byte1 & 0x07
        self.flags = (byte1 >> 3) & 0x1F
        
        self.size_of_prolog = struct.unpack("<B", buffer.read(1))[0]
        self.count_of_codes = struct.unpack("<B", buffer.read(1))[0]
        
        frame_reg_byte = struct.unpack("<B", buffer.read(1))[0]
        self.frame_register = frame_reg_byte & 0x0F
        self.frame_offset = (frame_reg_byte >> 4) & 0x0F
        
        self.unwind_codes: List[UnwindCode] = []
        for _ in range(self.count_of_codes):
            code = UnwindCode.from_buffer(buffer)
            self.unwind_codes.append(code)
            
        if self.flags & 0x3:
            if self.count_of_codes % 2:
                buffer.read(2)
            self.exception_handler = struct.unpack("<I", buffer.read(4))[0]
        else:
            self.exception_handler = None

def dump_unwind_info(buffer: BinaryIO, function_info: FunctionInfo, raw_offset: int) -> None:
    print(f"\nRuntime Function:")
    print(f"  Begin Address:  0x{function_info.start:08X}")
    print(f"  End Address:    0x{function_info.end:08X}")
    print(f"  Unwind Info:    0x{function_info.unwind_info:08X}")
    print(f"  Raw Offset:     0x{raw_offset:08X}")  # Added this line
    print(f"  File Offset:    0x{function_info.calculated_offset:08X}")
    
    # Seek directly to the calculated offset for UnwindInfo
    buffer.seek(function_info.calculated_offset)
    
    try:
        unwind_info = UnwindInfo(buffer)
        
        print(f"\nUnwind Info at offset 0x{function_info.calculated_offset:08X}:")
        print(f"  Version:        {unwind_info.version}")
        print(f"  Flags:          0x{unwind_info.flags:02X}")
        print(f"  Prolog Size:    0x{unwind_info.size_of_prolog:02X}")
        print(f"  Code Count:     {unwind_info.count_of_codes}")
        
        if unwind_info.frame_register:
            print(f"  Frame Register: {REGISTERS[unwind_info.frame_register]}")
            print(f"  Frame Offset:   0x{unwind_info.frame_offset * 16:02X}")
        
        print("\nUnwind Codes:")
        for i, code in enumerate(unwind_info.unwind_codes):
            print(f"\n  Code {i}:")
            print(f"    Offset:     0x{code.code_offset:02X}")
            print(f"    Operation:  {code.unwind_op.name}")
            
            if code.unwind_op == UnwindOpCodes.UWOP_PUSH_NONVOL:
                print(f"    Register:   {REGISTERS[code.op_info]}")
            elif code.unwind_op == UnwindOpCodes.UWOP_ALLOC_LARGE:
                if code.op_info == 0:
                    buffer.seek(2, 1)
                    size = struct.unpack("<H", buffer.read(2))[0] * 8
                else:
                    buffer.seek(2, 1)
                    size = struct.unpack("<I", buffer.read(4))[0]
                print(f"    Size:       0x{size:X}")
        
        if unwind_info.exception_handler:
            print(f"\n  Exception Handler: 0x{unwind_info.exception_handler:08X}")
    
    except Exception as e:
        print(f"Error processing function: {str(e)}")

def parse_input_file(filename: str) -> List[FunctionInfo]:
    functions = []
    base_address = 0x6910000
    raw_offset = 0x95EF0
    
    with open(filename, 'r') as f:
        for line in f:
            # Split the line by spaces and dashes
            parts = line.strip().split(' - ')
            
            # Extract the hexadecimal values
            start = int(parts[0].split(': ')[1], 16)
            end = int(parts[1].split(': ')[1], 16)
            unwind_info = int(parts[2].split(': ')[1], 16)
            
            # Calculate the offset for UnwindInfo
            calculated_offset = (unwind_info - base_address) + raw_offset
            
            functions.append(FunctionInfo(start, end, unwind_info, calculated_offset))
    
    return functions

def main():
    raw_offset = 0x95EF0  # Made this explicit at the top level
    functions = parse_input_file('offsets.txt')
    
    with open('serpentine.exe', 'rb') as f:
        for func in functions:
            try:
                dump_unwind_info(f, func, raw_offset)  # Pass raw_offset to the function
                print("\n" + "="*80 + "\n")
            except Exception as e:
                print(f"Error processing function at 0x{func.start:08X}: {str(e)}")

if __name__ == '__main__':
    main()