from geopy.geocoders import Nominatim as nt
def obtener_estado(lat, long):
    if lat <= 49 and lat >= 39 and long <= -103 and long >= -125:
        if lat >= 45.5437202453613 and lat <= 49.00244140625 and long >= -124.836097717285 and long <=-116.917427062988:
            return 'Washington'
        elif lat >= 41.9917907714844 and lat <= 46.2991027832031 and long >= -124.703544616699 and long <= -116.463500976562:
            return 'Oregon'
        elif lat >= 41.9880561828613 and lat <= 49.000846862793 and long >= -117.243034362793 and long <= -111.043563842773:
            return 'Idaho'
        elif lat >= 44.3582191467285 and lat <= 49.0011100769043 and long >= -116.050003051758 and long <= -104.039558410645:
            return 'Montana'
        elif lat >= 40.9948768615723 and lat <= 45.0034217834473 and long >= -111.05689239502 and long <= -104.052154541016:
            return 'Wyoming'
        elif lat >= 45.9350357055664 and lat <= 49.0004920959473 and long >= -104.049270629883 and long <= -96.5543899536133:
            return 'North Dakota'
        elif lat >= 42.4798889160156 and lat <= 45.9454536437988 and long >= -104.05770111084 and long <= -96.4363327026367:
            return 'South Dakota'
        elif lat >= 39.9999961853027 and lat <= 43.0017013549805 and long >= -104.053520202637 and long <= -95.3080520629883:
            return 'Nebraska'
        elif lat >= 32.5295219421387 and lat <= 42.0095024108887 and long >= -124.482009887695 and long <= -114.13077545166:
            return 'California'
        elif lat >= 35.0018730163574 and lat <= 42.0022087097168 and long >= -120.005729675293 and long <= -114.039642333984:
            return 'Nevada'
        elif lat >= 36.9979667663574 and lat <= 42.0013885498047 and long >= -114.053932189941 and long <= -109.041069030762:
            return 'Utah'
        elif lat >= 36.9924240112305 and lat <= 41.0023612976074 and long >= -109.060256958008 and long <= -102.041580200195:
            return 'Colorado'
        elif lat >= 36.9930801391602 and lat <= 40.0030975341797 and long >= -102.0517578125 and long <= -94.5882034301758:
            return 'Kansas'
    elif lat <= 39 and lat >= 25 and long <= -103 and long >= -125:
        if lat >= 31.3321762084961 and lat <= 37.0042610168457 and long >= -114.818359375 and long <= -109.045196533203:
            return 'Arizona'
        elif lat >= 32.5295219421387 and lat <= 42.0095024108887 and long >= -124.482009887695 and long <= -114.13077545166:
            return 'California'
        elif lat >= 35.0018730163574 and lat <= 42.0022087097168 and long >= -120.005729675293 and long <= -114.039642333984:
            return 'Nevada'
        elif lat >= 36.9979667663574 and lat <= 42.0013885498047 and long >= -114.053932189941 and long <= -109.041069030762:
            return 'Utah'
        elif lat >= 36.9924240112305 and lat <= 41.0023612976074 and long >= -109.060256958008 and long <= -102.041580200195:
            return 'Colorado'
        elif lat >= 36.9930801391602 and lat <= 40.0030975341797 and long >= -102.0517578125 and long <= -94.5882034301758:
            return 'Kansas'
        elif lat >= 31.3323001861572 and lat <= 37.0001411437988 and long >= -109.050178527832 and long <= -103.000862121582:
            return 'New Mexico'
        elif lat >= 25.8370609283447 and lat <= 36.5007057189941 and long >= -106.645652770996 and long <= -93.5078201293945:
            return 'Texas'
        elif lat >= 33.6191940307617 and lat <= 37.0021362304688 and long >= -103.002571105957 and long <= -94.4312133789062:
            return 'Oklahoma'
    elif lat <= 49 and lat >= 39 and long <= -66 and long >= -103:
        if lat >= 45.9350357055664 and lat <= 49.0004920959473 and long >= -104.049270629883 and long <= -96.5543899536133:
            return 'North Dakota'
        elif lat >= 42.4798889160156 and lat <= 45.9454536437988 and long >= -104.05770111084 and long <= -96.4363327026367:
            return 'South Dakota'
        elif lat >= 39.9999961853027 and lat <= 43.0017013549805 and long >= -104.053520202637 and long <= -95.3080520629883:
            return 'Nebraska'
        elif lat >= 32.5295219421387 and lat <= 42.0095024108887 and long >= -124.482009887695 and long <= -114.13077545166:
            return 'California'
        elif lat >= 36.9924240112305 and lat <= 41.0023612976074 and long >= -109.060256958008 and long <= -102.041580200195:
            return 'Colorado'
        elif lat >= 36.9930801391602 and lat <= 40.0030975341797 and long >= -102.0517578125 and long <= -94.5882034301758:
            return 'Kansas'
        elif lat >= 43.4994277954102 and lat <= 49.3844909667969 and long >= -97.2392654418945 and long <= -89.4833831787109:
            return 'Minnesota'
        elif lat >= 42.491943359375 and lat <= 47.3025016784668 and long >= -92.8881149291992 and long <= -86.2495422363281:
            return 'Wisconsin'
        elif lat >= 40.4773979187012 and lat <= 45.0158615112305 and long >= -79.7625122070312 and long <= -71.8527069091797:
            return 'New York'
        elif lat >= 42.7269325256348 and lat <= 45.0166664123535 and long >= -73.437744140625 and long <= -71.4653549194336:
            return 'Vermont'
        elif lat >= 42.9561233520508 and lat <= 47.4598426818848 and long >= -71.0841751098633 and long <= -66.9250717163086:
            return 'Maine'
        elif lat >= 42.6970405578613 and lat <= 45.3057823181152 and long >= -72.55712890625 and long <= -70.534065246582:
            return 'New Hampshire'
        elif lat >= 41.1863288879395 and lat <= 42.8867149353027 and long >= -73.5081481933594 and long <= -69.8615341186523:
            return 'Massachusetts'
        elif lat >= 40.9667053222656 and lat <= 42.0505905151367 and long >= -73.7277755737305 and long <= -71.7869873046875:
            return 'Connecticut'
        elif lat >= 41.055534362793 and lat <= 42.018856048584 and long >= -71.9070053100586 and long <= -71.1204681396484:
            return 'Rhode Island'
        elif lat >= 40.3755989074707 and lat <= 43.5011367797852 and long >= -96.6397171020508 and long <= -90.1400604248047:
            return 'Iowa'
        elif lat >= 35.9956817626953 and lat <= 40.6136360168457 and long >= -95.7741470336914 and long <= -89.0988388061523:
            return 'Missouri'
        elif lat >= 36.9701309204102 and lat <= 42.5083045959473 and long >= -91.513053894043 and long <= -87.0199203491211:
            return 'Illinois'
        elif lat >= 37.7717399597168 and lat <= 41.7613716125488 and long >= -88.0997085571289 and long <= -84.7845764160156:
            return 'Indiana'
        elif lat >= 38.4031982421875 and lat <= 42.3232383728027 and long >= -84.8203430175781 and long <= -80.5189895629883:
            return 'Ohio'
        elif lat >= 39.7197647094727 and lat <= 42.5146903991699 and long >= -80.5210876464844 and long <= -74.6894989013672:
            return 'Pennsylvania'
        elif lat >= 38.7887535095215 and lat <= 41.3574256896973 and long >= -75.5633926391602 and long <= -73.8850555419922:
            return 'New Jersey'
        elif lat >= 37.8856391906738 and lat <= 39.7229347229004 and long >= -79.4871978759766 and long <= -75.0395584106445:
            return 'Maryland'
        elif lat >= 38.4511260986328 and lat <= 39.8394355773926 and long >= -75.7890472412109 and long <= -74.9846343994141:
            return 'Delaware'
        elif lat >= 37.2014808654785 and lat <= 40.638801574707 and long >= -82.6447448730469 and long <= -77.7190246582031:
            return 'West Virginia'
        elif lat >= 36.4967155456543 and lat <= 39.1474609375 and long >= -89.5715103149414 and long <= -81.9645385742188:
            return 'Kentucky'
        elif lat >= 36.5407867431641 and lat <= 39.4660148620605 and long >= -83.6754150390625 and long <= -75.2312240600586:
            return 'Virginia'
    elif lat <= 39 and lat >= 25 and long <= -66 and long >= -103:
        if lat >= 35.9956817626953 and lat <= 40.6136360168457 and long >= -95.7741470336914 and long <= -89.0988388061523:
            return 'Missouri'
        elif lat >= 36.9701309204102 and lat <= 42.5083045959473 and long >= -91.513053894043 and long <= -87.0199203491211:
            return 'Illinois'
        elif lat >= 37.7717399597168 and lat <= 41.7613716125488 and long >= -88.0997085571289 and long <= -84.7845764160156:
            return 'Indiana'
        elif lat >= 38.4031982421875 and lat <= 42.3232383728027 and long >= -84.8203430175781 and long <= -80.5189895629883:
            return 'Ohio'
        elif lat >= 39.7197647094727 and lat <= 42.5146903991699 and long >= -80.5210876464844 and long <= -74.6894989013672:
            return 'Pennsylvania'
        elif lat >= 38.7887535095215 and lat <= 41.3574256896973 and long >= -75.5633926391602 and long <= -73.8850555419922:
            return 'New Jersey'
        elif lat >= 37.8856391906738 and lat <= 39.7229347229004 and long >= -79.4871978759766 and long <= -75.0395584106445:
            return 'Maryland'
        elif lat >= 38.4511260986328 and lat <= 39.8394355773926 and long >= -75.7890472412109 and long <= -74.9846343994141:
            return 'Delaware'
        elif lat >= 37.2014808654785 and lat <= 40.638801574707 and long >= -82.6447448730469 and long <= -77.7190246582031:
            return 'West Virginia'
        elif lat >= 36.4967155456543 and lat <= 39.1474609375 and long >= -89.5715103149414 and long <= -81.9645385742188:
            return 'Kentucky'
        elif lat >= 36.5407867431641 and lat <= 39.4660148620605 and long >= -83.6754150390625 and long <= -75.2312240600586:
            return 'Virginia'
        elif lat >= 36.9930801391602 and lat <= 40.0030975341797 and long >= -102.0517578125 and long <= -94.5882034301758:
            return 'Kansas'
        elif lat >= 25.8370609283447 and lat <= 36.5007057189941 and long >= -106.645652770996 and long <= -93.5078201293945:
            return 'Texas'
        elif lat >= 33.6191940307617 and lat <= 37.0021362304688 and long >= -103.002571105957 and long <= -94.4312133789062:
            return 'Oklahoma'
        elif lat >= 33.0041046142578 and lat <= 36.4996032714844 and long >= -94.6178131103516 and long <= -89.6422424316406:
            return 'Arkansas'
        elif lat >= 34.9829788208008 and lat <= 36.6781196594238 and long >= -90.310302734375 and long <= -81.6468963623047:
            return 'Tennessee'
        elif lat >= 33.7528762817383 and lat <= 36.5880393981934 and long >= -84.3218765258789 and long <= -75.4001159667969:
            return 'North Carolina'
        elif lat >= 28.9210300445557 and lat <= 33.019458770752 and long >= -94.0431518554688 and long <= -88.817008972168:
            return 'Louisiana'
        elif lat >= 30.1477890014648 and lat <= 34.9960556030273 and long >= -91.6550140380859 and long <= -88.0980072021484:
            return 'Mississippi'
        elif lat >= 30.1375217437744 and lat <= 35.0080299377441 and long >= -88.4731369018555 and long <= -84.8882446289062:
            return 'Alabama'
        elif lat >= 32.0333099365234 and lat <= 35.2155418395996 and long >= -83.35400390625 and long <= -78.4992980957031:
            return 'South Carolina'
        elif lat >= 30.3557567596436 and lat <= 35.0008316040039 and long >= -85.6051712036133 and long <= -80.7514266967773:
            return 'Georgia'
        elif lat >= 24.3963069915771 and lat <= 31.0009689331055 and long >= -87.6349029541016 and long <= -79.9743041992188:
            return 'Florida'
    elif lat >= 52.469971 and lat <= 71.699910 and long >= -165.982207 and long <= -141.147125:
            return 'Alaska'
    elif lat >= 18.714689 and lat <= 22.348588 and long >= -160.515854 and long <= -154.665708:
            return 'Hawaii'



geolocator = nt()
location = geolocator.reverse("40, -82")
print(location.address)
location = geolocator.reverse("40.5, -86")
print(location.address)
location = geolocator.reverse("37.575939, -97.701630")
print(location.address)
location = geolocator.reverse("27.330475, -98.185307")
print(location.address)


print(obtener_estado(40, -82))
print(obtener_estado(40.5, -86))
print(obtener_estado(37.575939, -97.701630))
print(obtener_estado(27.330475, -98.185307))