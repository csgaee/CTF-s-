# ===============================================================
# get typedobj RUNTIME_FUNCTION and UNWIND_INFO info and layout
# ===============================================================
# import idautils

# for struct in idautils.Structs():
#     print(f"Structure : {struct}")

# Structure : (1, 18374686479671624181, 'RUNTIME_FUNCTION')
# Structure : (2, 18374686479671624185, 'UNWIND_INFO_HDR')
# Structure : (3, 18374686479671624192, 'UNWIND_CODE')
# Structure : (4, 18374686479671624196, 'FuncInfo')
# Structure : (5, 18374686479671624207, 'IPtoStateMap')
# Structure : (6, 18374686479671624210, 'UnwindMapEntry')
# Structure : (9, 18374686479671625749, '_FILETIME')
# Structure : (11, 18374686479671625753, 'LARGE_INTEGER')
# Structure : (89, 18374686479671626193, 'LIST_ENTRY')
# Structure : (90, 18374686479671626194, '_LIST_ENTRY')
# Structure : (96, 18374686479671626212, 'DYNAMIC_FUNCTION_TABLE')
# Structure : (98, 18374686479671626328, 'UNWIND_INFO')
# Structure : (99, 18374686479671626329, '_UNWIND_INFO')

# 14001FC90

# sid = 18374686479671624185
# for m in idautils.StructMembers(sid):
#     print(f"member : {m}")

# ===============================================================
# ===============================================================
# ===============================================================

import idaapi
import ida_dbg
idaapi.msg_clear()
# Address of the RUNTIME_FUNCTION structure
# RF_addr = ida_dbg.get_reg_val("RAX") # Replace with your actual address
RF_addr = 0x1408A7108
base_addr = 0x140000000  # Replace with your actual base address

def interpret_unwind_code(prolog_off, unwind_op, op_info):
    unwind_ops = {
        0: "UWOP_PUSH_NONVOL",
        1: "UWOP_ALLOC_LARGE",
        2: "UWOP_ALLOC_SMALL",
        3: "UWOP_SET_FPREG",
        4: "UWOP_SAVE_NONVOL",
        5: "UWOP_SAVE_NONVOL_FAR",
        6: "UWOP_SAVE_XMM128",
        7: "UWOP_SAVE_XMM128_FAR",
        8: "UWOP_PUSH_MACHFRAME"
    }
    
    registers = ["RAX", "RCX", "RDX", "RBX", "RSP", "RBP", "RSI", "RDI", "R8", "R9", "R10", "R11", "R12", "R13", "R14", "R15"]

    interpretation = f" -->"
    # interpretation += f"PrologOff: {prolog_off} (Offset from start of function)\n"
    # interpretation += f"UnwindOp: {unwind_op} ({unwind_ops.get(unwind_op, 'Unknown')})\n"
    # interpretation += f"OpInfo: {op_info}\n\n"

    if unwind_op == 0:  # UWOP_PUSH_NONVOL
        interpretation += f"Pushes register {registers[op_info]} onto the stack"
    elif unwind_op == 1:  # UWOP_ALLOC_LARGE
        if op_info == 0:
            interpretation += "Allocates a large-sized area on the stack. The size is in the next slot."
        elif op_info == 1:
            interpretation += "Allocates a large-sized area on the stack. The size is in the next two slots."
    elif unwind_op == 2:  # UWOP_ALLOC_SMALL
        size = (op_info * 8) + 8
        interpretation += f"Allocates {size} bytes on the stack"
    elif unwind_op == 3:  # UWOP_SET_FPREG
        interpretation += f"Sets the frame pointer using register {registers[op_info]}"
    elif unwind_op == 4:  # UWOP_SAVE_NONVOL
        interpretation += f"Saves register {registers[op_info]} at [RSP+8*next_slot]"
    elif unwind_op == 5:  # UWOP_SAVE_NONVOL_FAR
        interpretation += f"Saves register {registers[op_info]} at [RSP+32-bit-offset-in-next-2-slots]"
    elif unwind_op == 6:  # UWOP_SAVE_XMM128
        interpretation += f"Saves 128-bit XMM register {op_info} at [RSP+8*next_slot]"
    elif unwind_op == 7:  # UWOP_SAVE_XMM128_FAR
        interpretation += f"Saves 128-bit XMM register {op_info} at [RSP+32-bit-offset-in-next-2-slots]"
    elif unwind_op == 8:  # UWOP_PUSH_MACHFRAME
        interpretation += "Pushes a machine frame onto the stack"
        if op_info == 0:
            interpretation += " (without error code)"
        elif op_info == 1:
            interpretation += " (with error code)"
    else:
        interpretation += "Unknown unwind operation"

    return interpretation

print(f"RUNTIME_FUNCTION base: {RF_addr:#x}")
print("-" * 35)
# Ensure the structure types are correctly defined in IDA's Local Types
try:
    # Define and retrieve =RUNTIME_FUNCTION object
    rf_tp = idaapi.Appcall.typedobj("RUNTIME_FUNCTION;", RF_addr)
    rf_ok, rf = rf_tp.retrieve()

    if rf_ok:
        print(f"FunctionStart: {rf.FunctionStart+base_addr:#x}")
        print(f"FunctionEnd: {rf.FunctionEnd+base_addr:#x}")
        unwind_info_addr = idaapi.get_dword(RF_addr + 8)
        unwind_info_addr += base_addr
        print(f"unwind_info_addr -> {hex(unwind_info_addr)}")
        print('=' * 50)
        # "rf.UnwindInfo" is a <class 'ida_idaapi.object_t'> that contains the following fields:
        # ['CountOfCodes', 'Flags', 'FrameOffset', 'FrameRegister', 'SizeOfProlog', 'UnwindCode', 'Version']
        # print(dir(rf.UnwindInfo))   
    

        # Now retrieve the _UNWIND_INFO object at the UnwindInfo address
        ui_tp = idaapi.Appcall.typedobj("_UNWIND_INFO ;", unwind_info_addr)
        ui_ok, ui = ui_tp.retrieve()
        print("unwind_info")
        print("-" * 35)

        if ui_ok:
            print(f"Version: {ui.Version}")
            print(f"Flags: {ui.Flags}")
            print(f"PrologSize: {ui.SizeOfProlog}")
            print(f"CntUnwindCodes: {ui.CountOfCodes}")
            print(f"FrameRegister: {ui.FrameRegister}")
            print(f"FrameOffset: {ui.FrameOffset}")
            print('=' * 50)
            uc_addr = unwind_info_addr + 4
        else:
            print("Failed to retrieve _UNWIND_INFO")


        if ui.CountOfCodes:
            print("UNWIND_CODE")
            print("-" * 35)
            # 'OpInfo', 'PrologOff', 'UnwindOp'
            # struct UNWIND_CODE // sizeof=0x2
            # so, iterate according to how many CntUnwindCodes
            for i in range(ui.CountOfCodes):
                uc_addr = uc_addr + (i * 2)  # Each UNWIND_CODE is 2 bytes
                uc_tp = idaapi.Appcall.typedobj("UNWIND_CODE;", uc_addr)
                uc_ok, uc = uc_tp.retrieve()
                
                print(f"{hex(uc_addr)} PrologOff: {uc.PrologOff} UnwindOp: {uc.UnwindOp} OpInfo: {uc.OpInfo}")
                print(interpret_unwind_code(uc.PrologOff, uc.UnwindOp, uc.OpInfo))

    else:
        print("Failed to retrieve RUNTIME_FUNCTION")
except Exception as e:
    print(f"Error: {e}")