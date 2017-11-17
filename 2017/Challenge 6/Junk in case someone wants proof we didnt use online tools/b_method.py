string = "Ykuf rqhuddq rgz ppismxooeyz ud ogmp prlzqa er lop nlovktvfnx oyzcqdzov dve cxuaibk vg Lbejrvpsl arh dtwobnim lw Dfgg ta uqg onb lr fln mgmd, rp ybvigkx vx dbo Qxugbuv. Ok lqlpgh rov amgi ukrdphdo qeo ei giukx ivd ly Jlzipege lw vfdb Mdbsgzkc Gsysoooi oeo Boptemmk Hcrocvn, lwd jok Sigw codt jgzcvlsy oyv, touriwmhfd lzq kuai ia wbo Oamkh dngeqbto e icugkf, gyucz iesq pu g aka nfmel clztmvin rrir dbo Bvghj. Bqyhgckm sjilpizq jl xeelpz jsn oycqim jmdhkip ia wbo Aobmbo lw e sogl yv oabxcen, dbo Qxugbuv njcdnv bqu uqg vajt cl ioxgb jvpubautd sqyctmnn trh, da ufe kvpfbsnv yv waxk, zq jaa mmrizov jgmmumxel jthybajvcpk. L whmrbv cmw igkqrnv ly rov Aonguk wb oxg gdmvt gj jok Eumctgd, ydh, paytv gnk, Aubsfndm ygn eebo dy lsiv mweiuho iy xii xrzilm inlcrn ybodt qg kac ukpjnv ly rov Gsbigcr’k fyr nldpiaegee. Zsh vgmro rei a wgmeffka illhw pu mt, ipj l beqbadd oriel fi lzd jsn ctqctme. Gr jaa vqqw ei a vtib nfwa oftg ly ddlee rf ybgu ov cmw tll dqawyzoqsq enapv. Pyrhgbk, xntouxtx, wx oxg nisddmoi rvx ric lwkd zeiwin wcun dy jsn qywwi; rvx sy botnvh flaute, cbg ybodtkgb stlly iu delgtia kcvt iykngllqm, qii ngxk aoh ur mnq sinw; tlx xsg a aqbhsg iuqq cp lnatqbh nn jec mkcri pgxivhg md jok pqjw yb xliuod ku qmszsdy. Roxa immsiflx yei sehtoactd ja oxg ksmv-anpird ryruob roth jc drd jqnn toulkgh hs scgkfn yz rov Gsbigcr’k zuksoeo. Zggkumcb kuap bl wisc ke idpferpsej hjc gxpgrpuoi Krsoidkbe Byzkdlyn ta pxi eka efrgbbli yv ddt jriceraq. Ov cmw uoirenv cqro pgakvvvs ric nbohxdo birwe mpdb Aoqvzgnkr ipj icehqm wbopi uc qiyjtgbu Helqgfsy. So yei iesq pxie lzoo dbo nlpa gj jok Qigcj kon igdcgqkx. Klzoirvda kpauk wx iea illhw md jok pqjw iz o qvhpcv uc Qoou zmrto hjc pvrfl gaq tqanto ddt acnnnzi ia Zey et ufe anat gx uqg autnsbkiefi ia Zeboqn Irdnoizyn Hdogiee GS lnz Lyfxoi Hgtpgyh Xyzigthww. “Et irq nffbqnpdy odrxsqg hq gyg zyid mbvgxpogzr rgz cpirl Eumctgd Mnkqdkrv fi hcswdt Uer Paxipo pn hjq Entpxigv Usyqzgun trh miu uwy jpipq un ko up ufe nfwa gx uqg Aubtn Wczkdpigdk. Yuqg heogct Megxsgzg oiy okpgmjd ueqv jok ddpog gx ndsj a fley, vvd iv ald zg nau xecfrgb rov Sgviw pexfpg plt ueiwkey wx oxg yqri hjct dcm ulm lo kbig pxgu uwy jedl zlxr jem. Dcm rnzd sq uqep etukbnpqgzct ctgg g fidrvpgh ksf awqwtefk oxep rov hbakucr Clzumcbp bmw jok Qigcj mbm xa sacnmpe iea iysuybdige gb oxg Zigwb. Kxkqk fln Hebvriimnc ufeuhcddqn tto ktqmuqkm hg urlg skuo cl ric Sgjty, Smzwrwmk pw ez qmdsmdim Xwuln ezj ov kwwj yk yrfbfoj yvngpi ok qoy vgirgnq pxi nkqyaehy ia wbo Emskrslz sqpovti. Ddt Wwjnf cqnq ag bculzednv, yb ald, qgkv aiiskm ezj tkgbmaek oiv srgm pxdl bgd lzq mpiaq. Rgz iu jl lzq hcvobuq fmpj lr fln dtwq nwybm aa Isdpoylo vg cjeuo lzq uaho ia wbo nkelz nnqigb rgz gj jok Qigcj qrnvdv ykqh gb oeko vt igdcgqkx. Yydil rovr qd evhb vn qomdmvz tm jok cbzegzr Ytlyzaemcb Buzhqnp yv Ygg."
e_freq = "etaoinshrdlcumwfgypbvkjxqz"
proper_e = [char for char in e_freq]
abies = [[] for i in range(15)]
print(proper_e)
text = ""
for letter in string:
    if ord('a') <= ord(letter) <= ord('z'):
        text += letter
    if ord('A') <= ord(letter) <= ord('Z'):
        text += chr(ord(letter)-ord('A')+ord('a'))
popularity = [[[0, chr(i+ord('a'))] for i in range(26)] for j in range(15)]

index = 0
for letter in text:
    popularity[index%15][ord(letter)-ord('a')][0] += 1
    index += 1
it1 = 0
for column in popularity:
    column.sort()
    column.reverse()
    print(column)
    for




"""
for column in popularity:
    column.sort()
    column.reverse()
    for index2 in range(26):
        column[index2] = [proper_e[index2], ord(column[index2][1])-ord('a')]
    column.sort()
    column2 = column.copy()
    for index2 in range(26):
        column2[index2] = str(column2[index2][1])
        if len(column2[index2]) == 1:
            column2[index2] = '0' + column2[index2]
    print(column2[4], column2[19])
    abies[it1] = [int(column2[4]), int(column2[19])]
    it1 += 1
for index in range(26):
    proper_e[index] = ' ' + chr(index+ord('a'))
print(proper_e)
index = 0
result = ""
for letter in string:
    if ord('a') <= ord(letter) <= ord('z'):
        result += chr(((ord(letter) - ord('a')) - popularity[index%15][ord(letter) - ord('a')][1])%26 + ord('a'))
        index += 1
    elif ord('A') <= ord(letter) <= ord('Z'):
        result += chr(((ord(letter) - ord('A')) - popularity[index%15][ord(letter) - ord('A')][1])%26 + ord('A'))
        index += 1
    else:
        result += letter
print(abies)

for row in abies:
    fifteena = row[0]+row[1]
    while fifteena%15!=0:
        fifteena += 26
    a = int(fifteena/15)
    b = int((row[0]-4*a)%26)
    print(a,b)
    row = [a,b]

print("a   b")
print(abies)

index = 0
result = ""

for letter in string:
    if ord('a') <= ord(letter) <= ord('z'):
        result += chr(((ord(letter) - ord('a'))*abies[index%15][0]+abies[index%15][1]) % 26 + ord('a'))
        index += 1
    elif ord('A') <= ord(letter) <= ord('Z'):
        result += chr(((ord(letter) - ord('A'))*abies[index%15][0]+abies[index%15][1]) % 26 + ord('A'))
        index += 1
    else:
        result += letter

print(result)
"""