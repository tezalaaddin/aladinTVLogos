import os

# aladinTVLogos dizini altındaki webp formatlı logolar listesi
tv_logos = [
    "24.webp", "a2tv.webp", "ahabertv.webp", "akittv.webp", "aksutv.webp", "altastv.webp", 
    "anadoluajansi.webp", "arastv.webp", "aspor.webp", "astv.webp", "aturk.webp", "atv.webp", 
    "atvalanya.webp", "atvavrupa.webp", "babytv.webp", "beinhaber.webp", "beinsportshd1.webp", 
    "beinsportshd2.webp", "beinsportshd3.webp", "beinsportshd4.webp", "beinsportsmax1.webp", 
    "beinsportsmax2.webp", "benguturk.webp", "berattv.webp", "beyaztv.webp", "bht.webp", 
    "bircsatranc.webp", "birtv.webp", "bizimevtv.webp", "bloomberght.webp", "brt1hd.webp", 
    "brt2.webp", "brt3.webp", "brtv.webp", "bursatv.webp", "cantv.webp", "cartoonnetwork.webp", 
    "caytv.webp", "cekmekoywebtv.webp", "cgrt.webp", "cgtndocumentary.webp", "channelone.webp", 
    "ciftcitv.webp", "cine1.webp", "cine5.webp", "cine6.webp", "cnnturk.webp", "dehatv.webp", 
    "denizpostasitv.webp", "dha.webp", "dimtv.webp", "disneychannel.webp", "disneyjr.webp", 
    "diyanettv.webp", "diyartv.webp", "dosttv.webp", "dreamturk.webp", "ebatv_ilkokul.webp", 
    "ebatv_lise.webp", "ekanal.webp", "ekoltv.webp", "ertv.webp", "erzurumtv.webp", "estv.webp", 
    "etvtv.webp", "eurod.webp", "eurospor1.webp", "eurospor2.webp", "eurostar.webp", "exxen.webp", 
    "fbtv.webp", "finansturk.webp", "finesttv.webp", "flashhaber.webp", "flashtv.webp", "fox.webp", 
    "fx.webp", "genctv.webp", "gstv.webp", "gtv.webp", "gunestv.webp", "gzt.webp", "h8idt8o.webp", 
    "haber360.webp", "haber61.webp", "haberglobal.webp", "haberturk.webp", "halk-tv.webp", 
    "history.webp", "htspor.webp", "hunat.webp", "iceltv.webp", "imamhusseintv.webp", "inattv.webp", 
    "irkfaee.webp", "isimtv.webp", "justinsports.webp", "kanal12.webp", "kanal15.webp", "kanal23.webp", 
    "kanal24.webp", "kanal26.webp", "kanal3.webp", "kanal32.webp", "kanal33.webp", "kanal34.webp", 
    "kanal38.webp", "kanal58.webp", "kanal68.webp", "kanal7-.webp", "kanal7eu.webp", "kanalavrupa.webp", 
    "kanalb.webp", "kanald.webp", "kanaldeuro.webp", "kanaldrama.webp", "kanale.webp", "kanalfirat.webp", 
    "kanalv.webp", "kanalyeni.webp", "kanalz.webp", "kaytv.webp", "kentturk.webp", "konyaolaytv.webp", 
    "kralpoptv.webp", "krt.webp", "krwgu8g.webp", "ktv.webp", "kudustv.webp", "lalegultv.webp", 
    "lifetvhd.webp", "linetv.webp", "logo.webp", "lovenature.webp", "mans.webp", "mavitv.webp", 
    "mctv.webp", "meltemtv.webp", "mercantv.webp", "metropol.webp", "milyontv.webp", "minika-go.webp", 
    "minikacocuk.webp", "moviesmarthd.webp", "mturktv.webp", "myzentv.webp", "natgeo.webp", 
    "natgeowild.webp", "nickelodeon.webp", "nicktoons.webp", "nowtv.webp", "nr1.webp", "nr1ask.webp", 
    "nr1damar.webp", "nr1dance.webp", "nr1turkhd.webp", "ntv.webp", "nurtv.webp", "olayturk.webp", 
    "on4.webp", "on6.webp", "oncu.webp", "ontv.webp", "persianaturkiye.webp", "powerdance.webp", 
    "powerhd.webp", "powerlove.webp", "powerslow.webp", "powerturk.webp", "powerturkakustik.webp", 
    "powerturktaptaze.webp", "rtbaneka.webp", "rtgtv.webp", "sat7turk.webp", "selcuksports.webp", 
    "semerkandtv.webp", "showmaxtr.webp", "showturk.webp", "showtv.webp", "smartspor2.webp", 
    "sozcutv.webp", "sporsmart.webp", "sportstv.webp", "ssport.webp", "startv.webp", "stingraynaturescape.webp", 
    "suntv.webp", "superturk.webp", "szctv.webp", "tabii1.webp", "tabii2.webp", "tabii3.webp", 
    "tabii4.webp", "tabii5.webp", "tabii6.webp", "tabiispor6.webp", "tarihtv.webp", "tarimtv.webp", 
    "tatlisestv.webp", "tbnmtv.webp", "tele1.webp", "tempotv.webp", "teve2.webp", "tgrtbelgesel.webp", 
    "tgrteu.webp", "tgrthaber.webp", "tivi6.webp", "tivibu2.webp", "tivibu3.webp", "tivibu4.webp", 
    "tivibusp1.webp", "tiviturk.webp", "tlc.webp", "tmb.webp", "tontv.webp", "topraktv.webp", 
    "trabzonbb.webp", "trakyturk.webp", "trek.webp", "trt-haber.webp", "trt1.webp", "trt2.webp", 
    "trt3.webp", "trt4k.webp", "trtavaz.webp", "trtbelgesel.webp", "trtcocuk.webp", "trtdiyanetcocuk.webp", 
    "trteba.webp", "trthaber.webp", "trtkurdi.webp", "trtmuzik.webp", "trtspor.webp", "trtspor2.webp", 
    "trtsporyildiz.webp", "trtturk.webp", "trtworld.webp", "turkhaber.webp", "turkmax.webp", 
    "tv-net.webp", "tv1.webp", "tv100.webp", "tv2020.webp", "tv264.webp", "tv360.webp", "tv38.webp", 
    "tv41.webp", "tv422.webp", "tv52.webp", "tv8.webp", "tv85.webp", "tv8int.webp", "tvden.webp", 
    "tvnet.webp", "ulketv.webp", "ulusaltv.webp", "universitetv.webp", "urfanatiktv.webp", 
    "urmiatv.webp", "uutv2.webp", "varsport.webp", "vavtv.webp", "viasatexplore.webp", "vizyon58.webp", 
    "websport.webp", "womantv.webp", "xyzsport.webp"
]

print(f"Toplam yüklenen logo sayısı: {len(tv_logos)}")

# Dosya kontrolü (Codespace'i tetiklemek için)
for logo in tv_logos:
    if os.path.exists(logo):
        pass
