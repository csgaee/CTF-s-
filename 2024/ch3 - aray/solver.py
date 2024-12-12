from z3 import *

def uint32_to_ascii_string(value):
    # Convert the uint32 to a 4-byte hex representation and unpack the bytes
    byte1 = value & 0xFF
    byte2 = (value >> 8) & 0xFF
    byte3 = (value >> 16) & 0xFF
    byte4 = (value >> 24) & 0xFF
    return chr(byte1) + chr(byte2) + chr(byte3) + chr(byte4)

# Define a list of unsigned 8-bit bit-vectors
bitvecs = [BitVec(f'_{i}', 8) for i in range(0, 85)]

# Create a solver instance
s = Solver()

# # Constraints for _0
# s.add(ULT(bitvecs[0], 129))          # uint8(0) < 129 (unsigned less-than)
# s.add(UGT(bitvecs[0], 30))           # uint8(0) > 30 (unsigned greater-than)
# s.add(bitvecs[0] ^ 85 != 16)         # uint8(0) ^ 85 != 16
# s.add(bitvecs[0] ^ 85 != 41)         # uint8(0) ^ 85 != 41
# s.add(bitvecs[0] % 25 < 25)          # uint8(0) % 25 < 25
# s.add((bitvecs[0] & 128) == 0)       # uint8(0) & 128 == 0


# # constraints for _1
# s.add(ULT(bitvecs[1], 158))          # uint8(1) < 158 (unsigned less-than)
# s.add(UGT(bitvecs[1], 19))           # uint8(1) > 19 (unsigned greater-than)
# s.add(bitvecs[1] ^ 85 != 0)          # uint8(1) ^ 85 != 0
# s.add(bitvecs[1] ^ 85 != 232)        # uint8(1) ^ 85 != 232
# s.add(bitvecs[1] % 17 < 17)          # uint8(1) % 17 < 17
# s.add((bitvecs[1] & 128) == 0)       # uint8(1) & 128 == 0


# Constraints for _2 0
s.add(bitvecs[2] + 11 == 119)        # uint8(2) + 11 == 119
s.add(ULT(bitvecs[2], 147))          # uint8(2) < 147 (unsigned less-than)
s.add(UGT(bitvecs[2], 20))           # uint8(2) > 20 (unsigned greater-than)
s.add(bitvecs[2] ^ 85 != 205)        # uint8(2) ^ 85 != 205
s.add(bitvecs[2] ^ 85 != 54)         # uint8(2) ^ 85 != 54
s.add(bitvecs[2] % 28 < 28)          # uint8(2) % 28 < 28
s.add((bitvecs[2] & 128) == 0)       # uint8(2) & 128 == 


c_3_6_uint32 = BitVec('c_3_6_uint32', 32)
# uint32(3) ^ 298697263 == 2108416586
s.add(c_3_6_uint32  ^ 298697263 == 2108416586)

# # Constraints for _3 
# s.add(ULT(bitvecs[3], 141))          # uint8(3) < 141 (unsigned less-than)
# s.add(UGT(bitvecs[3], 21))           # uint8(3) > 21 (unsigned greater-than)
# s.add(bitvecs[3] ^ 85 != 147)        # uint8(3) ^ 85 != 147
# s.add(bitvecs[3] ^ 85 != 43)         # uint8(3) ^ 85 != 43
# s.add(bitvecs[3] % 13 < 13)          # uint8(3) % 13 < 13
# s.add((bitvecs[3] & 128) == 0)       # uint8(3) & 128 == 0


# # Constraints for _4 
# s.add(ULT(bitvecs[4], 139))          # uint8(4) < 139 (unsigned less-than)
# s.add(UGT(bitvecs[4], 30))           # uint8(4) > 30 (unsigned greater-than)
# s.add(bitvecs[4] ^ 85 != 23)         # uint8(4) ^ 85 != 23
# s.add(bitvecs[4] ^ 85 != 253)        # uint8(4) ^ 85 != 253
# s.add(bitvecs[4] % 17 < 17)          # uint8(4) % 17 < 17
# s.add((bitvecs[4] & 128) == 0)       # uint8(4) & 128 == 0


# # Constraints for _5 
# s.add(ULT(bitvecs[5], 158))          # uint8(5) < 158 (unsigned less-than)
# s.add(UGT(bitvecs[5], 14))           # uint8(5) > 14 (unsigned greater-than)
# s.add(bitvecs[5] ^ 85 != 243)        # uint8(5) ^ 85 != 243
# s.add(bitvecs[5] ^ 85 != 43)         # uint8(5) ^ 85 != 43
# s.add(bitvecs[5] % 27 < 27)          # uint8(5) % 27 < 27
# s.add((bitvecs[5] & 128) == 0)       # uint8(5) & 128 == 0


# # Constraints for _6
# s.add(ULT(bitvecs[6], 155))          # uint8(6) < 155 (unsigned less-than)
# s.add(UGT(bitvecs[6], 6))            # uint8(6) > 6 (unsigned greater-than)
# s.add(bitvecs[6] ^ 85 != 129)        # uint8(6) ^ 85 != 129
# s.add(bitvecs[6] ^ 85 != 39)         # uint8(6) ^ 85 != 39
# s.add(bitvecs[6] % 12 < 12)          # uint8(6) % 12 < 12
# s.add((bitvecs[6] & 128) == 0)       # uint8(6) & 128 == 0

# constraints for _7
s.add(bitvecs[7] - 15 == 82)         # uint8(7) - 15 == 82
s.add(ULT(bitvecs[7], 131))          # uint8(7) < 131 (unsigned less-than)
s.add(UGT(bitvecs[7], 18))           # uint8(7) > 18 (unsigned greater-than)
s.add(bitvecs[7] ^ 85 != 15)         # uint8(7) ^ 85 != 15
s.add(bitvecs[7] ^ 85 != 221)        # uint8(7) ^ 85 != 221
s.add(bitvecs[7] % 12 < 12)          # uint8(7) % 12 < 12
s.add((bitvecs[7] & 128) == 0)       # uint8(7) & 128 == 0

# constraints for _8
s.add(ULT(bitvecs[8], 133))          # uint8(8) < 133 (unsigned less-than)
s.add(UGT(bitvecs[8], 3))            # uint8(8) > 3 (unsigned greater-than)
s.add(bitvecs[8] ^ 85 != 107)        # uint8(8) ^ 85 != 107
s.add(bitvecs[8] ^ 85 != 2)          # uint8(8) ^ 85 != 2
s.add(bitvecs[8] % 21 < 21)          # uint8(8) % 21 < 21
s.add((bitvecs[8] & 128) == 0)       # uint8(8) & 128 == 0


# constraints for _9
s.add(bitvecs[9] % 22 < 22)          # uint8(9) % 22 < 22
s.add((bitvecs[9] & 128) == 0)       # uint8(9) & 128 == 0
s.add(ULT(bitvecs[9], 151))          # uint8(9) < 151 (unsigned less-than)
s.add(UGT(bitvecs[9], 23))           # uint8(9) > 23 (unsigned greater-than)
s.add(bitvecs[9] ^ 85 != 164)        # uint8(9) ^ 85 != 164
s.add(bitvecs[9] ^ 85 != 5)          # uint8(9) ^ 85 !=


# constraints for _10
# uint32(10) + 383041523 == 2448764514 
c_10_13_uint32 = BitVec('c_10_13_uint32', 32)
s.add(c_10_13_uint32 + 383041523 == 2448764514)

# constraints for _11
# constraints for _12
# constraints for _13
# constraints for _14
# constraints for _15

# constraints for _16
# uint8(16) % 31 < 31 
# uint8(16) & 128 == 0 
# uint8(16) < 134 
# uint8(16) > 25 
# uint8(16) ^ 7 == 115 
# uint8(16) ^ 85 != 144 
# uint8(16) ^ 85 != 7 
s.add(bitvecs[16] % 31 < 31)          # uint8(16) % 31 < 31
s.add((bitvecs[16] & 128) == 0)       # uint8(16) & 128 == 0
s.add(ULT(bitvecs[16], 134))          # uint8(16) < 134 (unsigned less-than)
s.add(UGT(bitvecs[16], 25))           # uint8(16) > 25 (unsigned greater-than)
s.add(bitvecs[16] ^ 7 == 115)         # uint8(16) ^ 7 == 115
s.add(bitvecs[16] ^ 85 != 144)        # uint8(16) ^ 85 != 144
s.add(bitvecs[16] ^ 85 != 7)          # uint8(16) ^ 85 != 7


# constraints for _17
# constraints for _18
# constraints for _19
# constraints for _20
c_17_20_uint32 = BitVec('c_17_20_uint32', 32)
# uint32(17) - 323157430 == 1412131772
s.add(c_17_20_uint32 - 323157430 == 1412131772)

# constraints for _21
s.add(bitvecs[21] % 11 < 11)          # uint8(21) % 11 < 11
s.add((bitvecs[21] & 128) == 0)       # uint8(21) & 128 == 0
s.add(bitvecs[21] - 21 == 94)         # uint8(21) - 21 == 94
s.add(ULT(bitvecs[21], 138))          # uint8(21) < 138 (unsigned less-than)
s.add(UGT(bitvecs[21], 7))            # uint8(21) > 7 (unsigned greater-than)
s.add(bitvecs[21] ^ 85 != 188)        # uint8(21) ^ 85 != 188
s.add(bitvecs[21] ^ 85 != 27)         # uint8(21) ^ 85 != 27

c_22_25_uint32 = BitVec('c_22_25_uint32', 32)
#uint32(22) ^ 372102464 == 1879700858 
s.add(c_22_25_uint32 ^ 372102464 == 1879700858)


# constraints for _26
s.add(bitvecs[26] % 25 < 25)          # uint8(26) % 25 < 25
s.add((bitvecs[26] & 128) == 0)       # uint8(26) & 128 == 0
s.add(bitvecs[26] - 7 == 25)          # uint8(26) - 7 == 25
s.add(ULT(bitvecs[26], 132))          # uint8(26) < 132 (unsigned less-than)
s.add(UGT(bitvecs[26], 31))           # uint8(26) > 31 (unsigned greater-than)
s.add(bitvecs[26] ^ 85 != 161)        # uint8(26) ^ 85 != 161
s.add(bitvecs[26] ^ 85 != 44)         # uint8(26) ^ 85 != 44


# constraints for _27
s.add(bitvecs[27] % 26 < 26)          # uint8(27) % 26 < 26
s.add((bitvecs[27] & 128) == 0)       # uint8(27) & 128 == 0
s.add(ULT(bitvecs[27], 147))          # uint8(27) < 147 (unsigned less-than)
s.add(UGT(bitvecs[27], 23))           # uint8(27) > 23 (unsigned greater-than)
s.add(bitvecs[27] ^ 21 == 40)         # uint8(27) ^ 21 == 40
s.add(bitvecs[27] ^ 85 != 244)        # uint8(27) ^ 85 != 244
s.add(bitvecs[27] ^ 85 != 43)         # uint8(27) ^ 85 != 43


# constraints for _28
c_28_31_uint32 = BitVec('c_28_31_uint32', 32)
# uint32(28) - 419186860 == 959764852 
s.add(c_28_31_uint32 - 419186860 == 959764852)


# constraints for _36
# uint8(36) % 22 < 22 
# uint8(36) & 128 == 0 
# uint8(36) + 4 == 72 
# uint8(36) < 146 
# uint8(36) > 11 
# uint8(36) ^ 85 != 6 
# uint8(36) ^ 85 != 95 
s.add(bitvecs[36] % 22 < 22)          # uint8(36) % 22 < 22
s.add((bitvecs[36] & 128) == 0)       # uint8(36) & 128 == 0
s.add(bitvecs[36] + 4 == 72)          # uint8(36) + 4 == 72
s.add(ULT(bitvecs[36], 146))          # uint8(36) < 146 (unsigned less-than)
s.add(UGT(bitvecs[36], 11))           # uint8(36) > 11 (unsigned greater-than)
s.add(bitvecs[36] ^ 85 != 6)          # uint8(36) ^ 85 != 6
s.add(bitvecs[36] ^ 85 != 95)         # uint8(36) ^ 85 != 95

c_37_40_uint32 = BitVec('c_37_40_uint32', 32)
# uint32(37) + 367943707 == 1228527996
s.add(c_37_40_uint32 + 367943707 == 1228527996)

c_41_44_uint32 = BitVec('c_41_44_uint32', 32)
# uint32(41) + 404880684 == 1699114335 
s.add(c_41_44_uint32 + 404880684 == 1699114335)

# constraints for _45
s.add(bitvecs[45] % 17 < 17)          # uint8(45) % 17 < 17
s.add((bitvecs[45] & 128) == 0)       # uint8(45) & 128 == 0
s.add(ULT(bitvecs[45], 136))          # uint8(45) < 136 (unsigned less-than)
s.add(UGT(bitvecs[45], 17))           # uint8(45) > 17 (unsigned greater-than)
s.add(bitvecs[45] ^ 85 != 146)        # uint8(45) ^ 85 != 146
s.add(bitvecs[45] ^ 85 != 19)         # uint8(45) ^ 85 != 19
s.add(bitvecs[45] ^ 9 == 104)         # uint8(45) ^ 9 == 104



# constraints for _46
s.add(bitvecs[46] % 28 < 28)          # uint8(46) % 28 < 28
s.add((bitvecs[46] & 128) == 0)       # uint8(46) & 128 == 0
s.add(ULT(bitvecs[46], 154))          # uint8(46) < 154 (unsigned less-than)
s.add(UGT(bitvecs[46], 22))           # uint8(46) > 22 (unsigned greater-than)
s.add(bitvecs[46] ^ 85 != 18)         # uint8(46) ^ 85 != 18
s.add(bitvecs[46] ^ 85 != 186)        # uint8(46) ^ 85 !=
s.add(bitvecs[46] ^ 85 != 186)        # uint8(46) ^ 85 != 186

c_46_49_uint32 = BitVec('c_46_49_uint32', 32)
# uint32(46) - 412326611 == 1503714457 
s.add(c_46_49_uint32 - 412326611 == 1503714457)

c_52_55_uint32 = BitVec('c_52_55_uint32', 32)
# uint32(52) ^ 425706662 == 1495724241 
s.add(c_52_55_uint32 ^ 425706662 == 1495724241)


# constraints for _58
s.add(bitvecs[58] % 14 < 14)          # uint8(58) % 14 < 14
s.add((bitvecs[58] & 128) == 0)       # uint8(58) & 128 == 0
s.add(bitvecs[58] + 25 == 122)        # uint8(58) + 25 == 122
s.add(ULT(bitvecs[58], 146))          # uint8(58) < 146 (unsigned less-than)
s.add(UGT(bitvecs[58], 30))           # uint8(58) > 30 (unsigned greater-than)
s.add(bitvecs[58] ^ 85 != 12)         # uint8(58) ^ 85 != 12
s.add(bitvecs[58] ^ 85 != 77)         # uint8(58) ^ 85 != 77

c_59_62_uint32 = BitVec('c_59_62_uint32', 32)
# uint32(59) ^ 512952669 == 1908304943
s.add(c_59_62_uint32 ^ 512952669 == 1908304943)

# constraints for _65
s.add(bitvecs[65] % 22 < 22)          # uint8(65) % 22 < 22
s.add((bitvecs[65] & 128) == 0)       # uint8(65) & 128 == 0
s.add(bitvecs[65] - 29 == 70)         # uint8(65) - 29 == 70
s.add(ULT(bitvecs[65], 149))          # uint8(65) < 149 (unsigned less-than)
s.add(UGT(bitvecs[65], 1))            # uint8(65) > 1 (unsigned greater-than)
s.add(bitvecs[65] ^ 85 != 215)        # uint8(65) ^ 85 != 215
s.add(bitvecs[65] ^ 85 != 28)         # uint8(65) ^ 85 != 28

c_66_69_uint32 = BitVec('c_66_69_uint32', 32)
# uint32(66) ^ 310886682 == 849718389 
s.add(c_66_69_uint32 ^ 310886682 == 849718389)


# constraints for _70
c_70_73_uint32 = BitVec('c_70_73_uint32', 32)
# uint32(70) + 349203301 == 2034162376
s.add(c_70_73_uint32 + 349203301 == 2034162376)


# constraints for _74
# uint8(74) % 10 < 10 
# uint8(74) & 128 == 0 
# uint8(74) + 11 == 116 
# uint8(74) < 152 
# uint8(74) > 1 
# uint8(74) ^ 85 != 193 
# uint8(74) ^ 85 != 45 
s.add(bitvecs[74] % 10 < 10)          # uint8(74) % 10 < 10
s.add((bitvecs[74] & 128) == 0)       # uint8(74) & 128 == 0
s.add(bitvecs[74] + 11 == 116)        # uint8(74) + 11 == 116
s.add(ULT(bitvecs[74], 152))          # uint8(74) < 152 (unsigned less-than)
s.add(UGT(bitvecs[74], 1))            # uint8(74) > 1 (unsigned greater-than)
s.add(bitvecs[74] ^ 85 != 193)        # uint8(74) ^ 85 != 193
s.add(bitvecs[74] ^ 85 != 45)         # uint8(74) ^ 85 != 45


# constraints for _75
# uint8(75) % 24 < 24 
# uint8(75) & 128 == 0 
# uint8(75) - 30 == 86 
# uint8(75) < 142 
# uint8(75) > 30 
# uint8(75) ^ 85 != 25 
# uint8(75) ^ 85 != 35 
s.add(bitvecs[75] % 24 < 24)          # uint8(75) % 24 < 24
s.add((bitvecs[75] & 128) == 0)       # uint8(75) & 128 == 0
s.add(bitvecs[75] - 30 == 86)         # uint8(75) - 30 == 86
s.add(ULT(bitvecs[75], 142))          # uint8(75) < 142 (unsigned less-than)
s.add(UGT(bitvecs[75], 30))           # uint8(75) > 30 (unsigned greater-than)
s.add(bitvecs[75] ^ 85 != 25)         # uint8(75) ^ 85 != 25
s.add(bitvecs[75] ^ 85 != 35)         # uint8(75) ^ 85 !=

c_80_83_uint32 = BitVec('c_80_83_uint32', 32)
# uint32(80) - 473886976 == 69677856
s.add(c_80_83_uint32 - 473886976 == 69677856)

# constraints for _84
s.add(bitvecs[84] % 18 < 18)          # uint8(84) % 18 < 18
s.add((bitvecs[84] & 128) == 0)       # uint8(84) & 128 == 0
s.add(bitvecs[84] + 3 == 128)         # uint8(84) + 3 == 128
s.add(ULT(bitvecs[84], 129))          # uint8(84) < 129 (unsigned less-than)
s.add(UGT(bitvecs[84], 26))           # uint8(84) > 26 (unsigned greater-than)
s.add(bitvecs[84] ^ 85 != 231)        # uint8(84) ^ 85 != 231
s.add(bitvecs[84] ^ 85 != 3)          # uint8(84) ^ 85 != 3

# constraints for _51
# uint8(51) % 15 < 15 
# uint8(51) & 128 == 0 
# uint8(51) < 139 
# uint8(51) > 7 
# uint8(51) ^ 85 != 0 
# uint8(51) ^ 85 != 204 
s.add(bitvecs[51] % 15 < 15)          # uint8(51) % 15 < 15
s.add((bitvecs[51] & 128) == 0)       # uint8(51) & 128 == 0
s.add(ULT(bitvecs[51], 139))          # uint8(51) < 139 (unsigned less-than)
s.add(UGT(bitvecs[51], 7))            # uint8(51) > 7 (unsigned greater-than)
s.add(bitvecs[51] ^ 85 != 0)          # uint8(51) ^ 85 != 0
s.add(bitvecs[51] ^ 85 != 204)        # uint8(51) ^ 85 != 204


# Check if the constraints are satisfiable
if s.check() == sat:
    m = s.model()
    # Sorting variables by name in lexicographical order and printing their values
    print(f"_0 : _1 --> 'ru' ")
    print(f"_3 : _6 --> '{uint32_to_ascii_string(m[c_3_6_uint32].as_long())}'")
    print(f"_10 : _13 --> '{uint32_to_ascii_string(m[c_10_13_uint32].as_long())}'")
    print(f"_17 : _20 --> '{uint32_to_ascii_string(m[c_17_20_uint32].as_long())}'")
    print(f"_22 : _25 --> '{uint32_to_ascii_string(m[c_22_25_uint32].as_long())}'")
    print(f"_28 : _31 --> '{uint32_to_ascii_string(m[c_28_31_uint32].as_long())}'")
    print(f"_37 : _40 --> '{uint32_to_ascii_string(m[c_37_40_uint32].as_long())}'")
    print(f"_41 : _44 --> '{uint32_to_ascii_string(m[c_41_44_uint32].as_long())}'")
    print(f"_46 : _49 --> '{uint32_to_ascii_string(m[c_46_49_uint32].as_long())}'")
    print(f"_52 : _55 --> '{uint32_to_ascii_string(m[c_52_55_uint32].as_long())}'")
    print(f"_59 : _62 --> '{uint32_to_ascii_string(m[c_59_62_uint32].as_long())}'")
    print(f"_66 : _69 --> '{uint32_to_ascii_string(m[c_66_69_uint32].as_long())}'")
    print(f"_70 : _73 --> '{uint32_to_ascii_string(m[c_70_73_uint32].as_long())}'")
    print(f"_80 : _83 --> '{uint32_to_ascii_string(m[c_80_83_uint32].as_long())}'")
    for var in sorted(m, key=lambda x: str(x)):
        value = m[var].as_long()
        char = chr(value) if 32 <= value <= 126 else '?'  # Printable ASCII range check
        print(f"{var} = {value} --> '{char}'")  # Print the variable, value, and ASCII char
else:
    print("Unsatisfiable")
