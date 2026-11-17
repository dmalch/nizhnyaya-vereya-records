from verso.ru.dsl import (Month, RecordDefaults, Relationship, Side, marriage, marriage_month,
                          marriage_records, page, person, relative)
from verso.ru.dsl.statuses import (KAZENNYJ_PEASANT_FEMALE, KAZENNYJ_PEASANT_GIRL,
                                   KAZENNYJ_PEASANT_MALE, SOLDIER_DAUGHTER, WIDOW)

# Метрическая книга Успенской церкви с. ШИМОРСКОГО за 1859 г., часть вторая — венчания с
# участием «Казеннаго вѣдомства деревни Нижней Верьи». **ГАВО ф. 590 оп. 5 д. 4, лл. 915об–926об**
# (альбом «Шиморское 1859 (ГАВО 590-5-4)»; консисторская копия, поручители — на recto).
# Прочитана вся часть вторая (65 венчаній): из НВ — четыре жениха (№ 7, 16, 17, 18).
#
# Все четыре сходятся с РС-10 1857 г. (`../1857/rs10_1857_households.md`): № 7 — двор 34
# (Иванъ Гурьевъ, сынъ Александръ 18 л 2 мѣс), № 16 — двор 9 (Родіонъ Симоновъ, сынъ Ѳилиппъ 16) и
# двор 32 (Григорій Осиповъ, дочь Агаѳья 15), № 17 — двор 36 (Козьма Ивановъ), № 18 — двор 15
# (Евстигней, сынъ Николай 16 л 11 мѣс).
#
# reviewed=False: прочитано при 2–2.4×, имена — при 5–9×; спорное — в комментариях.

DEFAULTS = RecordDefaults(residence="Нижняя Верея", status_male=KAZENNYJ_PEASANT_MALE,
                          status_female=KAZENNYJ_PEASANT_FEMALE)

nizhnyaya_vereya_marriages_1859 = marriage_records(
    "ГАВО", "590", "5", "4", "Нижняя Верея", "Успенская",
    1859,
    *page("916об",
          *marriage_month(Month.FEBRUARY,
                          # «Казеннаго вѣдомства деревни Нижней Верьи крестьянина Ивана Гурьева сынъ Александръ
                          # первымъ бракомъ», 19 ⚭ «Тогожъ вѣдомства … нова Ольга? Степанова, деревни Высокова
                          # крестьянина Ѳедора Евѳимова? дочь вдовица? первымъ бракомъ», 21. ⚠ Первая строка
                          # невѣсты не прочитана и при 9×; «Степанова» при отце Ѳедорѣ — так в подлиннике, вписано
                          # как написано. Поручители (л. 917): «по женихѣ крестьяне Емельянъ и Василій Мироновы,
                          # а по невѣстѣ Ѳедоръ Ивановъ и Евлампій Ивановъ». Вѣнчалъ священникъ Стефанъ Свавицкій
                          marriage(7, 2,
                                   groom=person("Александръ", "Ивановъ"),
                                   bride=person("Ольга", "Степанова", residence="Высоково"),
                                   groom_age=19, bride_age=21, groom_marriage_num=1,
                                   relatives=[relative(person("Иванъ", "Гурьевъ"), Relationship.FATHER, "жених")],
                                   witness1=person("Емельянъ", "Мироновъ", side=Side.GROOM),
                                   witness2=person("Василій", "Мироновъ", side=Side.GROOM),
                                   witness3=person("Ѳедоръ", "Ивановъ", side=Side.BRIDE),
                                   witness4=person("Евлампій", "Ивановъ", side=Side.BRIDE)),
                          ),
          ),
    *page("917об",
          *marriage_month(Month.OCTOBER,
                          # «Деревни Нижней Верьи крестьянина Родіона Симонова сынъ Ѳилиппъ холостъ», 18 ⚭ «Дѣвка
                          # Агаѳья крестьянина Григорія Осипова дочь тойже деревни и тогожъ исповѣданія», 16.
                          # Поручители (л. 918): «по женихѣ Александръ Родіоновъ (братъ, РС-10 двор 9) и Тихонъ
                          # Савельевъ, и по невѣстѣ Никита Осиповъ (дядя, РС-10 двор 32) и Константинъ Никитинъ»
                          marriage(16, 11,
                                   groom=person("Ѳилиппъ", "Родіоновъ"),
                                   bride=person("Агаѳья", "Григорьева", status=KAZENNYJ_PEASANT_GIRL),
                                   groom_age=18, bride_age=16, groom_marriage_num=1, bride_marriage_num=1,
                                   relatives=[relative(person("Родіонъ", "Симоновъ"), Relationship.FATHER, "жених"),
                                              relative(person("Григорій", "Осиповъ"), Relationship.FATHER, "невеста")],
                                   witness1=person("Александръ", "Родіоновъ", side=Side.GROOM),
                                   witness2=person("Тихонъ", "Савельевъ", side=Side.GROOM),
                                   witness3=person("Никита", "Осиповъ", side=Side.BRIDE),
                                   witness4=person("Константинъ", "Никитинъ", side=Side.BRIDE)),
                          # «Оной же деревни крестьянина Козьмы Иванова сынъ Михаилъ холостъ», 18 ⚭ «Дѣвка
                          # Харитина Евѳимова стрѣлка Евѳима Алексѣева дочь тогожъ исповѣданія», 20 (деревня
                          # невѣсты не названа). «Евѳимъ» — «в» у писца похоже на «р» («Ерѳимъ»; так же
                          # прочитано в РС-10, двор 15). ⚠ В РС-10 1857 г. (двор 36) Михаила среди сыновей Козьмы НЕТ —
                          # Павелъ, Марка, Дмитрій, Иванъ, Стефанъ; поручители по женихѣ — «Дмитрій и Иванъ
                          # Козьмины», т. е. братья. По невѣстѣ — «Василій Мироновъ и Савелій? Никитинъ» (л. 918)
                          marriage(17, 11,
                                   groom=person("Михаилъ", "Козьминъ"),
                                   bride=person("Харитина", "Евѳимова", status=SOLDIER_DAUGHTER),
                                   groom_age=18, bride_age=20, groom_marriage_num=1, bride_marriage_num=1,
                                   relatives=[relative(person("Козьма", "Ивановъ"), Relationship.FATHER, "жених"),
                                              relative(person("Евѳимъ", "Алексѣевъ"), Relationship.FATHER, "невеста")],
                                   witness1=person("Дмитрій", "Козьминъ", side=Side.GROOM),
                                   witness2=person("Иванъ", "Козьминъ", side=Side.GROOM),
                                   witness3=person("Василій", "Мироновъ", side=Side.BRIDE),
                                   witness4=person("Савелій", "Никитинъ", side=Side.BRIDE)),
                          ),
          ),
    *page("918об",
          *marriage_month(Month.OCTOBER,
                          # «Оной же деревни крестьянина Евстигнія Авдѣева сынъ Николай, холостъ православнаго
                          # исповѣданія», 18 ⚭ «Дѣвка Татіана Иванова, деревни Гиблова вдовы Агаѳьи Ѳедоровой
                          # дочь тогожъ исповѣданія», 19. «Оной же деревни» — по предыдущей записи № 17 (НВ).
                          # Поручители (л. 919): «по женихѣ Евѳимъ Евстигнѣевъ (братъ, РС-10 двор 15) и Василій
                          # Епифановъ; а по невѣстѣ Герасимъ Ивановъ и Симонъ Климовъ»
                          marriage(18, 18,
                                   groom=person("Николай", "Евстигнѣевъ"),
                                   bride=person("Татіана", "Иванова", status=KAZENNYJ_PEASANT_GIRL, residence="Гиблово"),
                                   groom_age=18, bride_age=19, groom_marriage_num=1, bride_marriage_num=1,
                                   relatives=[relative(person("Евстигней", "Авдѣевъ"), Relationship.FATHER, "жених"),
                                              relative(person("Агаѳья", "Ѳедорова", status=WIDOW, residence="Гиблово"),
                                                       Relationship.MOTHER, "невеста")],
                                   witness1=person("Евѳимъ", "Евстигнѣевъ", side=Side.GROOM),
                                   witness2=person("Василій", "Епифановъ", side=Side.GROOM),
                                   witness3=person("Герасимъ", "Ивановъ", side=Side.BRIDE),
                                   witness4=person("Симонъ", "Климовъ", side=Side.BRIDE)),
                          ),
          ),
    defaults=DEFAULTS,
    reviewed=False,
)
