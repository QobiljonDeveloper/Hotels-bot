from aiogram.types import InlineKeyboardMarkup , InlineKeyboardButton


Regions = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🌆Yunusabad" , callback_data="yunusabad"),
            InlineKeyboardButton("🌆Chilonzor" , callback_data="chilonzor") 
        ],
      [
        InlineKeyboardButton("🌆Yakkasaroy" , callback_data="yakkasaroy"),
        InlineKeyboardButton("🌆Bektemir" , callback_data="bektemir")
      ],
      [
        InlineKeyboardButton("🌆Mirzo Ulug'bek" , callback_data="mirzo"),
        InlineKeyboardButton("🌆Mirobod" , callback_data="mirobod")
      ],
      [
        InlineKeyboardButton("🌆Olmazor" , callback_data="olmazor"),
        InlineKeyboardButton("🌆Sergeli" , callback_data="sergeli")
      ],
      [
        InlineKeyboardButton("🌆Shayxontohur" ,callback_data="shayhontohur"),
        InlineKeyboardButton("🌆Yashnabod" , callback_data="yashnabod")
      ],
      [
        InlineKeyboardButton("🌆Uchtepa" , callback_data="uchtepa"),
        InlineKeyboardButton("🌆Yangihayot" , callback_data="hayot")
      ]
    ],
)


Hotels = InlineKeyboardMarkup(
    inline_keyboard=[   
        [
            InlineKeyboardButton("Uzbekistan Hotels" , callback_data="uzbekistan"),
            InlineKeyboardButton("Гостиница Золотая Долина"  ,callback_data="gostina")
        ],
        [
            InlineKeyboardButton("International Hotel Tashkent" , callback_data="internetion"),
            InlineKeyboardButton("CITY PLACE" , callback_data="place")
        ],
        [
            InlineKeyboardButton("GRAND CAPITAL HOTEL" , callback_data=("grand")),
            InlineKeyboardButton("Orqaga" , callback_data="orqaga")
        ]
    ]
)


chilonzorz_hotels = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("DIAMOND" , callback_data="dimond"),
            InlineKeyboardButton("DUBAY" , callback_data="dubay")
        ],
        [
            InlineKeyboardButton("GRAND ATLAS HOTEL" ,callback_data="atlas"),
            InlineKeyboardButton("HILAL HOTEL" , callback_data="hilal")
        ],
        [
            InlineKeyboardButton("HOTELIOS" , callback_data="lios"),
            InlineKeyboardButton("Orqaga" , callback_data="orqaga")
        ]
    ]
)



yakkasaroys_hotels = InlineKeyboardMarkup( 
    inline_keyboard=[
        [
            InlineKeyboardButton("Panarams Hotel Tashkent" , callback_data="panarama"),
            InlineKeyboardButton("BEST GUESTHOUSE" , callback_data="best")
        ],
        [
            InlineKeyboardButton("Sevinch Hotel" , callback_data="sevinch"),
             InlineKeyboardButton("Orient Grand Hotel" , callback_data="grand" )
        ],
        [
            InlineKeyboardButton("Demure Hotel" , callback_data="demure"),
            InlineKeyboardButton("Orqaga" , callback_data="orqaga")
        ]
    ]
)



bektemirs_hotels = InlineKeyboardMarkup(
    inline_keyboard=[
        [
           InlineKeyboardButton(text="Diyora hostel", callback_data="diyora"),
            InlineKeyboardButton(text="Resident hotel", callback_data="resident" ),
        ],
        [
            InlineKeyboardButton(text="Hotel shosh palace", callback_data="shosh"),
             InlineKeyboardButton(text="Hayot hostel", callback_data="hayot"),
        ],
        [
             InlineKeyboardButton(text="Ayva hotel", callback_data="ayva"),
            InlineKeyboardButton("Orqaga" , callback_data="orqaga")
        ]
])




mirzo_ulugbek_hotels = InlineKeyboardMarkup(
    inline_keyboard=[
            [
                InlineKeyboardButton(text="Sofiya Hotel Tashkent", callback_data="sofia"),
                 InlineKeyboardButton(text="Kamal Hote", callback_data="kamal"),
            ],
            [
                InlineKeyboardButton(text="The Top Hostel", callback_data="top"),
                 InlineKeyboardButton(text="Asli Makon Hotel", callback_data="asli"),
            ],
            [
                 InlineKeyboardButton(text="National Hostel", callback_data="national"),
                 InlineKeyboardButton("Orqaga" , callback_data="orqaga")
            ]
 ] )




mirobod_hotels = InlineKeyboardMarkup(
    inline_keyboard=[
            [
                 InlineKeyboardButton(text="Uzbekistan Hotel", callback_data="uzbekistan1"),
                 InlineKeyboardButton(text="Comfort Hotel", callback_data="comfort"),   
            ],
            [
                  InlineKeyboardButton(text="Gallery Hotel", callback_data="gallery"),
                  InlineKeyboardButton(text="Safarova Hostel", callback_data="safarova"),
            ],
            [
            InlineKeyboardButton(text="BLUE SKY HOTEL", callback_data="blue"),
                 InlineKeyboardButton("Orqaga" , callback_data="orqaga")

            ]
]
)





olmazor_menu = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="Budget Hostel", callback_data="budget"),
            InlineKeyboardButton(text="Hotel OK", callback_data="ok"),
        ],
        [
            InlineKeyboardButton(text="HostelPoint", callback_data="ponit"),
            InlineKeyboardButton(text="PARADISE HOSTEL", callback_data="paradise"),
        ],
        [
            InlineKeyboardButton(text="MASKAN HOTEL", callback_data="maskan"),
             InlineKeyboardButton("Orqaga" , callback_data="orqaga")
        ],
    ]
)


sergeli_menu = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="Hotel Empire", callback_data="empire"),
            InlineKeyboardButton(text="Sulaymon hotel", callback_data="sulaymon"),
        ],
        [
            InlineKeyboardButton(text="Daniel Hill", callback_data="hill"),
            InlineKeyboardButton(text="Atlantis Hotel", callback_data="atlan"),
        ],
        [
            InlineKeyboardButton(text="South Hotel", callback_data="south"),
            InlineKeyboardButton("Orqaga" , callback_data="orqaga")
        ],
    ]
)



shayxontohur_menu = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="Jules Verne Hostel", callback_data="jules"),
            InlineKeyboardButton(text="Palma", callback_data="palma"),
        ],
        [
            InlineKeyboardButton(text="Friday Hotel", callback_data="friday"),
            InlineKeyboardButton(text="Mulberry Hotel", callback_data="mulberry"),
        ],
        [
            InlineKeyboardButton(text="ART B&B HOTEL", callback_data="art"),
            InlineKeyboardButton("Orqaga" , callback_data="orqaga")
         ],
    ]
)




uchtepa_menu = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="BoloXona", callback_data="bolaxon"),
            InlineKeyboardButton(text="RD HOSTEL", callback_data="rd"),
        ],
        [
            InlineKeyboardButton(text="Vatan Plaza Hotel", callback_data="vatan"),
            InlineKeyboardButton(text="Sanor Capsule Hotel", callback_data="sanor"),
        ],
        [
            InlineKeyboardButton(text="AKA Hostel", callback_data="aka"),
            InlineKeyboardButton("Orqaga" , callback_data="orqaga")
        ],
    ]
)

yashnobod_menu = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="Eurolux Boutique", callback_data="lux"),
            InlineKeyboardButton(text="Hotel IRIS", callback_data="iris"),
        ],
        [
            InlineKeyboardButton(text="Safarova Hostel", callback_data="va"),
            InlineKeyboardButton(text="Khan Palace hostel", callback_data="khan"),
        ],
        [
            InlineKeyboardButton(text="Harmony Hotel", callback_data="harmony"),
            InlineKeyboardButton("Orqaga" , callback_data="orqaga")
        ],
    ]
)


yangihayot_menu = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="Yangi hotel", callback_data="yangiha"),
            InlineKeyboardButton(text="Hotel Hon Saroy", callback_data="hon"),
        ],
        [
            InlineKeyboardButton(text="City Hotel ", callback_data="citya"),
            InlineKeyboardButton(text="Hotel Palace", callback_data="place"),
        ],
        [
            InlineKeyboardButton(text="UNIQUE HOTEL", callback_data="uniq"),
            InlineKeyboardButton("Orqaga" , callback_data="orqaga")
        ],
    ]
)







Orqaga_hotels = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🔙Orqaga" , callback_data="orqagaa"),
        ],
    ]
)








Orqaga_hotels_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🔙Orqaga" , callback_data="orqagaaa"),
        ],
    ]
)


Orqaga_hotels_2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🔙Orqaga" , callback_data="orqagaaaa"),
        ],
    ]
)
Orqaga_hotels_3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🔙Orqaga" , callback_data="orqagaaaaa"),
        ],
    ]
)



Orqaga_hotels_4 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🔙Orqaga" , callback_data="orqagaaaaaa"),
        ],
    ]
)

Orqaga_hotels_5 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🔙Orqaga" , callback_data="orqagaaaaaaa"),
        ],
    ]
)

Orqaga_hotels_6 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🔙Orqaga" , callback_data="orqagaaaaaaaa"),
        ],
    ]
)


Orqaga_hotels_7 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🔙Orqaga" , callback_data="orqagaaaaaaaaa"),
        ],
    ]
)





Orqaga_hotels_8 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🔙Orqaga" , callback_data="orqagaaaaaaaaaa"),
        ],
    ]
)



Orqaga_hotels_9 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🔙Orqaga" , callback_data="orqagaaaaaaaaaaa"),
        ],
    ]
)



Orqaga_hotels_10 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🔙Orqaga" , callback_data="orqagaaaaaaaaaaaa"),
        ],
    ]
)


Orqaga_hotels_11 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🔙Orqaga" , callback_data="orqagaaaaaaaaaaaaa"),
        ],
    ]
)