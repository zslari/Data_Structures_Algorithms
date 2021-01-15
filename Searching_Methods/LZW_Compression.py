"""
Using Python's Built-in Searching Methods
Created By: Zafir Lari
Application: LZW Compression

Description: This application implements an LZW
Compression encoder using Python's built-in search methods
and datatypes.
"""


# Establish dictionary of uppercase letters A-Z, space, comma, and period
dictionary = {chr(i + 65): i for i in range(0, 26)}
dictionary[chr(32)] = 26
dictionary[chr(44)] = 27
dictionary[chr(46)] = 28


def LZW(file: str):
    """ Appends new character strings to global dictionary if
    they do not already appear in the dictionary. """
    codevalue = 29
    p = ""
    result = []

    for c in file.upper():
        pc = p + c
        if pc in dictionary:
            p = pc
        else:
            result.append(dictionary[p])
            dictionary[pc] = codevalue
            codevalue += 1
            p = c
    if p != '':
        result.append(dictionary[p])
    return result


def test_run():
    """ Reads and encodes data from 'data.txt' file and writes
    encoded values to 'zllzw.txt' file. Prints all encoded keys value
    pairs that have been added to the dictionary.
    """
    test = str(open('data.txt').read().replace('\n', " "))
    outputfile = open("zllzw.txt", 'w')
    outputfile.write(str(LZW(test)).strip('[').strip(']'))
    outputfile.close()
    for key, value in dictionary.items():
        print(f'{key:<3} {value}')


if __name__ == "__main__":
    test_run()


""" Sample Run 
A   0
B   1
C   2
D   3
E   4
F   5
G   6
H   7
I   8
J   9
K   10
L   11
M   12
N   13
O   14
P   15
Q   16
R   17
S   18
T   19
U   20
V   21
W   22
X   23
Y   24
Z   25
    26
,   27
.   28
TH  29
HE  30
E   31
 T  32
TI  33
IM  34
ME  35
E T 36
TR  37
RA  38
AV  39
VE  40
EL  41
LL  42
LE  43
ER  44
R,  45
,   46
 F  47
FO  48
OR  49
R   50
 S  51
SO  52
O   53
 I  54
IT  55
T   56
 W  57
WI  58
IL  59
LL  60
 B  61
BE  62
E C 63
CO  64
ON  65
NV  66
VEN 67
NI  68
IE  69
EN  70
NT  71
T T 72
TO  73
O S 74
SP  75
PE  76
EA  77
AK  78
K   79
 O  80
OF  81
F   82
 H  83
HI  84
IM, 85
,   86
 WA 87
AS  88
S   89
 E  90
EX  91
XP  92
PO  93
OU  94
UN  95
ND  96
DI  97
IN  98
NG  99
G   100
 A  101
A   102
 R  103
RE  104
EC  105
CON 106
NDI 107
ITE 108
E M 109
MA  110
AT  111
TT  112
TE  113
ER  114
 TO 115
O U 116
US  117
S.  118
.   119
 HI 120
IS  121
S G 122
GR  123
REY 124
Y   125
 EY 126
YE  127
ES  128
S S 129
SH  130
HO  131
ONE 132
E A 133
AN  134
ND  135
    136
 TW 137
WIN 138
NK  139
KL  140
LED 141
D,  142
, A 143
AND 144
D   145
 HIS 146
S U 147
USU 148
UA  149
AL  150
LLY 151
Y P 152
PA  153
ALE 154
E F 155
FA  156
AC  157
CE  158
E W 159
WA  160
AS  161
 FL 162
LU  163
USH 164
HED 165
D A 166
AND  167
 AN 168
NIM 169
MAT 170
TED 171
D.  172
. T 173
THE 174
E   175
 FI 176
IR  177
RE  178
 BU 179
UR  180
RN  181
NE  182
ED  183
D B 184
BR  185
RI  186
IG  187
GH  188
HT  189
TL  190
LY  191
Y A 192
AND T 193
THE  194
 SO 195
OFT 196
T R 197
RAD 198
DIA 199
ANC 200
CE  201
 OF 202
F T 203
THE I 204
INC 205
CA  206
ANDE 207
ESC 208
CEN 209
NT  210
  L 211
LI  212
IGH 213
HTS 214
S I 215
IN  216
 TH 217
HE  218
 L  219
LIL 220
LIE 221
ES  222
 OF  223
 SI 224
ILV 225
VER 226
R C 227
CAU 228
UG  229
GHT 230
T TH 231
HE B 232
BU  233
UB  234
BB  235
BL  236
LES 237
S T 238
THA 239
AT  240
 FLA 241
ASH 242
HED  243
 AND 244
D   245
 P  246
PAS 247
SS  248
SE  249
ED  250
 IN 251
N   252
 OU 253
UR  254
 G  255
GL  256
LA  257
ASS 258
SES 259
S.  260

Process finished with exit code 0
"""







