string = "UGXXV,\n\nBGXVGB THQQRTKRF N QRK NY KCHZU GT PR YRRF G ZCHXNRX GYF TUR KUCHQUK VCH BNQUK AR NYKRXRTKRF NY SCNYNYQ HT. URX TCHXZRT UGOR ZCYENXBRF KUGK KUR ACCL NT ARNYQ UHYKRF AV GY NIIRQGI EHYFXGNTNYQ QXCHM YGBRF BNFGT PUNZU UGT ARRY GTTCZNGKRF PNKU TRORXGI KRXXCX YRKPCXLT NY KUR IGTK ERP VRGXT. BGXVGB UGT KXGORIIRF KC NTKGYAHI ECIICPNYQ G IRGF CY KUR AHVRX NY KUR UCMR PR ZGY TZGXR KURB CEE, AHK NE KUGK FCRTY’K PCXL KURY PR PNII YRRF KC ENYF KUR XRTK CE KUR ACCL ZUGMKRXT ARECXR BNFGT FC. PR GXR ACKU UCMNYQ VCHX FNGXV NT ZIRGX, ARZGHTR NE N GB XNQUK PR PNII UGOR GYCKURX KUXRR MIGZRT KC ONTNK GEKRX KUNT CYR, GYF N GB YCK THXR UCP ICYQ NK PNII KGLR.\n\nN ENYNTURF BV PCXL CY KUR KUNXF ZUGMKRX CE KGZNKHT’T BCYCQXGMU PUNZU N ECHYF CY XUCFRT. NK PGT ZCYZRGIRF NY G IGXQR TKCYR INYKRI ARGXNYQ GY NBGQR CE G XCTR, KUR TVBACI CE KUR ZCYTCXK CE KUR THY QCF URINCT. NYKXNQHNYQIV XUCFRT NT GITC LYCPY GT KUR NTIGYF CE KUR LYNQUKT, YGBRF GEKRX KUR LYNQUKT CE TGNYK SCUY CE SRXHTGIRB, GYF KUR ZIHR GK KUR RYF CE ZUGMKRX KUXRR MCNYKRF KC GYCKURX UCBR CE KUR LYNQUKT GK ACFXHB, TC N KXGORIIRF KURXR GYF PGT YCK KCC THXMXNTRF KC ENYF ZUGMKRX ECHX ZCYZRGIRF NY KUR XRBGNYT CE KURNX ECXK. N PGT UCPRORX GTKCYNTURF AV KUR KRJK! NK KCCL BR G PUNIR KC ZXGZL NK GT N FNFY'K XRZCQYNTR KUR RYZXVMKNCY GT GYVKUNYQ ZIGTTNZGI. PURY N ENYGIIV AXCLR NK N FNTZCORXRF KUGK KGZNKHT UGF HTRF G ZNMURX KUGK PR KUCHQUK UGF ARRY NYORYKRF NY TNJKRRYKU ZRYKHXV EXGYZR. NK TRRBT KUGK KUR NBMRXNGI ZNMURX TZUCCI PRXR BHZU BCXR GFOGYZRF KUGY PR UGF GYV XRGTCY KC RJMRZK. NE ZCHXNRX FHKV NTY'K RJZNKNYQ RYCHQU ECX VCH MRXUGMT KUR ZUGYZR KC FNTZCORX BCXR NBMRXNGI ZNMURXT PNII AR?\n\nKUR ZIHR GK KUR RYF CE KUNT ZUGMKRX NT ORXV THQQRTKNOR, GYF N UGOR ACHQUK G KNZLRK KC TRIZHL KC NYORTKNQGKR. N GB MXRKKV THXR N PGT ECIICPRF KC KUR KNZLRK CEENZR.\n\nNE VCH ZGY ZCBR KURY PR YRRF VCH KC FXCM AV KUR AXNKNTU BHTRHB ARECXR VCH ZCBR CHK. N KUNYL KURXR NT TCBRKUNYQ KURXR KUGK PR YRRF GYF PNII TRYF G BRTTGQR KC BV ZCYKGZK NY XCCB KPRYKV KPC KRIINYQ KURB KC RJMRZK VCH GYF AXNRENYQ KURB CY PUGK KC ICCL CHK ECX. NK PCHIF AR QCCF NE VCH ZCHIF AR ORXV FNTZXRRK GACHK KUGK, AHK BGLR GT BHZU EHTT GT VCH INLR GACHK BRRKNYQ BR NY TRIZHL. N PNII RJMIGNY IGKRX!\n\nGII KUR ARTK,\n\nSCFNR"
key = "BMO_FDAULXTKPIVWGEJSHY_RNC"
newstring = ""
index = 0
for letter in string:
    if ord('A')<=ord(letter)<=ord('Z'):
        newstring += key[ord(letter)-ord('A')]
        index += 1
    else:
        newstring+=letter
print(newstring)
