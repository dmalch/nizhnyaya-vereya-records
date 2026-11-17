from verso.ru.dsl import (CensusRole, Month, RecordDefaults, census_records, household, member,
                          page, person)
from verso.ru.dsl.statuses import ECON_PEASANT_FEMALE, ECON_PEASANT_MALE

# 8-я ревизия 1834 г., «1834 года апрѣля … дня Владимирской губерніи … Экономической деревни
# Нижней Верьи». **ГАВО ф. 301 оп. 5 д. 495, лл. 214–226** (заказ № 5003, получен 28.10.2026;
# Photos «Нижняя Верея 1834 РС-8 (ГАВО 301-5-495)», pk 3753). Заказывали лл. 171–210об — архив
# нашёл сказку деревни на лл. 214–226 и копировал её. 39 семей; в альбоме нет оборота
# титула 214об–215 и последнего оборота.
#
# Взяты Гусевы (`../Гусев.md`) — семьи 16 (Ефимъ Абрамовъ), 17 (Пантелей Андреевъ), 18
# (Поліевктъ Абрамовъ) — и Ладугины (`../Ладугин.md`) — семья 33 (Никита Сергеевъ).
#
# 🏆 Семья 16: «Ефимъ Абрамовъ 54, умеръ въ 1821 году; Ефимовъ сынъ Ипполитъ 12 / 30» — тот
# же двор, что семья 16 РС-7 1816 г.: Ипполитъ — сынъ Ефима Абрамова.
# 🆕 Семья 18 даёт ещё одного сына Ивана Полуектова — Ефима (7 в 1816 г., «умеръ въ 1831
# году») — и жену Ѳедора Ивановича: **Мавра, 22**. РС-9 1850 г. зовёт жену Ѳедора «Марья
# Авдѣева, 36» — другое имя; проверить, не второй ли это брак.
# 🆕 Семья 33 — **корень Ладугиныхъ**: «Никита Сергеевъ», перечислен «по указу казенной
# палаты изъ села Степанкова въ 1828 году», «умеръ въ 1829 году». Отчество деда Никиты
# (`Ладугин.md` знал только «Никита, досёлковое поколение») — **Сергеевъ**. Первая жена
# Савватея — **Татьяна, 19**; в РС-9 1850 г. Василій «отъ 1-й жены».
#
# Первая графа — по 7-й ревизии 1816 г., вторая — на 1834 г. (разница 18).
# reviewed=False: прочитано 28.10.2026 по кадрам 1360, 1370 и 1410; вычитать в Verso.

census = census_records(
    "ГАВО", "301", "5", "495", "Нижняя Верея", 1834,
    *page("218об",
          household("16",
                    member(1, person("Ефимъ", "Абрамовъ"), CensusRole.HEAD, previous_age=54,
                           departure_year=1821, departure_reason="умер"),
                    member(2, person("Ипполитъ"), CensusRole.SON, ref_member=1, previous_age=12, age=30),
                    # «Ипполитовы сыновья: Григорій, Семіонъ — новорожденные»
                    member(3, person("Григорій"), CensusRole.SON, ref_member=2, age=10),
                    member(4, person("Семіонъ"), CensusRole.SON, ref_member=2, age=3),
                    # женская страница л. 219
                    member(5, person("Аксинья"), CensusRole.WIFE, ref_member=2, age=29),
                    member(6, person("Акулина"), CensusRole.DAUGHTER, ref_member=2, age=12),
                    member(7, person("Гликерія"), CensusRole.DAUGHTER, ref_member=2, age=6),
                    member(8, person("Марья"), CensusRole.DAUGHTER, ref_member=2, age="2 недели"),
                    ),
          household("17",
                    member(1, person("Пантелей", "Андреевъ"), CensusRole.HEAD, previous_age=50, age=68),
                    member(2, person("Авдотья"), CensusRole.WIFE, ref_member=1, age=63),
                    ),
          household("18",
                    member(1, person("Поліевктъ", "Абрамовъ"), CensusRole.HEAD, previous_age=65,
                           departure_year=1822, departure_reason="умер"),
                    member(2, person("Иванъ"), CensusRole.SON, ref_member=1, previous_age=31, age=49),
                    # л. 219об
                    member(3, person("Ксенофонтъ"), CensusRole.SON, ref_member=2, previous_age=8, age=26),
                    member(4, person("Григорій"), CensusRole.SON, ref_member=3, age=11),
                    member(5, person("Антонъ"), CensusRole.SON, ref_member=3, age=2),
                    member(6, person("Ефимъ"), CensusRole.SON, ref_member=2, previous_age=7,
                           departure_year=1831, departure_reason="умер",
                           comment="«Ивана Поліевктова другой сынъ Ефимъ»"),
                    member(7, person("Ѳедоръ"), CensusRole.SON, ref_member=2, previous_age=1, age=19,
                           comment="«его же третей сынъ Ѳедоръ»"),
                    member(8, person("Иванъ"), CensusRole.SON, ref_member=7, age="4 мес",
                           comment="«Ѳедора Иванова сынъ Иванъ же», новорожденный"),
                    # женская страница л. 219–220
                    member(9, person("Прасковья"), CensusRole.WIFE, ref_member=2, age=49),
                    member(10, person("Анна"), CensusRole.DAUGHTER, ref_member=2, age=12),
                    member(11, person("Соломея"), CensusRole.WIFE, ref_member=3, age=28),
                    member(12, person("Авдотья"), CensusRole.DAUGHTER, ref_member=3,
                           comment="«… мѣсяца» — число месяцев в скане не прочитано"),
                    member(13, person("Мавра"), CensusRole.WIFE, ref_member=7, age=22),
                    ),
          ),
    *page("223об",
          household("33",
                    member(1, person("Никита", "Сергеевъ"), CensusRole.HEAD,
                           arrival_year=1828, arrival_reason="перечислен по указу казенной палаты из села Степанкова",
                           departure_year=1829, departure_reason="умер"),
                    member(2, person("Алексей"), CensusRole.SON, ref_member=1, age=32,
                           arrival_year=1828, arrival_reason="перечислен по указу казенной палаты из села Степанкова"),
                    member(3, person("Іонъ"), CensusRole.SON, ref_member=2, age=9,
                           arrival_year=1828, arrival_reason="перечислен по указу казенной палаты из села Степанкова"),
                    member(4, person("Кондратей"), CensusRole.SON, ref_member=2, age="3 недели"),
                    member(5, person("Савватей"), CensusRole.SON, ref_member=1, age="20½",
                           arrival_year=1828, arrival_reason="перечислен по указу казенной палаты из села Степанкова",
                           comment="«Никиты Сергеева другой сынъ Савватей»"),
                    # женская страница л. 224
                    member(6, person("Прасковья"), CensusRole.WIFE, ref_member=1, age=58),
                    member(7, person("Екатерина"), CensusRole.WIFE, ref_member=2, age=27),
                    member(8, person("Соломея"), CensusRole.DAUGHTER, ref_member=2, age=3),
                    member(9, person("Татьяна"), CensusRole.WIFE, ref_member=5, age=19),
                    ),
          ),
    record_month=Month.APRIL,
    prev_revision_year=1816,
    defaults=RecordDefaults(residence="Нижняя Верея", status_male=ECON_PEASANT_MALE,
                            status_female=ECON_PEASANT_FEMALE),
    reviewed=False,
)
