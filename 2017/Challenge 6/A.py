string = "Lelqzq, C xnyhv Isxad en Gkcghhe ufc wbw gem ugejldv maw efjdexq. Rly zzh vwdr fwzhcff xbw LMXSR sjwqenauim gm e qakh agnwy ugemw zvimmh Mwkgoc leeamk u dnx ix msckd evgtx fgnocff jij sly ehwmamk wzztnwq en lgi Nwltfw nj Ujsigar. Xbss kund qy lhqy ln vylqmynd mn xqsg Bnhcw'r jladrx ss xbw Avclhwb Etwyml, ababl bsr e wgkpyusmif nj ujsizsbxm xqsg lgi Nwltfw. Isxad wuqr wbw jryo vi qgtpx xhkojd sol vlyjd xi yn ryps. Xbw bpow vem am xbw kswssmifr. Xbw emlks shw vem ss xbw Fvyss Tsjzqcv, sly kdgifc en lgi zgqx ix Peclaes ogmwz vem ttmfl evie sly jtmhk nj nzd Pcygxbgtwy ss Efwwehvqmu smh nzd xbaqh if Qlivdw, uenra lgi lmhrm ge xbw Bsfgrwok. Sly Cmmazs'w wsrxfw zx Vgcvoe vem ttmfl evie sly jdquamw ix sly Ezymgkioe zx Bskmwsqrukrym, zdrww sly “yqepw” semc nj amzvxamk nzd figj. Wi skp zaui wzztnwqw qwqi zgtrx ss xbw rmnw nj ifd sz lgi Mwuih Onrxwqw ix sly smgcwmx qgqpx. Lgi ifkc lwlecfhra dngulhshk zvy lgi Mlzxow nj Twtw ul Npseomu smh nzd Luffmhy Felvdrm ge Futxpif, zrx fn-shw gem smc cvde qzdvy lgi asqhyfr qcygx bsui vwdr, mg sly gmps hkeww vi wgtpx yn ryps mm Gkcghhe. Nzd gfmd en lgi yfc sz ugejldv zaui jghrnk rxlshkbl slyjd, wcfbi faflnamk, vmkp ufc suc zvy skp mqlfidr sz Rdym. Od wbgtpx td wuxd lyjd fyuzymw Isxad'w hwsaijj luk rihl gil ssxuujilk nr ng Kshvnr vq kesamk u dnra lqecd nj zgqkyv cswmlihlr vyndefamk nzd piuzxcgm sz ugejldv zaui. Nzzx vgtkbl tw yfnyaz smgw ss fgbenw zrx vdgchgil ugejldv maw. Ay zzh vwdr nzhreamk utnyn lgi ynnpolhsh ge xbw Hqjwqmud Bmjzdvm. Lzgcltw okdh vgsl nzd Zcydryjd ehv Aiumesll bmjzdvm ogmwz zvy hnpssktbsainab zyjrmifr sz lgi Wsdwuj rlcxs, ehv zx zaqwn od emktqyv slul bluhsil khb qgtpx td ihuqcjldh nzd wued auq. Vi qwqi udlsml qmazs. Qysmabaki Dgcmy'k trypoiwldh nskihl esl xnvawqc bsr kcndr gw zr cvde. C lgmhc vi gafln td evdd xi ltvh gtv yfdqcwr sh gmi ufnxbwq fs wwtfghxcff lyj fmzl, ayn A jrio gil utvlwmx zgbym ar jcytvcff sol vlyjd sh wzvnz sly kdzyfsl qgmhyj lmazs fy."
key='ZEUS'
keytable=[(ord(char)-ord('A'))%26 for char in key]
print(keytable)
index = 0
result = ""
for letter in string:
    if ord('a') <= ord(letter) <= ord('z'):
        result += chr((ord(letter) - ord('a') - keytable[index % 4]) % 26 + ord('a'))
        index += 1
    elif ord('A') <= ord(letter) <= ord('Z'):
        result += chr((ord(letter) - ord('A') - keytable[index % 4]) % 26 + ord('A'))
        index += 1
    else:
        result += letter
print(result)