import logging

from aiogram import Bot, Dispatcher, executor, types
from button_inline_keyboard import *

API_TOKEN = ''

logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.reply("Rayonni tanlang😉",reply_markup=Regions)



@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

@dp.callback_query_handler(text="yunusabad")
async def echo(call: types.CallbackQuery):
    await call.message.answer("🏙Yunusoboddagi mehmonhonalar" ,reply_markup=Hotels)

@dp.callback_query_handler(text="chilonzor")
async def echo(call: types.CallbackQuery):
    await call.message.answer("🏙Chilonzordagi mehmonhonalar",reply_markup=chilonzorz_hotels)


@dp.callback_query_handler(text="yakkasaroy")
async def echo(call: types.CallbackQuery):
    await call.message.answer("🏙Yakkasaroydagi  mehmonhonalar" ,reply_markup=yakkasaroys_hotels)


@dp.callback_query_handler(text="bektemir")
async def echo(call: types.CallbackQuery):
    await call.message.answer("🏙Bektemirdagi  mehmonhonalar",reply_markup=bektemirs_hotels)


@dp.callback_query_handler(text="mirzo")
async def echo(call: types.CallbackQuery):
    await call.message.answer("🏙Mirzo-Ulugbekdagi  mehmonhonalar",reply_markup=mirzo_ulugbek_hotels)


@dp.callback_query_handler(text="mirobod")
async def echo(call: types.CallbackQuery):
    await call.message.answer("🏙Miroboddagi  mehmonhonalar",reply_markup=mirobod_hotels)



@dp.callback_query_handler(text="olmazor")
async def echo(call: types.CallbackQuery):
    await call.message.answer("🏙Olmazordagi  mehmonhonalar",reply_markup=olmazor_menu)



@dp.callback_query_handler(text="sergeli")
async def echo(call: types.CallbackQuery):
    await call.message.answer("🏙Sergelidagi mehmonhonalar",reply_markup=sergeli_menu)



@dp.callback_query_handler(text="shayhontohur")
async def echo(call: types.CallbackQuery):
    await call.message.answer("🏙Shayhontohurdagi mehmonhonalar",reply_markup=shayxontohur_menu)


@dp.callback_query_handler(text="uchtepa")
async def echo(call: types.CallbackQuery):
    await call.message.answer("🏙Uchtepadagi mehmonhonalar",reply_markup=uchtepa_menu)



@dp.callback_query_handler(text="yashnabod")
async def echo(call: types.CallbackQuery):
    await call.message.answer("🏙Yashnaboddagi mehmonhonalar",reply_markup=yashnobod_menu)


@dp.callback_query_handler(text="hayot")
async def echo(call: types.CallbackQuery):
    await call.message.answer("🏙Yangihayotdagi mehmonhonalar",reply_markup=yangihayot_menu)

# YUNUSABAD'S HOTELS :



@dp.callback_query_handler(text="uzbekistan")   
async def region(call: types.CallbackQuery):
    await call.message.answer_photo("https://content.r9cdn.net/rimg/himg/66/f7/b2/expediav2-2626-b99482-810144.jpg?width=226&height=200&xhint=540&yhint=332&crop=true&watermarkheight=14&watermarkpadding=5" , caption="""
Адрес: 45, ул. Мусаханова 100047,  г. Ташкент
До аэропорта:  10 км
До ж/д вокзала: 7 км
До центра города: в центре города
До ближайшей станции метро: 0,2 км – м. «Амир Темур» / «Юнус Раджабий»
Ближайшие достопримечательности: Сквер Амира Темура,
Музей Амира Темура, Дворец международных форумов, Куранты
    
    
     """ , reply_markup=Orqaga_hotels, )
    await call.message.answer_location(41.311624418366605, 69.28265768839725)
    await call.answer("Yunusoboddagi mehmon honalar" ,)



@dp.callback_query_handler(text="orqaga")
async def orqaga(call: types.CallbackQuery):
    await call.message.answer("orqga qayttingiz", reply_markup=Regions)




@dp.callback_query_handler(text="gostina")
async def region(call: types.CallbackQuery):
    await call.message.answer_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNq9G7INSZbvWnlK-ZdaLIHwNKGm4hnRFSMiQNmzvVI8eW54wcmMPvEvPaqQTIBkkMDM8&usqp=CAU", caption="""
Адрес: Улица Чинабад 61А, 100039 Ташкент, Узбекистан 
До аэропорта:  11 км
До ж/д вокзала: 3 км
До центра города: 3,5км
До ближайшей станции метро: 0,5 км – м. «Шахристан»
Ближайшие достопримечательности: Санатория Чинабад
Телебашня,Центр плова «Beshqozon»,Теннисный корт.
""" ,reply_markup=Orqaga_hotels)
    await call.message.answer_location(41.35571253087879, 69.30222045155489)
    await call.answer("Yunusoboddagi mehmon honalar")

@dp.callback_query_handler(text="orqagaa")
async def orqaga(call: types.CallbackQuery):
    await call.message.answer('🏙Yunusaboddagi mehmon honalar', reply_markup=Hotels)


@dp.callback_query_handler(text="orqagaaa")
async def orqaga(call: types.CallbackQuery):
    await call.message.answer('🏙Chilonzordagi mehmon honalar', reply_markup=chilonzorz_hotels)


@dp.callback_query_handler(text="internetion")
async def region(call: types.CallbackQuery):
    await call.message.answer_photo("https://media-cdn.tripadvisor.com/media/photo-s/09/50/64/f5/international-hotel-tashkent.jpg", caption="""
Отель International Tashkent находится в центральной парковой зоне. Прогулка до выставочного центра Ташкента и Международного бизнес-центра занимает 10 минут. На территории обустроена бесплатная частная парковка.
""" , reply_markup=Orqaga_hotels)
    await call.message.answer_location(41.35571253087879, 69.30222045155489)
    await call.answer("Yunusoboddagi mehmon honalar")



@dp.callback_query_handler(text="place")
async def region(call: types.CallbackQuery):
    await call.message.answer_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQg63OEbarLp1gLMktyRknYI_0W6qMPAk_SpyGMiO4-XvWe_Pxgg_J02UliJFJaqJ1CIVo&usqp=CAU", caption="""
Юридическое название: CITY PALACE ООО

Брендовое название: CITY PALACE ГОСТИНИЦА

Адрес: Узбекистан, 100000, ТАШКЕНТ, ЮНУСАБАДСКИЙ район, просп. АМИРА ТЕМУРА, 15

Ориентиры: рынок "АЛАЙСКИЙ", гостиница "WYNDHAM" (бывш. гостиница "ДЕДЕМАН")
""" , reply_markup=Orqaga_hotels)
    await call.message.answer_location(41.31631141433502, 69.27981640723873)
    await call.answer("Yunusoboddagi mehmon honalar")


@dp.callback_query_handler(text="grand")
async def region(call: types.CallbackQuery):
    await call.message.answer_photo("https://www.grandcapitalhotel.uz/ru/wp-content/uploads/sites/2/2018/09/photo_fasad_26.jpg", caption="""
Юридическое название: PROGRESS STILL ООО

Брендовое название: GRAND CAPITAL HOTEL ГОСТИНИЦА

Адрес: Узбекистан, 100000, ТАШКЕНТ, ЮНУСАБАДСКИЙ район, ул. ШАРАФОБОД, 2

Ориентиры: ст.м. "МИНОР"
""" , reply_markup=Orqaga_hotels)
    await call.message.answer_location(41.32526854117656, 69.28753201179111)
    await call.answer("Yunusoboddagi mehmon honalar")



# CHILONZOR MEHMONHONALAR:


@dp.callback_query_handler(text="dimond")
async def region(call: types.CallbackQuery):
    await call.message.answer_photo("https://cf.bstatic.com/xdata/images/hotel/max1024x768/205269062.jpg?k=5a3d68e88c76e2d194c50ca76bc08d0328a77e1ed3acceb5c53608caa499514e&o=&hp=1", caption="""
Юридическое название: PROGRESS STILL ООО

Брендовое название: GRAND CAPITAL HOTEL ГОСТИНИЦА

Адрес: Узбекистан, 100000, ТАШКЕНТ, ЮНУСАБАДСКИЙ район, ул. ШАРАФОБОД, 2

Ориентиры: ст.м. "МИНОР"
""" , reply_markup=Orqaga_hotels_1)
    await call.message.answer_location(41.32526854117656, 69.28753201179111)
    await call.answer("Chilonzordagi mehmonhonalar")





@dp.callback_query_handler(text="dubay")
async def region(call: types.CallbackQuery):
    await call.message.answer_photo("https://komandirovka.ru/upload/save_file49/77c/77c89efaef6994100b033bc515f60430.jpg", caption="""
Юридическое название: DUBAY GROUP ООО

Брендовое название: DUBAY ГОСТИНИЦА

Адрес: Узбекистан, ТАШКЕНТ, ЧИЛАНЗАРСКИЙ район, ул. ДИЙДОР, 71 А

Ориентиры: завод "АЛГОРИТМ"
""" , reply_markup=Orqaga_hotels_1)
    await call.message.answer_location(41.259363195100754, 69.16260577889415)
    await call.answer("Chilonzordagi mehmonhonalar")



@dp.callback_query_handler(text="atlas")
async def region(call: types.CallbackQuery):
    await call.message.answer_photo("https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0f/c7/c6/ea/grand-atlas-hotel.jpg?w=700&h=-1&s=1", caption="""
Юридическое название: GRAND ATLAS ООО

Брендовое название: GRAND ATLAS HOTEL ГОСТИНИЦА

Адрес: Узбекистан, 100081, ТАШКЕНТ, ЧИЛАНЗАРСКИЙ район, ул. ДОМБРАБАД, 182

Ориентиры: бывш. гор. больница №16
""" , reply_markup=Orqaga_hotels_1)
    await call.message.answer_location(41.257654079931854,  69.20396984247452)
    await call.answer("Chilonzordagi mehmonhonalar")







@dp.callback_query_handler(text="hilal")
async def region(call: types.CallbackQuery):
    await call.message.answer_photo("https://dynamic-media-cdn.tripadvisor.com/media/photo-o/18/48/7f/54/caption.jpg?w=600&h=-1&s=1", caption="""
Юридическое название: CITIZEN TRAVEL ООО

Брендовое название: HILAL HOTEL TASHKENT ГОСТИНИЦА

Адрес: Узбекистан, 100113, ТАШКЕНТ, ЧИЛАНЗАРСКИЙ район, м-в ЧИЛАНЗАР-Ц, ул. КАТАРТАЛ, 28

Ориентиры: торговый комплекс "МЕДИА ПАРК"
""" , reply_markup=Orqaga_hotels_1)
    await call.message.answer_location(41.28182925775529,  69.20217316760935    )
    await call.answer("Chilonzordagi mehmonhonalar")


@dp.callback_query_handler(text="lios")
async def region(call: types.CallbackQuery):
    await call.message.answer_photo("https://www.goldenpages.uz/bek/1400909-16/hotelios7.jpg", caption="""
Юридическое название: BOOKING SYSTEM ООО

Брендовое название: HOTELIOS

Адрес: Узбекистан, 100115, ТАШКЕНТ, ЧИЛАНЗАРСКИЙ район, ул. ГАГАРИНА, 66

Ориентиры: школа №103
""" , reply_markup=Orqaga_hotels_1)
    await call.message.answer_location(41.28182925775529,  69.20217316760935    )
    await call.answer("Chilonzordagi mehmonhonalar")




# Yakkasaroy hotels:


@dp.callback_query_handler(text="orqagaaaa")
async def orqaga(call: types.CallbackQuery):
    await call.message.answer("orqga qayttingiz", reply_markup=yakkasaroys_hotels)

@dp.callback_query_handler(text="panarama")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Panarams Hotel Tashkent""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/85", caption="""Radisson Individuals dasturida ishtirok etuvchi Panarams Tashkent – ​​Toshkent shahrida joylashgan 4 yulduzli mehmonxona. U teras, restoran, bar, umumiy dam olish xonasi, bepul Wi-Fi va xususiy hammom bilan jihozlangan konditsioner xonalar taklif etadi. Mehmonlar yopiq basseyn, fitness markazi va saunaga ega spa va sog'lomlashtirish markazidan foydalanishlari mumkin. Bepul velosiped ijarasi taqdim etiladi.Standart qulayliklar qatoriga seyf va tekis ekranli televizor kiradi. Panarams Tashkentning barcha xonalarida sochiq va choyshablar mavjud.Eng yaqin aeroport - Islom Karimov nomidagi Toshkent xalqaro aeroporti, Panarams Tashkent mehmonxonasidan 8 km uzoqlikda. Mehmonxona aeroportga bepul transport xizmatini taklif qiladi.""" , reply_markup=Orqaga_hotels_2)
    await call.message.answer_location(41.310757348708066, 69.31310642561571)



@dp.callback_query_handler(text="best")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""BEST GUESTHOUSE""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/86", caption="""BEST mehmon uyi Toshkent shahrida joylashgan. Saytda teras mavjud. Qabulxona 24/7 ishlaydi. Mehmonxonada umumiy oshxona mavjud. Mehmonlar valyuta ayirboshlash va xona xizmatidan foydalanishlari mumkin.Mehmonxonaning barcha xonalari shkaf va tekis ekranli televizor bilan jihozlangan. BEST Guesthouse mehmonxonasining har bir xonasi konditsioner va stol bilan jihozlangan.Islom Karimov Toshkent xalqaro aeroporti 5 km uzoqlikda joylashgan. Qo'shimcha haq evaziga aeroportga xizmat ko'rsatish mumkin.""" , reply_markup=Orqaga_hotels_2) 
    await call.message.answer_location(41.300787411688034, 69.25518631212502)



@dp.callback_query_handler(text="sevinch")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Sevinch Hotel""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/87", caption="""“Sevinch” mehmonxonasi Oqtepa shahrida joylashgan. Bog', restoran va butun bo'ylab bepul Wi-Fi mavjud. Qabulxona 24/7 ishlaydi. Shuningdek, valyuta ayirboshlash shoxobchasi ham mavjud.Konditsionerli xonalar kabel kanallari bilan tekis ekranli televizor, ish stoli, mikroto'lqinli pech, choynak, shuningdek dush va bepul hojatxona jihozlari bilan jihozlangan. Maxsus hammom hammom, fen va shippak bilan jihozlangan. Sochiq va choyshab bilan ta'minlangan.Sevinch mehmonxonasida alakart yoki halol nonushta taklif etiladi.Islom Karimov Toshkent xalqaro aeroporti 5 km uzoqlikda joylashgan.""" , reply_markup=Orqaga_hotels_2)
    await call.message.answer_location(41.28085508519233, 69.27032765259442)


@dp.callback_query_handler(text="grand")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Orient Grand Hotel""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/88", caption="""Orient Grand mehmonxonasi Toshkent shahrida joylashgan. Mehmonxonada bankomat va restoran mavjud. Qabulxona 24/7 ishlaydi. So'rov bo'yicha aeroport transferlari va xona xizmati mavjud. Bepul Wi-Fi mavjud.Bu dush va bepul hojatxonalar bilan jihozlangan xususiy hammom, tekis ekranli televizor va konditsionerga ega. Ba'zi xonalarda yashash maydoni mavjud. Barcha xonalarda shkaf va choynak mavjud.Orient Grand mehmonxonasi mehmonlari bufet yoki kontinental nonushtadan bahramand bo'lishlari mumkin.Islom Karimov Toshkent xalqaro aeroporti 4 km masofada joylashgan.""" , reply_markup=Orqaga_hotels_2)
    await call.message.answer_location(41.28729760096161, 69.24349114096098)


@dp.callback_query_handler(text="demure")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Demure Hotel""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/89", caption="""Demure inn Toshkentda joylashgan bo'lib, bog' va terastaga ega. U 24 soatlik resepsiyon va bagajni saqlashni taklif etadi. Xona xizmati mavjud.Barcha xonalar konditsioner va sun'iy yo'ldosh kanallari bilan tekis ekranli televizor bilan jihozlangan. Choynak, dush, fen va ish stoli ham mavjud. Barcha xonalarda shkaf mavjud.Mehmonlar ertalab bufet, osiyo yoki halol nonushtani tanlashlari mumkin.Islom Karimov nomidagi Toshkent xalqaro aeroporti mehmonxonadan 9 km uzoqlikda joylashgan.""" , reply_markup=Orqaga_hotels_2)
    await call.message.answer_location(41.28103476006766, 69.24179186979721)




# Bektemir_hotels_menu :


@dp.callback_query_handler(text="orqagaaaaa")
async def orqaga(call: types.CallbackQuery):
    await call.message.answer("orqga qayttingiz", reply_markup=bektemirs_hotels)




@dp.callback_query_handler(text="diyora")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Diyora Hostel""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/25", caption="""Bog'ga ega Diyora Hostel Qŭyliqda joylashgan.Yotoqxonada xonalar stol bilan jihozlangan. Diyora Hostelda har bir xonada umumiy hammom va choyshab mavjud.Eng yaqin aeroport Islom Karimov nomidagi Toshkent xalqaro aeroporti, turar joydan 4 km uzoqlikda joylashgan.""" ,reply_markup=Orqaga_hotels_3)
    await call.message.answer_location(41.26061485667236, 69.34528594371623)




@dp.callback_query_handler(text="resident")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""RESIDENT HOTEL" MEHMONXONASI""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/22", caption="""RESIDENT HOTEL" MEHMONXONASI - Toshkent, O'zbekiston xaritadasida tashkilotning joylashuvi iloji boricha aniq ko'rsatilgan, xato 100 metrdan oshmaydi. Yaqin atrofda bir nechta tashkilotlar joylashgan: eng yaqin mo'ljal: "THE ROYAL MEZBON" MEHMONXONASI (0.03 km), shuningdek "SALON EXCLUSIVE" MEBEL SALONI (0.11 km) va USMON IBN MAZUN MASJIDI (0.14 km).""" , reply_markup=Orqaga_hotels_3)
    await call.message.answer_location(41.267596241535834, 69.24831748875009)




@dp.callback_query_handler(text="shosh")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Hotel shosh palace""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/27", caption="""Shosh saroyida Genius chegirmasini olishingiz mumkin! Bu mulkni tejash uchun hisobingizga kiring.Shosh Palace mehmonxonasi Toshkent shahrida joylashgan. Unda mavsumiy ochiq basseyn, bog' va mehmonxona bo'ylab bepul Wi-Fi mavjud. Mulk bepul shaxsiy avtoturargoh va frantsuz restoranini taklif etadi.""" ,reply_markup=Orqaga_hotels_3)
    await call.message.answer_location(41.293241611413286, 69.26637960551875)



@dp.callback_query_handler(text="hayot")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Hayot hostel""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/29", caption="""Hayot hosteli Toshkent shahrida, shahar markazi va vokzaldan 7 km uzoqlikda joylashgan. Bu bepul Wi-Fi va bepul mashinalar bilan jihozlangan konditsionerli xonalarni taklif etadi.Har bir xonada kabel kanallari bo'lgan televizor mavjud. Hayot hostelidagi boshqa imkoniyatlarga umumiy hammom, umumiy oshxona va ovqatlanish joyi kiradi.“Hayot” mehmonxonasida restoran joylashgan bo‘lib, u yotoqxonadan 50 metr uzoqlikda joylashgan hamkor dastur hisoblanadi.Xostelda 24 soat xizmat ko'rsatadigan resepsiyon va bagaj saqlash joyi mavjud.Toshkent xalqaro aeroporti 3 km uzoqlikda; qo'shimcha haq evaziga transport xizmati mavjud.""" , reply_markup=Orqaga_hotels_3)
    await call.message.answer_location(41.24568822767874, 69.3148638752002)



@dp.callback_query_handler(text="ayva")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Ayva hotel""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/30", caption="""“Ayva” mehmonxonasi sizga Toshkentdagi eng qulay va keng mehmon xonalarini, shuningdek, turli turdagi biznes uchrashuvlarini o‘tkazish, tadbirlarni tashkil etish va mehmonxonada mehmonlarni joylashtirish uchun barcha qulayliklarni taklif etadi. Mehmonxona aeroportdan 15 daqiqa, temir yo'l vokzalidan esa 10 daqiqalik masofada joylashgan...""" , reply_markup=Orqaga_hotels_3)
    await call.message.answer_location(41.247951518403205, 69.30681983760024)






# MIRZO - ULUGBEK'S HOTELS :


@dp.callback_query_handler(text="orqagaaaaaa")
async def orqaga(call: types.CallbackQuery):
    await call.message.answer("orqga qayttingiz", reply_markup=mirzo_ulugbek_hotels)








@dp.callback_query_handler(text="sofia")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Sofiya Hotel Tashkent""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/52", caption="""Sofiya Tashkent” mehmonxonasi Toshkentning shimoliy-sharqiy qismida joylashgan. U bog ', bepul Wi-Fi va bepul shaxsiy avtoturargohni taklif etadi. Kechqurun ko'ngilochar dastur mavjud.Konditsionerli xonalar sun'iy yo'ldosh televideniesi va choy-qahva tayyorlash uchun jihozlar bilan jihozlangan. Hammomlarda fen va shippak mavjud.""" , reply_markup=Orqaga_hotels_4) 
    await call.message.answer_location(41.314936471009666, 69.33180722200163)




@dp.callback_query_handler(text="kamal")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Kamal Hotel""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/53", caption="""KAMAL mehmonxonasi Toshkent shahrida joylashgan. U konditsionerli xonalarni taklif etadi. Ushbu 1 yulduzli mehmonxonada 24 soat xizmat ko'rsatish bo'limi mavjud. Xona xizmati so'rov bo'yicha mavjud. Xohlovchilar oilaviy xonalarni bron qilishlari mumkin.Islom Karimov nomidagi Toshkent xalqaro aeroporti mehmonxonadan 12 km uzoqlikda joylashgan.""" , reply_markup=Orqaga_hotels_4)
    await call.message.answer_location(41.3343211275041, 69.34876044045248)





@dp.callback_query_handler(text="top")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""The Top Hostel""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/54", caption="""Bog' va barbekyu jihozlari bilan jihozlangan The Top Hostel Toshkentda joylashgan. Qabulxona 24/7 ishlaydi. Imkoniyatlar umumiy oshxona va butun bo'ylab bepul Wi-Fi o'z ichiga oladi. Mehmonxona aeroportdan va aeroportgacha transport xizmatini taklif qiladi.Siz yotoqxonada stol tennisi o'ynashingiz mumkin. Bu hudud piyoda sayr qilish uchun mashhur.Eng yaqin aeroport - Islom Karimov nomidagi Toshkent xalqaro aeroporti, The Top Hosteldan 10 km uzoqlikda.""" ,reply_markup=Orqaga_hotels_4)
    await call.message.answer_location(41.326072968023816, 69.31995271289001)




@dp.callback_query_handler(text="asli")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Asli Makon Hotel""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/55", caption="""Toshkentda joylashgan Asli Makon mehmonxonasida bar mavjud. Qabulxona 24/7 ishlaydi. Mehmonlar restoranga tashrif buyurishlari yoki ovqat va ichimliklar uchun xona xizmatiga buyurtma berishlari mumkin. Bepul Wi-Fi mavjud. Binoda bankomat mavjud. Konsyerj va valyuta ayirboshlash xizmatlari ko'rsatiladi.Konditsionerli xonalar shkaf, choynak, minibar, seyf, tekis ekranli televizor va dushli xususiy hammom bilan jihozlangan.Har kuni ertalab alakart va halol variantlari bilan birga bufet nonushtasi taqdim etiladi""" ,reply_markup=Orqaga_hotels_4)
    await call.message.answer_location(41.32795987916482, 69.3441490256166)




@dp.callback_query_handler(text="national")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""National Hostel""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/58", caption="""Milliy hostel Toshkent shahrida joylashgan bo'lib, umumiy dam olish xonasiga ega. Xonalar dush va fen bilan jihozlangan umumiy hammom bilan jihozlangan, yotoqxonaning ba'zi xonalarida esa teras mavjud.""")
    await call.message.answer_location(41.31655026910663, 69.30219516794274)







# MIROBOT HOTELS :

@dp.callback_query_handler(text="orqagaaaaaaa")
async def orqaga(call: types.CallbackQuery):
    await call.message.answer("orqga qayttingiz", reply_markup=mirobod_hotels)




@dp.callback_query_handler(text="uzbekistan1")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Uzbekistan Hotel""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/42", caption="""Ushbu mehmonxona Toshkent markazidagi Amir Temur maydonidan atigi 100 metr uzoqlikda joylashgan. U sport zali, sauna va tekis ekranli televizor bilan jihozlangan konditsionerli xonalarni taklif etadi. Bepul avtoturargoh mavjud va hududda ajoyib transport aloqalari mavjud.Hotel Uzbekistan klassik tarzda jihozlangan xonalar va minibar bilan jihozlangan suitlarni taklif etadi. Ichki makonlar quyuq yog'och mebellar va oqlangan matolar bilan bezatilgan. Har bir hammomda sochlarini fen mashinasi mavjud.""" , reply_markup=Orqaga_hotels_5)
    await call.message.answer_location(41.312775185856125, 69.28319232855132)






@dp.callback_query_handler(text="comfort")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Comfort Hotel""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/43", caption="""Comfort Hotel Tashkent mehmonxonasi Toshkent shahrida joylashgan bo'lib, bog'ga ega. Teras va bepul shaxsiy avtoturargohni taklif etadi. Bepul Wi-Fi mavjud.Mehmonxonaning barcha xonalari tekis ekranli televizor bilan jihozlangan. Bundan tashqari, oshxona mavjud. Maxsus hammom dush va fen bilan jihozlangan. Comfort Tashkent mehmonxonasining barcha xonalari konditsioner bilan jihozlangan. Mehmonlar umumiy hammomdan foydalanishlari mumkin.""" , reply_markup=Orqaga_hotels_5)
    await call.message.answer_location(41.2850330717665, 69.26046085666972)


@dp.callback_query_handler(text="gallery")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Gallery Hotel""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/46", caption="""Gallery Hostel Toshkent shahrida joylashgan. Unda bog' va umumiy dam olish xonasi mavjud. Saytda bepul shaxsiy avtoturargoh mavjud. Qo'shimcha haq evaziga aeroportga xizmat ko'rsatish mumkin.Har kuni ertalab bufet, kontinental va halol nonushta variantlari mavjud.24 soatlik resepsiyon xodimlari ingliz, fors, yapon va rus tillarida gaplashadi.""" ,reply_markup=Orqaga_hotels_5)
    await call.message.answer_location(41.29140263528017, 69.26640882747098)







@dp.callback_query_handler(text="safarova")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Safarova Hostel""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/47", caption="""Safarovning oilaviy yotoqxonasi Toshkent shahrida joylashgan. Unda umumiy dam olish xonasi, teras, bar va butun mulk bo'ylab bepul Wi-Fi mavjud. Aeroportga transport xizmati taqdim etiladi. Velosiped ijarasi do'koni mavjud.Ba'zi xonalarda muzlatgich, mikroto'lqinli pech va minibar bilan jihozlangan oshxona mavjud.Hostel mehmonlari kontinental nonushta qilishlari mumkin.Siz Safarov's Family Hostelda dart o'ynashingiz mumkin. Hudud piyoda yurish va velosipedda sayr qilish uchun mashhur.""" , reply_markup=Orqaga_hotels_5)
    await call.message.answer_location(41.35552071392737, 69.38468055087985)    




@dp.callback_query_handler(text="blue")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""BLUE SKY HOTEL""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/51", caption="""Qo‘shqo‘rg‘onda joylashgan Bluesky bog‘ va umumiy dam olish maskaniga ega. Bepul shaxsiy avtoturargoh mavjud va mehmonxona pullik aeroport xizmatini taklif qiladi.Mehmonxona mehmonlari Osiyo nonushtasidan bahramand bo'lishlari mumkin.Ingliz, fors va rus tillarida so'zlashadigan xodimlar bilan resepsiyonda kechayu kunduz ma'lumotlar mavjud.Eng yaqin aeroport - Islom Karimov nomidagi Toshkent xalqaro aeroporti, Bluesky dan 3 km uzoqlikda.""" , reply_markup=Orqaga_hotels_5)
    await call.message.answer_location(41.27874598629179, 69.28532277041573)













# Olmazor hotels :

@dp.callback_query_handler(text="orqagaaaaaaaa")
async def orqaga(call: types.CallbackQuery):
    await call.message.answer("orqga qayttingiz", reply_markup=olmazor_menu)

@dp.callback_query_handler(text="budget")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Budget Hostel""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/59", caption="""Budget Hostelda Toshkentda bar, umumiy dam olish xonasi, bog' va teras mavjud. U 24 soatlik resepsiyon va umumiy oshxonani taklif etadi.Yotoqxonadagi barcha xonalar choynak bilan jihozlangan. Budjet yotoqxonasidagi xonalar konditsioner va stol bilan jihozlangan.Mehmonlar kontinental nonushta qilishlari mumkin.Qum Budget Hosteldan 18 km uzoqlikda joylashgan. Toshkent xalqaro aeroporti 11 km uzoqlikda joylashgan. Qo'shimcha haq evaziga aeroportga xizmat ko'rsatish mumkin.""" , reply_markup=Orqaga_hotels_6)
    await call.message.answer_location(41.34754397505469, 69.21446414282036)





@dp.callback_query_handler(text="ok")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Hotel OK""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/59", caption="""OK mehmonxonasi Toshkent shahrida joylashgan. U 24 soatlik resepsiyon, butun mulk bo'ylab bepul Wi-Fi va xona xizmatini taklif etadi. Mehmonxona shahar manzarasida.Barcha xonalarda choynak bor. OK mehmonxonasining konditsionerli xonalari tekis ekranli televizor bilan jihozlangan.Islom Karimov nomidagi Toshkent xalqaro aeroporti 15 km masofada joylashgan.""", reply_markup=Orqaga_hotels_6)
    await call.message.answer_location(41.36318471158257, 69.18425119476674)


@dp.callback_query_handler(text="ponit")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""HostelPoint""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/61", caption="""HostelPoint Toshkent shahrida joylashgan. U konditsionerli xonalarni taklif etadi. Boshqa imkoniyatlarga umumiy oshxona, umumiy dam olish xonasi va butun mulk bo'ylab bepul Wi-Fi kiradi. Qabulxona 24/7 ishlaydi. Mehmonlar konsyerj xizmatlaridan va bagajni saqlashdan foydalanishlari mumkin.Barcha xonalarda choyshablar mavjud.Islom Karimov nomidagi Toshkent xalqaro aeroporti 11 km.""" ,reply_markup=Orqaga_hotels_6)
    await call.message.answer_location(41.34603886144716, 69.27723408143446)




@dp.callback_query_handler(text="paradise")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""PARADISE HOSTEL""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/62", caption="""Toshkentda joylashgan Paradise Inn Hostel bog'ga ega. Imkoniyatlarga konsyerj xizmatlari, bolalar o'yin maydonchasi, umumiy dam olish xonasi va 24 soatlik resepsiyon kiradi. Mehmonxona transport xizmatlari va butun bo'ylab bepul Wi-Fi taklif qiladi.Konditsionerli xonalar dush kabinasi, ish stoli, mikroto'lqinli pech, muzlatgich, choynak va fen bilan jihozlangan. Yotoqxona xonalarida sochiq va choyshablar mavjud.Paradise inn'da siz mashina ijaraga olishingiz yoki hududda piyoda yurishingiz mumkin.""" , reply_markup=Orqaga_hotels_6)
    await call.message.answer_location(41.31881368667223, 69.2749099660866)


@dp.callback_query_handler(text="maskan")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""MASKAN HOTEL""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/22", caption="""Oqtepa-Chig'atoyda joylashgan MASKAN HOTEL bog'i, terasi va restoraniga ega 4 yulduzli turar joyni taklif etadi. Ushbu 4 yulduzli mehmonxona xona xizmati va 24 soatlik resepsiyonni taklif etadi. Mehmonxonada oilaviy xonalar mavjud.Ushbu 4 yulduzli mehmonxonada stol tennisi o'ynashingiz mumkin.Eng yaqin aeroport Islom Karimov nomidagi Toshkent xalqaro aeroporti, mehmonxonadan 10 km uzoqlikda joylashgan.""" , reply_markup=Orqaga_hotels_6)
    await call.message.answer_location(41.345897089137395, 69.20969199863723)



# SERGELI HOTELS :


@dp.callback_query_handler(text="orqagaaaaaaaaa")
async def orqaga(call: types.CallbackQuery):
    await call.message.answer("orqga qayttingiz", reply_markup=sergeli_menu)



@dp.callback_query_handler(text="empire")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Hotel Empire""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/64", caption="""U juda qulay joyda, katta ko'chaning yonida joylashgan, ammo ikkinchi qatorda, bu tufayli shovqinli emas. Booking.com orqali ikki kishilik xonani bron qildik. Biroq, xonada faqat bitta karavot borligi va u unchalik keng emasligi ma'lum bo'ldi.""" , reply_markup=Orqaga_hotels_7)
    await call.message.answer_location(41.282423848242196, 69.2620963366734)




@dp.callback_query_handler(text="sulaymon")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Sulaymon hotel""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/65", caption="""Sulaymon mehmon uyi Toshkent shahridagi konditsionerli turar joylarga ega.Mehmonxonada xonalar shkaf, tekis ekranli televizor, xususiy hammom, choyshab va sochiqlar bilan jihozlangan.Mehmonxonada har kuni ertalab alakart, osiyo yoki vegetarian nonushtasi mavjud."""  ,reply_markup=Orqaga_hotels_7) 
    await call.message.answer_location(41.216044976716475, 69.21622299677412)




@dp.callback_query_handler(text="hill")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Daniel HillI""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/66", caption="""Daniel Hill mehmonxonasi Toshkent shahrida joylashgan. Mehmonlar umumiy dam olish xonasi, teras, bar va suv sporti inshootlaridan foydalanishlari mumkin.""" , reply_markup=Orqaga_hotels_7)
    await call.message.answer_location(41.2530688592442, 69.30563149491982)




@dp.callback_query_handler(text="atlan")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Atlantis Hotel""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/68", caption="""Atlantis mehmonxonasi Toshkent shahrida joylashgan. Mulk umumiy dam olish xonasi, suv parki va mavsumiy ochiq basseynni, shuningdek, bepul shaxsiy avtoturargohni taklif etadi. Bepul Wi-Fi mavjud.Mehmonxonadagi konditsionerli xonalar tekis ekranli televizor, ish stoli va seyf kassasi bilan jihozlangan. Dushli maxsus hammom mavjud. Ba'zi xonalarda mikroto'lqinli pech bilan jihozlangan oshxona mavjud. Atlantis mehmonxonasining xonalari sochiq va choyshablar bilan jihozlangan."""  , 
    reply_markup=Orqaga_hotels_7)
    await call.message.answer_location(41.21621318224051, 69.21970901212063)


    


@dp.callback_query_handler(text="south")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""South Hotel""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/69", caption="""Janubiy mehmonxona Toshkent shahrida joylashgan. Unda restoran, bar, teras va bog' mavjud. Resepsiyon kuniga 24 soat ochiq va xona xizmati mavjud. Mehmonlar uchun aeroport xizmati tashkil etilishi mumkin. Mehmonxonada bepul Wi-Fi mavjud.Xonalar konditsioner, sun'iy yo'ldosh kanallari bilan tekis ekranli televizor, minibar, choynak, ish stoli, bide va bepul hojatxona jihozlari bilan jihozlangan. Sochiq va choyshab bilan ta'minlangan.""" , reply_markup=Orqaga_hotels_7)
    await call.message.answer_location(41.25806833666005, 69.2276244391032)



# SHAYHONTOHUR - HOTELS :


@dp.callback_query_handler(text="orqagaaaaaaaaaa")
async def orqaga(call: types.CallbackQuery):
    await call.message.answer("orqga qayttingiz", reply_markup=shayxontohur_menu)


@dp.callback_query_handler(text="jules")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Jules Verne Hostel""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/70", caption="""Umumiy dam olish xonasiga ega Jules Verne Hostel Toshkentda joylashgan. Mehmonxonada 24 soatlik resepsiyon va umumiy oshxona mavjud. Mehmonlar uchun aeroport xizmati tashkil etilishi mumkin. Bepul Wi-Fi mavjud.Umumiy hammom dush va fen bilan jihozlangan.Hostelda har kuni kontinental nonushta taqdim etiladi.Hostelda har kuni kontinental nonushta taqdim etiladi.""" , reply_markup=Orqaga_hotels_8)
    await call.message.answer_location(41.334484298432535, 69.27131496608736)



@dp.callback_query_handler(text="palma")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Palma""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/71", caption="""Mehmonlarga quyidagi xizmatlar taklif etiladi: xonada ovqat va ichimliklar buyurtma qilish, to'xtash joyi, qulay restoran.Mehmonxona xodimlari rus tilini yaxshi biladi.Palma to'rt kishilik, uch kishilik, ikki kishilik, bir kishilik, ikki kishilik yoki egizaklik kabi toifadagi jami 5 ta xonani turli narxlardagi turar joy variantlarini taklif etadi.Palma Toshkentning Olmazor tumani Farobiy 448 V manzilida joylashgan. Shahar markazidan 7,1 km uzoqlikda joylashgan.""" , reply_markup=Orqaga_hotels_8)
    await call.message.answer_location(41.348524327100094, 69.16557162174188)





@dp.callback_query_handler(text="friday")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Friday Hotel""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/72", caption="""Friday Hotel Toshkent shahrida joylashgan. U 24 soatlik resepsiyon, aeroport transferlari, xona xizmati va bepul Wi-Fi xizmatlarini taklif etadi.Mehmonxonaning har bir xonasida choynak mavjud. Friday Hotel mehmonxonasidagi xonalar shahar manzarasini taqdim etadi. Xususiy hammomda dush va bepul hojatxona jihozlari mavjud. Har bir xonada konditsioner va tekis ekranli televizor mavjud.Friday Hotel alakart nonushta taklif qiladi.Islom Karimov Toshkent xalqaro aeroporti 10 km masofada joylashgan.""" , reply_markup=Orqaga_hotels_8)
    await call.message.answer_location(41.33909772324412, 69.2937406832904)



@dp.callback_query_handler(text="mulberry")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Mulberry Hotel""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/73", caption="""3 yulduzli Mulberry mehmonxonasi Xoja Ahror Valiy masjidi yaqinida, Koʻkeldosh madrasasidan 5 daqiqalik masofada joylashgan. Qo'shimcha qulaylik uchun sayt ichida bepul to'xtash joyi mavjud.Mehmonxona Abdulla Murodjaev 17a dan 1,7 km dan kamroq masofada joylashgan. Chorsu metro bekati 300 metr masofada joylashgan. Mehmonlar mehmonxonadan bir necha daqiqalik masofada joylashgan O‘zbekiston Davlat amaliy san’at muzeyiga tashrif buyurishlari mumkin. "Hadra maydoni" avtobus bekati 5 daqiqalik piyoda.""" , reply_markup=Orqaga_hotels_8)
    await call.message.answer_location(41.32524946960978, 69.24002890841363)


@dp.callback_query_handler(text="art")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""ART B&B HOTEL""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/74", caption="""Hudud obodonlashtirilgan va obodonlashtirilgan. Internetga kirish ta'minlandi.Mehmonxona xodimlari turk, rus, ingliz tillarida gaplashadi.ART B&B Hostel — Toshkentdagi yotoqxona boʻlib, oʻz mehmonlarini Kichik Xalqa Yoʻli, X. Irgashev 80, Toshkent, Oʻzbekiston manzilida kutmoqda. Shahar markazi 4 km uzoqlikda joylashgan.""" , reply_markup=Orqaga_hotels_8)
    await call.message.answer_location(41.30283959356487, 69.24030700585979)




# UCHTEPA - HOTELS :



@dp.callback_query_handler(text="orqagaaaaaaaaaaa")
async def orqaga(call: types.CallbackQuery):
    await call.message.answer("orqga qayttingiz", reply_markup=uchtepa_menu)



@dp.callback_query_handler(text="bolaxon")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""BoloXona""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/80", caption="""Hostel BoloXona Toshkentda restoran, bar, umumiy dam olish maskani va bog'ga ega. Old stol 24/7 ochiq. Mehmonlar umumiy oshxona, bepul Wi-Fi va aeroportga transport xizmatidan foydalanishlari mumkin.Xonalarda shkaf mavjud. Mehmonlar umumiy hammomdan foydalanishlari mumkin. Terlik va choyshab bilan ta'minlangan.Har kuni ertalab alakart nonushta beriladi.Qum qishlogʻi 16 km uzoqlikda joylashgan.""" , reply_markup=Orqaga_hotels_9)
    await call.message.answer_location(41.28378692009303, 69.17890981212419)






@dp.callback_query_handler(text="rd")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""RD HOSTEL""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/81", caption="""RD-HOSTEL Toshkent shahrida joylashgan. Mulkning ba'zi xonalarida shahar manzarali balkon mavjud.Yotoqxonada har bir xona shkaf bilan jihozlangan.RD-HOSTEL mehmonlarga hududni aylanib chiqishda yordam berish uchun resepsiyonda qulay ma'lumotlarni taqdim etishi mumkin.Eng yaqin aeroport - Islom Karimov nomidagi Toshkent xalqaro aeroporti, turar joydan 15 km uzoqlikda.""" , reply_markup=Orqaga_hotels_9)
    await call.message.answer_location(41.29440395892875, 69.17399351085913)



@dp.callback_query_handler(text="vatan")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Vatan Plaza Hotel""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/82", caption="""“Vatan Plaza” mehmonxonasi Toshkent shahrida joylashgan. Unda bar va yevropa taomlarini taklif qiluvchi restoran mavjud. Imkoniyatlar orasida 24 soatlik resepsiyon, umumiy dam olish xonasi va bepul Wi-Fi mavjud. Mehmonlar uchun aeroport xizmati tashkil etilishi mumkin.Har bir xonada shkaf mavjud. Konditsionerli xonalar tekis ekranli televizor va seyf bilan jihozlangan.Har kuni bufet, kontinental yoki to'liq ingliz/irland nonushtasi taqdim etiladi.Eng yaqin aeroport - Islom Karimov nomidagi Toshkent xalqaro aeroporti, Vatan Plaza mehmonxonasidan 13 km uzoqlikda.""" , reply_markup=Orqaga_hotels_9)
    await call.message.answer_location(41.279400675199184, 69.1768098139803)




@dp.callback_query_handler(text="sanor")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Sanor Capsule Hotel""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/83", caption="""Mehmonlarga taqdim etiladigan xizmatlar: bog ', aeroportdan / aeroportga o'tkazish, avtoulovlar uchun to'xtash joyi, tungi klub, oshxona, yo'lda tushlik qilish, malakali bolalar parvarishi, tennis korti, old stol kechayu kunduz ochiq.Chet ellik mehmonlar uchun turk, rus, ingliz tillarini biladigan xodimlar mavjud.Hostel SANOR Capsule Hotel Toshkent shahrida, Mirzo Ulug‘bek shoh ko‘chasi 73-uyda, markazdan 7,1 km uzoqlikda joylashgan. Ushbu mulk sport bilan shug'ullanish uchun javob beradi.""" , reply_markup=Orqaga_hotels_9)
    await call.message.answer_location(41.33229782031418, 69.33199404096324)



@dp.callback_query_handler(text="aka")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""AKA Hostel""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/84", caption="""Yakkasaroyda joylashgan AKA Hostel umumiy zal va bepul Wi-Fi-ni taklif etadi.Yotoqxonadagi barcha xonalar dushli umumiy hammomni o'z ichiga oladi.Eng yaqin aeroport - Islom Karimov nomidagi Toshkent xalqaro aeroporti, AKA Hosteldan 8 km uzoqlikda.""" , reply_markup=Orqaga_hotels_9)
    await call.message.answer_location(41.28291013569229, 69.2259690458522)


# YASHNABODD - HOTELS :
 

@dp.callback_query_handler(text="orqagaaaaaaaaaaaa")
async def orqaga(call: types.CallbackQuery):
    await call.message.answer("orqga qayttingiz", reply_markup=yashnobod_menu)



@dp.callback_query_handler(text="lux")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Eurolux Boutique""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/75", caption="""Eurolux Boutique-Hotel Toshkent shahrida joylashgan. Hududda bog' mavjud. Mehmonxonada Wi-Fi-dan bepul foydalanish mumkin va mehmonxonada bepul shaxsiy avtoturargoh mavjud.Mehmonxonaning har bir xonasi ish stoli bilan jihozlangan. Konditsionerli xonalar tekis ekranli televizor bilan jihozlangan. Xususiy hammomda dush va bepul hojatxona jihozlari mavjud. Ba'zi xonalarda balkon mavjud. Barcha xonalar muzlatgich bilan jihozlangan.Islom Karimov Toshkent xalqaro aeroporti 8 km masofada joylashgan.""" , reply_markup=Orqaga_hotels_10 )
    await call.message.answer_location(41.312120160406906, 69.30879367568971)



@dp.callback_query_handler(text="iris")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Hotel IRIS""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/76", caption="""IRIS mehmonxonasi Toshkent shahrida joylashgan. Saytda pullik shaxsiy avtoturargoh va bepul Wi-Fi mavjud.Mehmonxonadagi barcha xonalar sun'iy yo'ldosh kanallari bilan tekis ekranli televizor bilan jihozlangan. IRIS mehmonxonasining har bir xonasida konditsioner va ish stoli mavjud.Har kuni ertalab kontinental nonushta beriladi.Qabulxona xodimlari rus va ingliz tillarida gaplashadi va kunning istalgan vaqtida mehmonlarga yordam berishga tayyor.Eng yaqin aeroport - Islom Karimov nomidagi Toshkent xalqaro aeroporti, IRIS mehmonxonasidan 6 km uzoqlikda. Qo'shimcha haq evaziga aeroportga xizmat ko'rsatish mumkin.""" , reply_markup=Orqaga_hotels_10)
    await call.message.answer_location(41.29449968889708, 69.33292451026838)





@dp.callback_query_handler(text="va")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Safarova Hostel""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/77", caption="""Safarovning oilaviy yotoqxonasi Toshkent shahrida joylashgan. Unda umumiy dam olish xonasi, teras, bar va butun mulk bo'ylab bepul Wi-Fi mavjud. Aeroportga transport xizmati taqdim etiladi. Velosiped ijarasi do'koni mavjud.Ba'zi xonalarda muzlatgich, mikroto'lqinli pech va minibar bilan jihozlangan oshxona mavjud.Hostel mehmonlari kontinental nonushta qilishlari mumkin.Siz Safarov's Family Hostelda dart o'ynashingiz mumkin. Hudud piyoda yurish va velosipedda sayr qilish uchun mashhur.Mehmonxonada dazmollash moslamalari, bepul shaxsiy avtoturargoh, biznes markazi va 24 soatlik resepsiyon mavjud.Islom Karimov Toshkent xalqaro aeroporti 3 km masofada joylashgan.""" , reply_markup=Orqaga_hotels_10)
    await call.message.answer_location(41.28283294108688, 69.30435891212409)


@dp.callback_query_handler(text="khan")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Khan Palace hostelI""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/78", caption="""Khan Palace mehmonxonasi Yakkasaroyda joylashgan. Mehmonxonada 24 soatlik resepsiyon, aeroport transferlari, umumiy dam olish xonasi va butun mulk bo'ylab bepul Wi-Fi mavjud.Mehmon xonalari konditsioner, kabel kanalli tekis ekranli televizor, muzlatgich, choynak, dush, bepul hojatxona jihozlari va stol bilan jihozlangan. Har bir xona seyf bilan jihozlangan, ba'zi xonalar esa balkon bilan jihozlangan. Birliklarga garderob kiradi.Mehmonxonada har kuni bufet nonushtasi mavjud.Eng yaqin aeroport Islom Karimov nomidagi Toshkent xalqaro aeroporti, Khan Palace mehmonxonasidan 2 km uzoqlikda.""" , reply_markup=Orqaga_hotels_10)
    await call.message.answer_location(41.27284440574145, 69.31148633334942)


@dp.callback_query_handler(text="harmony")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Harmony Hotel""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/79", caption="""Harmony Tashkent mehmonxonasi Toshkent shahrida joylashgan. Unda bar va butun bo'ylab bepul Wi-Fi mavjud. Mehmonlar mahalliy taomlarni taklif qiluvchi restoranga tashrif buyurishlari mumkin. Siz mashinangizni bepul shaxsiy avtoturargohda qoldirishingiz mumkin.Xonalar konditsioner bilan jihozlangan. Unda stol, choynak, minibar, seyf, tekis ekranli televizor va bidetli xususiy hammom mavjud. Harmony Tashkent mehmonxonasi xonalarida sochiq va choyshablar mavjud.Islom Karimov Toshkent xalqaro aeroporti 2 km masofada joylashgan. Qo'shimcha haq evaziga aeroportga xizmat ko'rsatish mumkin.""" , reply_markup=Orqaga_hotels_10)
    await call.message.answer_location(41.266579883923995, 69.31523640636684)

# YANGIHAYOT - HOTELS :

@dp.callback_query_handler(text="orqagaaaaaaaaaaaaa")
async def orqaga(call: types.CallbackQuery):
    await call.message.answer("orqga qayttingiz", reply_markup=yangihayot_menu)



@dp.callback_query_handler(text="yangiha")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Yangi hotel""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/90", caption="""Restoranga ega “Yangi” mehmonxonasi Yakkasaroyda joylashgan. Toshkent mehmonxonadan 3,2 milya, Qum esa 6 milya masofada joylashgan.""" , reply_markup=Orqaga_hotels_11)
    await call.message.answer_location(41.27040010655858, 69.2521478353912)


@dp.callback_query_handler(text="hon")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Hotel Hon Saroy""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/91", caption="""Teras va saunaga egadgjhdfgdfhgidfhg kj  kdfjugifjkgheruytw 
      ureytiurytuerthufhredrfjeriut io Xon Saroy mehmonxonasi Toshkentda joylashgan. U bepul Wi-Fi va saytdagi bepul shaxsiy avtoturargohni taklif etadi.Barcha xonalar sun'iy yo'ldosh kanallari bilan tekis ekranli televizor bilan jihozlangan. Ba'zi xonalarda yashash maydoni mavjud. Boshqa qulayliklar orasida choynak mavjud. Dush va bide bilan jihozlangan maxsus hammom ham mavjud. Xonalarda xalat, shippak va bepul hojatxona jihozlari mavjud.Mehmonxona mehmonlari velosipedni bepul ijaraga olishlari mumkin. “Xon Saroy” mehmonxonasi Toshkent xalqaro aeroportidan 6 km uzoqlikda joylashgan.""" , reply_markup=Orqaga_hotels_11)
    await call.message.answer_location(41.29130259679881, 69.26010746608516)


@dp.callback_query_handler(text="citya")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""City Hotel""") 
    await call.message.answer_photo("https://t.me/vd_uz_n1/97", caption="""CITY mehmonxonasi Toshkent shahrida joylashgan. Unda bog' va bar mavjud. Bepul Wi-Fi mavjud. Maxsus to'xtash joylari qo'shimcha haq evaziga mavjud.Bu konditsioner xonada kabel kanallari bilan tekis ekranli televizor, minibar, choynak, stol, dush va bepul hojatxona jihozlari mavjud. Maxsus hammom hammom, fen va shippak bilan jihozlangan. Barcha xonalar sochiq va choyshablar bilan jihozlangan.Islom Karimov nomidagi Toshkent xalqaro aeroporti 3 km.""" , reply_markup=Orqaga_hotels_11)
    await call.message.answer_location(41.285413017316245, 69.25594140451717)

@dp.callback_query_handler(text="place")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Hotel Palace""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/92", caption="""Palace Tashkent mehmonxonasi Toshkent shahrida joylashgan. Mulkda bog ', umumiy dam olish xonasi, teras va bar mavjud. Mehmonxonada velosipedlarni bepul ijaraga olish mumkin. Imkoniyatlar orasida restoran, yopiq basseyn va fitnes markazi mavjud. Resepsiyon kuniga 24 soat ochiq va xona xizmati mavjud. Mehmonxonada valyuta ayirboshlash xizmati mavjud.Barcha konditsionerli xonalar muzlatgich, qahva mashinasi va sun'iy yo'ldosh kanallari bilan tekis ekranli televizor bilan jihozlangan. Dush, bepul hojatxona jihozlari va ish stoli ham mavjud. Har bir xonada seyf va bepul Wi-Fi mavjud. Ba'zi xonalar shahar manzarasini taqdim etadi. Barcha xonalarda sochiq va choyshablar mavjud.Islom Karimov Toshkent xalqaro aeroporti 9 km masofada joylashgan.""" , reply_markup=Orqaga_hotels_11)
    await call.message.answer_location(41.31115787374183, 69.31838578917957)






@dp.callback_query_handler(text="uniq")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""UNIQUE HOTEL""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/93", caption="""UNIQUE mehmonxonasi Chilonzor aholi punktida joylashgan. Mehmonlar umumiy dam olish xonasi, yopiq basseyn, hamam, teras va bog'dan foydalanishlari mumkin. Resepsiyon 24/7 ochiq; bepul Wi-Fi mavjud.Har bir konditsioner xonada shkaf, ish stoli, muzlatgich va tekis ekranli televizor mavjud. UNIQUE mehmonxonasining ba'zi xonalarida balkon ham mavjud.Mehmonlar har kuni ertalab kontinental, halol yoki bufet nonushtasidan birini tanlashlari mumkin.Boshqa narsalar qatorida, UNIQUE Hotel spa markazini taklif etadi. Chilonzor va uning atrofida sayr qilish va ochiq havoda sayr qilish uchun barcha sharoit yaratilgan.Islom Karimov nomidagi Toshkent xalqaro aeroporti 5 km masofada joylashgan.""" , reply_markup=Orqaga_hotels_11)
    await call.message.answer_location(41.27887347880058, 69.23926468143098)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
