from matplotlib import pyplot as plt
#key = "11001110111011101110111011101110111011101110111011101110111011101110111011101110011101101010101010101010101010101010101010101010101010101010101010101010101010101011011101000100010001000100010001000100010001000100010001000100010001000100010001000101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111111111111111111111111111111111111111111111111111111111111111111111111111110111011111111111111111111111111111111111111111111111111111111111111111111111111111110111011110111000111110001110111011101110111100011011101000111000011000111000110001011101111010110110111011111010110011011010111101110010010110110111110110111011110111011101101110101110101111101110101010101110111011101010101101101111101110110111101101110111000001000011011111000001010101000001110111011101000011000111000011101111011101110110111010101110111110111010101010111011101110111010111110111110101111011110110111011101110101101110111101110101100101110111011101110101111101111101101110111101110111011011101011101110001011101011101011101100011011101011111000011011101000110001011101111111111111111111111111111111111111111111111111111111111111111111111111111111011101111111111111111111111111111111111111111111111111111111111111111111111111111101110101110111011101110111011101110111011101110111011101110111011101110111011101110101110101010101010101010101010101010101010101010101010101010101010101010101010101010111011000100010001000100010001000100010001000100010001000100010001000100010001000110111011011101110111011101110111011101110111011101110111011101110111011101110111011011"
string = "Se vsv Rusyrrx fayyx ute Emaz ud Mpjmmwr ec lke kwrl mi hbi nqeqopzvsyi uh Nengepjii Ugxbhkz Giljjm Ymwxbrjivgz Npzhasx Zjrwgz cnk Uievm Purnnrsti Cmetjginxk, Ahjakbtr mrmyy “Hgw woxlnrk mm jtj zitwtn ip Yrqgcmfyckf aq ay ravh qyejnf. Gagwalgq apg qe i Zrlznjamc rdm, hgy vw raq m Yqfiv yjjsowv tiae, mbm qyhwakim kz ixp moj cmni bz r hijqcjfav. Ew xrq pahyn npx ar mhaxpz ci n pemmaa ud onp hz qeia xjw ipjhw. Ute Blyjuvnrujji qxlro pbwjl wswvecyz feijwnfnc zli rvf yaiwc eiox ld elwpihj taa hr aenweww imr tia zbion vw mjusjxy otme ii, mgp fhm gadw jk lwwgebkz. Ap sz jtj mvbr crrf pnxh um tbpg jv uga kwnjgf kqa qipwchfmv mcb ybe jnjgwn uh wxn qpmgyn Nkoeeen. Ad en aaa axub nngufnl hgw Gymau pbwe nwwtixx wyq xmzk ynn hi nqegeagyx nnf yvn ganwz gscp hi xprrex.” Aypjaqecy ybe Jdqaa hrmhldr Gagwalgq avmy bifn khtyy ec lke tjdix Nurenqgi’q hklmnh, hsw xn wixn c lnyp qhlk pbw ayonsvecy Pixwoonfs izm lainwgrwk nuvwx yu edpvaaue tia craidpww vuv wxn Isgjraj avj wxn Guxnf. Zth pfl cxvvsew Ynpejbrjiv hauzjiwmc mnp indjtjj pvpp rvf layijnpim Elraydra rspf p zdrcwae ytnvecygk iizyompej twyb talyi ijua wxn humhk iumxic ikev hky hwshi yeeqiyhyx Bmvu Jnrotsxk. Vzj pyb tdvc hky iznq yk Ndwe trz gaxevlmyawayyx ute xlqcxe se Bjfhizcwr ivx vvscw pfl Eboapr ov ute Blyjuv trz zjwv vlmyurwo bc ute isckivun, jtjsr fbrdor erk nzh. Igywpuxa mcyjx i vllxrv hd Lmbw, bsdwgaihjon nnf mesdqp ynlhnsv jleyb. Ptn ksqhb kiecpej dx op hibl qm muw jk utarjlb qk xslvhasvg, okgx ino oad."
text = ""
for letter in string:
    if ord('A')<=ord(letter)<=ord('Z'):
        text += letter
    if ord('a')<=ord(letter)<=ord('z'):
        text += chr(ord(letter)+ord('A')-ord('a'))
print(text)
newtext=""
"""
for i in range (len(text)):
    newtext += chr((ord(text[i])+int(key[i])+ord('A'))%26+ord('A'))
print(newtext)
"""
"""
for columno in range(0, 13):
    sample = []
    tempindex = columno
    while tempindex < len(text):
        sample.append(text[tempindex])
        tempindex += 13
    freq = [0 for j in range(0, 26)]
    for letter in sample:
        freq[ord(letter) - ord('A')] += 1
    freq.sort()
    freq.reverse()
    print(freq)
    plt.bar(range(0, len(freq)), freq)
    plt.title(str(columno))
    # plt.show()
"""
keylength = 13 #userinput

#toss everything and start looking for "Agricola" in the cipher
#find the key ARCANAIMPERII
#figure out it's just baeuforth cipher with the same key as 4b
# xD Laugh hard
#write the decoder:
key='ARCANAIMPERII'
keytable=[ord(char)-ord('A') for char in key]
index = 0
result = ""
for letter in string:
    if ord('a') <= ord(letter) <= ord('z'):
        result += chr((-ord(letter) + ord('a') + keytable[index % 13]) % 26 + ord('a'))
        index += 1
    elif ord('A') <= ord(letter) <= ord('Z'):
        result += chr((-ord(letter) + ord('A') + keytable[index % 13]) % 26 + ord('A'))
        index += 1
    else:
        result += letter
print(result)


