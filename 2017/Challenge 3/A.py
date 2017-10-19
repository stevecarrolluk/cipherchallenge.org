import matplotlib.pyplot as plt
string = "ICROCI,\nG FZWMSZF YWIE IWRE CJWMF AZCF OWM YCGX GP FZE ZWYDGFCB, CPX SGTEP AZCF ZCY ZCDDEPEX G FZGPU G GF AWMBX JE SWWX FW AWRU FWSEFZER.\nMPLWRFMPCFEBO GF YEEIY FZCF G CI PWF FZE WPBO WPE FROGPS FW LGPX FZE JWWU. FZERE GY C FZRGTGPS JBCQU ICRUEF CIWPS JGJBGWDZGBEY LWR CPOFZGPS CY WBX CY FZGY. GF GY TERO TCBMCJBE CPX GL FZE JWWU XGYCDDECRY GPFW FZE YZCXWAO AWRBX WL DRGTCFE BGJRCRGEY AE IGSZF PWF YEE GF CSCGP LWR QEPFMRGEY YW GF GY RECBBO GIDWRFCPF AE SEF FW GF LGRYF.\nFCQGFMY QBECRBO ACPFEX FW ICUE GF XGLLGQMBF FW CYYEIJBE FZE EPFGRE XWQMIEPF, YW ZE ZCX GF ZGXXEP CF C PMIJER WL YGFEY CRWMPX FZE CPQGEPF AWRBX. FZE JRGFGYZ BGJRCRO XEQGXEX FW YEPX YWIEWPE FW FRO FW LGPX CBB FZE DGEQEY. FZEGR EHDERFY LGSMREX FZE QZCDFERY AERE BGUEBO FW JE EPQRODFEX FWW YW, SGTEP IO JCQUSRWMPX, FZEO CYUEX IE FW SW. FZEO AERE RGSZF WL QWMRYE, FZE LGRYF QZCDFER ACY XGYSMGYEX MYGPS C QCEYCR YZGLF CPX FZE YEQWPX JO C YQOFCBE QGDZER, CPX G CI JESGPPGPS FW AWPXER AZCF WFZER QGDZERY FCQGFMY IGSZF QZCBBEPSE MY AGFZ. CY LCR CY AE UPWA FZE RWICPY AWMBX PWF ZCTE ZCX FZCF ICPO FW QZWWYE LRWI. G YMDDWYE ZE IGSZF ZCTE UPWAP CJWMF YWIE LWRI WL FZE DWBOJGMY QGDZER.\nFZE XWQMIEPFY G ZCTE LWMPX YW LCR (FCQGFMY BCYF FEYFCIEPF CPX QZCDFERY WPE CPX FAW WL ZGY ZGXXEP JWWU) ECQZ SGTE C QBME FW FZE BWQCFGWP WL FZE PEHF WPE, CPX CY YWWP CY FZEO BEF IE WMF WL ZWYDGFCB G DBCP FW FRO FW BWQCFE FZE FZGRX QZCDFER, AZGQZ FCQGFMY FEBBY MY GY ZGXXEP WP FZE GYBE WL FZWRPY. FZERE CRE YETERCB DBCQEY GP FZE CPQGEPF AWRBX FZCF FZGY IGSZF RELER FW, JMF G ZCTE C DREFFO SWWX GXEC WL AZERE GF IGSZF JE.\nGL G FZGPU WL CPOFZGPS EBYE G AGBB SEF GF FW OWM, CPX CY REKMEYFEX G AGBB QWDO GP OWMR LRGEPX ZCRRO. G YMSSEYF AE FGSZFEP YEQMRGFO C BGFFBE. ICOJE GL AE JBWQU WMR QGDZER FEHFY BGUE FZE EHDERFY GF AGBB DMF WLL QCYMCB GPFERQEDFY. FZE DEWDBE AE CRE MD CSCGPYF CRE MPBGUEBO FW JE XEFERREX JO IMQZ, JMF AE XWP'F ACPF FW GPTGFE EHFRC GPFERBWDERY FW FZE DCRFO.\nJO FZE ACO, IO LRGEPX GP FZE YWMU FWBX IE FZCF ZE IEF WPE WL OWMR CSEPFY AZW ACY CYUGPS GL ZE UPEA AZERE G ACY, AZGQZ YEEIY C JGF WXX SGTEP FZCF OWM UPWA G CI YFMQU ZERE. ACY FZCF NMYF FW FZRWA WMR RGTCBY WLL FZE YQEPF?\nCBB FZE JEYF,\nNWXGE"

ASCII = [[0, chr(i)] for i in range(0,255)]
for letter in string:
    if ord('A')<=ord(letter)<=ord('Z'):
        ASCII[ord(letter)][0] += 1
ASCII.sort()
ASCII.reverse()
print(ASCII)
slownik = {
    "E" : "E" ,
    "F" : "T" ,
    "G" : "I" ,#
    "W" : "O" ,
    "C" : "A" ,
    "Z" : "H" ,#
    "Y" : "S" ,
    "P" : "N" ,
    "R" : "R" ,#
    "B" : "L" ,
    "X" : "D" ,#
    "M" : "U" ,
    "Q" : "C" ,
    "A" : "W" ,
    "O" : "Y" ,#
    "L" : "F" ,
    "I" : "M" ,#
    "S" : "G" ,
    "D" : "P" ,
    "J" : "B" ,
    "U" : "K" ,
    "T" : "V" ,#
    "H" : "X" ,
    "N" : "J" ,
    "K" : "Q"
}
res = ""
for letter in string:
    if ord('A')<=ord(letter)<=ord('Z'):
        res+=(slownik[letter])
    else:
        res+=(letter)
a1 = [a[0] for a in ASCII[0:25]]
a2 = [b[1] for b in ASCII[0:25]]
print(a1)
print(a2)
plt.bar(range(0,25), a1)
#plt.show()
print(res)