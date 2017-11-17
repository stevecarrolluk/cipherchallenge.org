from matplotlib import pyplot as plt
string = "Ykuf rqhuddq rgz ppismxooeyz ud ogmp prlzqa er lop nlovktvfnx oyzcqdzov dve cxuaibk vg Lbejrvpsl arh dtwobnim lw Dfgg ta uqg onb lr fln mgmd, rp ybvigkx vx dbo Qxugbuv. Ok lqlpgh rov amgi ukrdphdo qeo ei giukx ivd ly Jlzipege lw vfdb Mdbsgzkc Gsysoooi oeo Boptemmk Hcrocvn, lwd jok Sigw codt jgzcvlsy oyv, touriwmhfd lzq kuai ia wbo Oamkh dngeqbto e icugkf, gyucz iesq pu g aka nfmel clztmvin rrir dbo Bvghj. Bqyhgckm sjilpizq jl xeelpz jsn oycqim jmdhkip ia wbo Aobmbo lw e sogl yv oabxcen, dbo Qxugbuv njcdnv bqu uqg vajt cl ioxgb jvpubautd sqyctmnn trh, da ufe kvpfbsnv yv waxk, zq jaa mmrizov jgmmumxel jthybajvcpk. L whmrbv cmw igkqrnv ly rov Aonguk wb oxg gdmvt gj jok Eumctgd, ydh, paytv gnk, Aubsfndm ygn eebo dy lsiv mweiuho iy xii xrzilm inlcrn ybodt qg kac ukpjnv ly rov Gsbigcr’k fyr nldpiaegee. Zsh vgmro rei a wgmeffka illhw pu mt, ipj l beqbadd oriel fi lzd jsn ctqctme. Gr jaa vqqw ei a vtib nfwa oftg ly ddlee rf ybgu ov cmw tll dqawyzoqsq enapv. Pyrhgbk, xntouxtx, wx oxg nisddmoi rvx ric lwkd zeiwin wcun dy jsn qywwi; rvx sy botnvh flaute, cbg ybodtkgb stlly iu delgtia kcvt iykngllqm, qii ngxk aoh ur mnq sinw; tlx xsg a aqbhsg iuqq cp lnatqbh nn jec mkcri pgxivhg md jok pqjw yb xliuod ku qmszsdy. Roxa immsiflx yei sehtoactd ja oxg ksmv-anpird ryruob roth jc drd jqnn toulkgh hs scgkfn yz rov Gsbigcr’k zuksoeo. Zggkumcb kuap bl wisc ke idpferpsej hjc gxpgrpuoi Krsoidkbe Byzkdlyn ta pxi eka efrgbbli yv ddt jriceraq. Ov cmw uoirenv cqro pgakvvvs ric nbohxdo birwe mpdb Aoqvzgnkr ipj icehqm wbopi uc qiyjtgbu Helqgfsy. So yei iesq pxie lzoo dbo nlpa gj jok Qigcj kon igdcgqkx. Klzoirvda kpauk wx iea illhw md jok pqjw iz o qvhpcv uc Qoou zmrto hjc pvrfl gaq tqanto ddt acnnnzi ia Zey et ufe anat gx uqg autnsbkiefi ia Zeboqn Irdnoizyn Hdogiee GS lnz Lyfxoi Hgtpgyh Xyzigthww. “Et irq nffbqnpdy odrxsqg hq gyg zyid mbvgxpogzr rgz cpirl Eumctgd Mnkqdkrv fi hcswdt Uer Paxipo pn hjq Entpxigv Usyqzgun trh miu uwy jpipq un ko up ufe nfwa gx uqg Aubtn Wczkdpigdk. Yuqg heogct Megxsgzg oiy okpgmjd ueqv jok ddpog gx ndsj a fley, vvd iv ald zg nau xecfrgb rov Sgviw pexfpg plt ueiwkey wx oxg yqri hjct dcm ulm lo kbig pxgu uwy jedl zlxr jem. Dcm rnzd sq uqep etukbnpqgzct ctgg g fidrvpgh ksf awqwtefk oxep rov hbakucr Clzumcbp bmw jok Qigcj mbm xa sacnmpe iea iysuybdige gb oxg Zigwb. Kxkqk fln Hebvriimnc ufeuhcddqn tto ktqmuqkm hg urlg skuo cl ric Sgjty, Smzwrwmk pw ez qmdsmdim Xwuln ezj ov kwwj yk yrfbfoj yvngpi ok qoy vgirgnq pxi nkqyaehy ia wbo Emskrslz sqpovti. Ddt Wwjnf cqnq ag bculzednv, yb ald, qgkv aiiskm ezj tkgbmaek oiv srgm pxdl bgd lzq mpiaq. Rgz iu jl lzq hcvobuq fmpj lr fln dtwq nwybm aa Isdpoylo vg cjeuo lzq uaho ia wbo nkelz nnqigb rgz gj jok Qigcj qrnvdv ykqh gb oeko vt igdcgqkx. Yydil rovr qd evhb vn qomdmvz tm jok cbzegzr Ytlyzaemcb Buzhqnp yv Ygg."
text = ""
index = 0
for letter in string:
    if ord('a') <= ord(letter) <= ord('z'):
        text += chr(ord(letter) +ord('A') - ord('a'))
        index +=1
    elif ord('A') <= ord(letter) <= ord('Z'):
        text += letter
        index +=1
    else:
        pass
for columno in range(0, 15):
    sample = []
    tempindex = columno
    while tempindex < len(text):
        sample.append(text[tempindex])
        tempindex += 15
    freq = [0 for j in range(0, 26)]
    for letter in sample:
        freq[ord(letter) - ord('A')] += 1
    print(chr((freq.index(max(freq)) - ord('E')) % 26 + ord('A')))
    freq.sort()
    freq.reverse()
    print(freq)
    plt.bar(range(0, len(freq)), freq)
    plt.title(str(columno))
    plt.show()