from keystone import *
from capstone import *
import ida_bytes
import ida_auto
import idaapi
import ida_search
import idautils
import ida_name
import idc

idaapi.msg_clear()

handler_offsets = [
0x00000098,
0x000001A7,
0x000002A2,
0x000003A8,
0x000004A9,
0x0000059F,
0x00000691,
0x000007DE,
0x000008E0,
0x000009EB,
0x00000AF1,
0x00000BFB,
0x00000CFB,
0x00000E3A,
0x00000F2D,
0x00001048,
0x00001140,
0x00001236,
0x0000137D,
0x00001466,
0x00001574,
0x00001677,
0x00001786,
0x00001884,
0x000019DA,
0x00001ACF,
0x00001BD9,
0x00001CD3,
0x00001DEE,
0x00001EF4,
0x00002027,
0x00002120,
0x0000222F,
0x00002333,
0x00002443,
0x00002534,
0x0000268E,
0x0000278A,
0x00002892,
0x00002988,
0x00002A86,
0x00002B88,
0x00002C79,
0x00002D6B,
0x00002E67,
0x00002F5C,
0x000030B1,
0x000031AF,
0x00003295,
0x00003389,
0x0000347E,
0x000035E1,
0x000036E0,
0x000037FC,
0x000038F4,
0x00003A02,
0x00003AFA,
0x00003C69,
0x00003D5F,
0x00003E70,
0x00003F70,
0x00004080,
0x00004182,
0x000042B2,
0x000043A8,
0x000044CB,
0x000045CC,
0x000046CF,
0x000047B2,
0x000048FE,
0x000049E5,
0x00004AFE,
0x00004C0A,
0x00004D05,
0x00004E5B,
0x00004F63,
0x0000507B,
0x000051A1,
0x0000528C,
0x000053A9,
0x000054AC,
0x000055A0,
0x000056A8,
0x000057F6,
0x000058ED,
0x000059ED,
0x00005AE2,
0x00005BF6,
0x00005CE6,
0x00005E20,
0x00005F15,
0x00006038,
0x0000613C,
0x00006249,
0x00006332,
0x00006487,
0x00006573,
0x00006697,
0x00006795,
0x000068A6,
0x0000699C,
0x00006AE3,
0x00006BCD,
0x00006CE8,
0x00006DDE,
0x00006EED,
0x00006FE0,
0x00007113,
0x0000720D,
0x0000732C,
0x0000743F,
0x00007534,
0x0000767E,
0x0000776B,
0x00007883,
0x000079A2,
0x00007A9C,
0x00007BA4,
0x00007C8F,
0x00007D8C,
0x00007E88,
0x00007FD2,
0x000080E4,
0x000081F3,
0x000082FF,
0x00008405,
0x0000855A,
0x00008646,
0x0000875F,
0x00008855,
0x00008956,
0x00008AAE,
0x00008B9D,
0x00008CBF,
0x00008DC6,
0x00008EBB,
0x00008FEF,
0x000090EA,
0x00009201,
0x000092F2,
0x000093E4,
0x0000951C,
0x0000961E,
0x00009739,
0x0000983C,
0x00009948,
0x00009A39,
0x00009B6D,
0x00009C51,
0x00009D51,
0x00009E60,
0x00009F5E,
0x0000A064,
0x0000A153,
0x0000A256,
0x0000A350,
0x0000A46F,
0x0000A56F,
0x0000A658,
0x0000A738,
0x0000A836,
0x0000A937,
0x0000AA62,
0x0000AB4E,
0x0000AC52,
0x0000AD52,
0x0000AE44,
0x0000AF67,
0x0000B064,
0x0000B16E,
0x0000B26B,
0x0000B380,
0x0000B477,
0x0000B58A,
0x0000B68D,
0x0000B79C,
0x0000B898,
0x0000B98C,
0x0000BA9E,
0x0000BB8B,
0x0000BC92,
0x0000BD9D,
0x0000BE93,
0x0000BFB1,
0x0000C09E,
0x0000C1B2,
0x0000C2B0,
0x0000C3A6,
0x0000C4B4,
0x0000C5B9,
0x0000C6A5,
0x0000C7BC,
0x0000C8AC,
0x0000CA16,
0x0000CB00,
0x0000CBF7,
0x0000CCF4,
0x0000CDF5,
0x0000CEDE,
0x0000D01E,
0x0000D11B,
0x0000D236,
0x0000D329,
0x0000D42A,
0x0000D52B,
0x0000D681,
0x0000D788,
0x0000D89D,
0x0000D995,
0x0000DA95,
0x0000DBDC,
0x0000DCC8,
0x0000DDDC,
0x0000DEE4,
0x0000DFD0,
0x0000E122,
0x0000E223,
0x0000E339,
0x0000E442,
0x0000E542,
0x0000E6A0,
0x0000E790,
0x0000E89D,
0x0000E9BE,
0x0000EABB,
0x0000EBC4,
0x0000ECB0,
0x0000EDA4,
0x0000EEA3,
0x0000EFA9,
0x0000F0AD,
0x0000F1A2,
0x0000F2A0,
0x0000F3AB,
0x0000F4A3,
0x0000F5B6,
0x0000F6B3,
0x0000F7C9,
0x0000F8C2,
0x0000F9D4,
0x0000FACF,
0x0000FBF8,
0x0000FCF4,
0x0000FE02,
0x0000FF04,
0x0001000A,
0x00010100,
0x00010205,
0x000102EF,
0x00010411,
0x00010506,
0x000105F3,
0x000106FB,
0x00010801,
0x0001092F,
0x00010A2E,
0x00010B48,
0x00010C3B,
0x00010D4D,
0x00010E49,
0x00010F59,
0x00011064,
0x00011159,
0x0001127E,
0x00011382,
0x0001149A,
0x000115A9,
0x0001169F,
0x000117B6,
0x000118A7,
0x00011995,
0x00011A92,
0x00011B9A,
0x00011CB0,
0x00011DA1,
0x00011E9E,
0x00011F8A,
0x00012075,
0x000121A0,
0x00012295,
0x0001239C,
0x0001248B,
0x00012594,
0x0001268C,
0x00012793,
0x00012890,
0x0001299B,
0x00012A9D,
0x00012B84,
0x00012C8D,
0x00012D83,
0x00012EA6,
0x00012FA7,
0x00013092,
0x000131BB,
0x000132BD,
0x000133D0,
0x000134BB,
0x000135BD,
0x000136B9,
0x000137D3,
0x000138D0,
0x000139DE,
0x00013AC7,
0x00013BBA,
0x00013D13,
0x00013E0A,
0x00013EFF,
0x00013FF6,
0x000140FD,
0x000141F6,
0x00014351,
0x0001443D,
0x0001454E,
0x00014641,
0x00014754,
0x0001484E,
0x00014998,
0x00014A98,
0x00014BA8,
0x00014CA9,
0x00014DA9,
0x00014E8D,
0x00014FD3,
0x000150D2,
0x000151E4,
0x000152FE,
0x000153F1,
0x0001554F,
0x00015656,
0x00015767,
0x00015861,
0x0001595E,
0x00015A5B,
0x00015BAC,
0x00015C93,
0x00015DA6,
0x00015E99,
0x00015F8D,
0x000160DB,
0x000161DC,
0x000162F5,
0x000163F8,
0x00016511,
0x00016613,
0x00016730,
0x0001681C,
0x0001693F,
0x00016A56,
0x00016B4A,
0x00016C50,
0x00016D4B,
0x00016E55,
0x00016F5C,
0x0001705A,
0x00017181,
0x00017285,
0x000173A6,
0x000174AA,
0x000175C7,
0x000176C7,
0x000177DE,
0x000178DF,
0x000179E1
]

Hlt_offsets = [
0x0,
0x107,
0x20a,
0x315,
0x407,
0x510,
0x5fc,
0x737,
0x83f,
0x94d,
0xa4e,
0xb58,
0xc62,
0xd99,
0xe9c,
0xfb0,
0x10aa,
0x1197,
0x12d3,
0x13d4,
0x14dc,
0x15de,
0x16e5,
0x17df,
0x1938,
0x1a3d,
0x1b46,
0x1c3a,
0x1d40,
0x1e55,
0x1f99,
0x2088,
0x219c,
0x2299,
0x239f,
0x24a4,
0x25f1,
0x26f2,
0x2802,
0x28f6,
0x29e9,
0x2afa,
0x2be5,
0x2cd3,
0x2dde,
0x2eca,
0x3003,
0x311c,
0x320e,
0x32ed,
0x33e5,
0x353c,
0x3643,
0x375d,
0x3864,
0x3962,
0x3a66,
0x3bb9,
0x3ccc,
0x3de3,
0x3ecb,
0x3fdf,
0x40e5,
0x4223,
0x4315,
0x4431,
0x452e,
0x4633,
0x472a,
0x485f,
0x495c,
0x4a6a,
0x4b65,
0x4c6f,
0x4dc3,
0x4ebf,
0x4fe5,
0x5103,
0x51fe,
0x5306,
0x540b,
0x5507,
0x5603,
0x5749,
0x585b,
0x5950,
0x5a55,
0x5b54,
0x5c59,
0x5d7f,
0x5e7d,
0x5f91,
0x6094,
0x61a6,
0x62a4,
0x63ee,
0x64e0,
0x65f7,
0x6702,
0x6807,
0x6905,
0x6a3d,
0x6b3a,
0x6c47,
0x6d51,
0x6e48,
0x6f4c,
0x7086,
0x717c,
0x7291,
0x7393,
0x74a0,
0x75e4,
0x76e4,
0x77ea,
0x78fa,
0x7a06,
0x7b0f,
0x7c04,
0x7cf5,
0x7df6,
0x7f2c,
0x803e,
0x8152,
0x8258,
0x835f,
0x84bf,
0x85bf,
0x86cc,
0x87bd,
0x88be,
0x8a15,
0x8b0f,
0x8c20,
0x8d22,
0x8e30,
0x8f58,
0x9051,
0x9170,
0x9258,
0x934a,
0x948b,
0x957e,
0x969c,
0x979c,
0x98b6,
0x99ad,
0x9ad8,
0x9bca,
0x9ccb,
0x9db1,
0x9ec5,
0x9fdb,
0xa0bd,
0xa1b7,
0xa2b7,
0xa3c1,
0xa4d3,
0xa5d0,
0xa6b2,
0xa7a6,
0xa89c,
0xa9b8,
0xaab9,
0xabc7,
0xacb2,
0xadb6,
0xaed1,
0xafcd,
0xb0e3,
0xb1d5,
0xb2de,
0xb3ea,
0xb4ed,
0xb5e9,
0xb70c,
0xb7f7,
0xb8f4,
0xba04,
0xbb01,
0xbc02,
0xbcf7,
0xbdfe,
0xbf13,
0xc010,
0xc11b,
0xc213,
0xc30f,
0xc410,
0xc517,
0xc616,
0xc71c,
0xc81f,
0xc96d,
0xca74,
0xcb71,
0xcc58,
0xcd5c,
0xce56,
0xcf75,
0xd07b,
0xd19a,
0xd295,
0xd393,
0xd490,
0xd5e5,
0xd6e9,
0xd809,
0xd8fa,
0xd9f0,
0xdb40,
0xdc3c,
0xdd45,
0xde35,
0xdf3d,
0xe082,
0xe188,
0xe2a7,
0xe391,
0xe49c,
0xe5fb,
0xe706,
0xe80c,
0xe91e,
0xea28,
0xeb30,
0xec26,
0xed0e,
0xee19,
0xef0a,
0xf014,
0xf117,
0xf209,
0xf306,
0xf40e,
0xf517,
0xf610,
0xf735,
0xf824,
0xf92e,
0xfa2f,
0xfb54,
0xfc59,
0xfd6d,
0xfe68,
0xff76,
0x1006c,
0x1016d,
0x10263,
0x10376,
0x1046d,
0x10561,
0x10667,
0x10760,
0x10888,
0x10999,
0x10aa9,
0x10ba5,
0x10caf,
0x10db7,
0x10ece,
0x10fb9,
0x110bc,
0x111db,
0x112e8,
0x113fe,
0x11504,
0x11600,
0x11716,
0x11815,
0x11901,
0x11a0a,
0x11af8,
0x11c0e,
0x11d11,
0x11e07,
0x11ef8,
0x11fe4,
0x12102,
0x12203,
0x1230c,
0x123f6,
0x124fc,
0x125fb,
0x126ff,
0x127ec,
0x1290b,
0x12a05,
0x12af4,
0x12bf7,
0x12cea,
0x12e08,
0x12f05,
0x12fff,
0x13126,
0x1321f,
0x13339,
0x13428,
0x13526,
0x13621,
0x13730,
0x13832,
0x1394c,
0x13a38,
0x13b22,
0x13c68,
0x13d72,
0x13e6f,
0x13f69,
0x14059,
0x14165,
0x142b0,
0x143aa,
0x144b3,
0x145aa,
0x146b0,
0x147b4,
0x148f2,
0x149fc,
0x14b13,
0x14c0c,
0x14d11,
0x14e05,
0x14f2b,
0x15039,
0x15155,
0x1524a,
0x1535a,
0x154ae,
0x155b8,
0x156ce,
0x157ca,
0x158cc,
0x159c5,
0x15b0b,
0x15c05,
0x15d13,
0x15dfe,
0x15ef6,
0x16040,
0x1613c,
0x1625d,
0x1635e,
0x16473,
0x16573,
0x16688,
0x16789,
0x1689e,
0x169a6,
0x16ab2,
0x16bc6,
0x16cad,
0x16dca,
0x16ebb,
0x16fc5,
0x170e6,
0x171eb,
0x17300,
0x1740c,
0x17520,
0x1762e,
0x1774d,
0x1783c,
0x1795a,
0x17a0e # not a HLT address but to get last handler parsed correctly  
]


# # test offsets
# Hlt_offsets = [
# 0x0,
# 0x107,
# 0x20a,
# 0x315]

# handler_offsets = [
# 0x00000098,
# 0x000001A7,
# 0x000002A2]


def read_binary(offset=0, size=None):
    try:
        with open(r"C:\Users\csgae\Downloads\tmp\flare\serpentine\serpentine.exe", 'rb') as f:
            f.seek(offset)
            if size:
                return f.read(size)
            return f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def disassemble(code, offset):
    """
    Disassemble code at given offset
    """
    md = Cs(CS_ARCH_X86, CS_MODE_64)
    instructions = []
    try:
        for i in md.disasm(code, offset):
            instructions.append({
                'address': i.address,
                'mnemonic': i.mnemonic,
                'op_str': i.op_str,
                'bytes': ' '.join(f'{x:02x}' for x in i.bytes)
            })
        return instructions
    except Exception as e:
        print(f"Disassembly error: {e}")
        return None

def get_inst(ea):
    md = Cs(CS_ARCH_X86, CS_MODE_64)
    opc_bytes = idc.get_bytes(ea, 20)
    for i in md.disasm(opc_bytes, ea):
        tmp = "%s %s" %(i.mnemonic, i.op_str)
        return tmp, i.mnemonic, i.op_str, i.size
    return None, None, None, None

def get_next_inst_addr(ea):
    md = Cs(CS_ARCH_X86, CS_MODE_64)
    opc_bytes = idc.get_bytes(ea, 20)
    for i in md.disasm(opc_bytes, ea):
        return ea + i.size
    return ea + 1  # Ensure we always move forward

def patch_inst(ea, inst):
    ks = Ks(KS_ARCH_X86, KS_MODE_64)
    #bytes_to_patch = inst.to_bytes(4, 'little')
    try:
        inst_opc, count = ks.asm(inst, addr=ea)
        for i in range(len(inst_opc)):
            idc.patch_byte(ea + i, inst_opc[i])
        return ea + len(inst_opc)
    except Exception as e:
        print(f"[-] Error patching instruction: {e}")
        return ea + 1  # Ensure we always move forward

def deobf_sequence(ea,call_add,ret_addr):
    # 1st -> mov rax, 0
    # 2nd -> move byte rax
    # 3rd -> lea rax, [rip + offset]

    # 1st -- init value of eax = 0
        for i in range(2):
            ea=get_next_inst_addr(ea)
        eax_val=eval(get_inst(ea)[2].strip().split(', ')[1])
        print(f"\t\tEAX_val -> {eax_val} __ ",end='')

    # 2nd - value of the byte 
        ea=get_next_inst_addr(ea)
        by_addr = get_inst(ea)[2].strip().split(', ')[1].strip('mov ah, byte ptr ')[1:-1].replace('rip','ea')
        tmp=int(by_addr.split('0x')[1],16)
        if tmp==0x15:
            by_val=ord(idc.get_bytes(eval(by_addr)+6,1))<<8+eax_val
        else:
            by_val = (ret_addr&0xff)<<8
        print(f"Byte_val -> {by_val} __ ",end='')
        
    # 3rd - value of the big_val
        ea=get_next_inst_addr(ea)
        lea_inst = get_inst(ea)
                
        # Extract offset from lea instruction
        # [ ]  lea_inst[2] don't split by + 
        offset_str = lea_inst[2].split(',')[1].strip(']').strip(' [').replace('eax' , 'by_val')
        offset = lea_inst[2].split(',')[1].strip(']').strip(' [').strip('eax')
        # to do it right (0xB800 - 0x2E4DD617) & 0xFFFFFFFF
        print(f"Offset -> {offset_str} __ ",end='')
          
        
        # 2nd & 3rd --> this patches the 2nd part in deobf sequence 
        final = eval(offset_str) & 0xFFFFFFFF
        print(f"final -> {hex(final)}")



# after the patch either (JMP to HLT) OR (proceed placing RET to decoded instruction)

    # jmp HLT
    # could be matched also by see if 0x48, 0x8D, 0x40, 0x00 -- if LEA offset is 0x00 so it's a jmp 
        opcode = final & 0xFF
        if opcode == 0xE9:
            print(f"JMP to hlt")
            real_exec = None
            return ret_addr , real_exec

        # search through bytes till find -- lea     rax, [rax+0x0] -- 0x48, 0x8D, 0x40, 0x00
        else:
            lea = ida_bytes.find_bytes(b"\x48\x8D\x40",ea , 0x100, flags=ida_search.SEARCH_DOWN)
            lea_offset = ord(idc.get_bytes(lea + 3,1))

            real_exec = ret_addr + lea_offset
            deobfusctated_inst = get_inst(real_exec)
            print(f"\t\t\t offset {lea_offset} =>", end=' ')
            print(f"addr {hex(real_exec)} =>", end=' ')
            print(f" [+] instruction : {deobfusctated_inst[0]}")
            
            return ret_addr , real_exec
            

        return ret_addr , real_exec


def get_handler_range(handler_addr):
    start = handler_addr
    for hlt in Hlt_offsets:
        if hlt > start:
            return (start, hlt)
    return None

def check_instruction_pattern(addr):
    ida_auto.auto_make_code(addr)
    try:
        disasm1 = idc.GetDisasm(addr)
        if not ("pop" in disasm1 and "qword" in disasm1):
            return False
        
        addr2 = idc.next_head(addr)
        if not addr2 or idc.GetDisasm(addr2) != "push    rax":
            return False
        
        addr3 = idc.next_head(addr2)
        if not addr3:
            return False
            
        disasm3 = idc.GetDisasm(addr3)
        if not ("mov" in disasm3 and "rax" in disasm3 and "0" in disasm3):
            return False
        
        return True
    except:
        return False

def deobf_func(start_addr, end_addr, ret_addr):
    ea = start_addr

    while ea < end_addr:
        print(f"PC -----> {hex(ea)}")
        full_instr, mnem, oper, inst_size = get_inst(ea)
        if not full_instr or not mnem:
            ea = get_next_inst_addr(ea)
            continue
            
        if mnem == "call":
            target = idc.get_operand_value(ea, 0) # same as oper
            call_address = ea
            ret_addr = call_address + inst_size
            if target and check_instruction_pattern(target):
                    # address of the called -> call_address
                    # address called -> target == ea
                    # address of the next instruction after the call -> ret_addr
                # print(f"\t[+] call_address --> 0x{call_address:x}")
                # print(f"\t[+] ret_addr --> 0x{ret_addr:x}")
                # print(f"\t[+] target --> {hex(target)}")
                # storing previous ret address
                ret_addr, real_exec = deobf_sequence(target, call_address, ret_addr)
                if real_exec == None:
                    return ret_addr # fixing where real ret is --> :)
                else:
                    ea = real_exec


        else:
            print(f"\t [+] instruction : {full_instr}")
        
        # update to next    
        # need to look inside deobfuscated func if it call -- else -- get next inst :)
        if 'call' in get_inst(ea)[0]:
            continue
        # [ ] if normal call hit it will loop through infinite loop
        # [ ] FIX 3rd handler when ea 0x140097da4
        else:
            ea = get_next_inst_addr(ea)
    



#ida_dbg.add_bpt(0x140001649)  # passing key to table in main break
#ida_dbg.start_process()
#table_base = ida_bytes.get_dword(idc.get_operand_value(ida_dbg.get_reg_val("RIP"), 0))

table_base = 0x140097AF0 
raw_base_offset = 0x00095EF0

breakpoint()


print("====== Processing handlers ======")
handler_ranges = {}
ret_addr = None  # Initialize ret_addr
for i, handler in enumerate(handler_offsets):
    if get_handler_range(handler) is None:
        continue
        
    start, end = get_handler_range(handler)
    start += table_base
    end += table_base
    handler_ranges[start] = (end, i)
    print(f"Handler {i}: Start -> {hex(start)} end -> {hex(end)}")
    
    # Analyze and deobfuscate
    ida_auto.auto_make_code(start)
    # print(f"\nDeobfuscating handler {i}:")
    # ret addr will hold the return address of last call that ended with JMP to HLT 
    ret_addr = deobf_func(start, end, ret_addr)  # Pass ret_addr to deobf_func
    print("=" * 50)
    print("=" * 50)

print("[+] Script completed")