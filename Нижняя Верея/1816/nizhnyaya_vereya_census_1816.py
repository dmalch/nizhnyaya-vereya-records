from verso.ru.dsl import (CensusRole, Month, RecordDefaults, census_records, household, member,
                          page, person)
from verso.ru.dsl.statuses import ECON_PEASANT_FEMALE, ECON_PEASANT_MALE

# 7-я ревизия 1816 г., «1816 года марта … дня Владимирской губерніи Меленковскаго уѣзда деревни
# Нижней Верьи» (число в бланке не проставлено). **ГАВО ф. 301 оп. 5 д. 371, лл. 891–901**
# (заказ № 5003, получен 28.10.2026; Photos «Нижняя Верея 1816 РС-7 (ГАВО 301-5-371)», pk 3752).
# Архив сам нашёл сказку деревни и переписал листы задания: заказывали лл. 881–920об.
# Сказка целая — от первой семьи до итога «…вѣрно мужеска пола на лицо 124» и подписи на
# л. 900об–901; в альбоме нет только оборота титульного листа 891об–892 и последнего оборота.
#
# Взяты дворы рода Гусевых (`../Гусев.md`) — 16 (Ефимъ Абрамовъ), 17 (Пантелей Андреевъ,
# внукъ Абрама Дорофеева) и 18 (Полиевктъ Абрамовъ). Ладугиных в 1816 г. в деревне ещё нет:
# Никита Сергеевъ «перечисленъ изъ села Степанкова въ 1828 году» (РС-8 1834, семья 33).
#
# 🏆 **СЕМЬЯ 16 ДОКАЗЫВАЕТ ОТЦА ИППОЛИТА:** «Ефимъ Абрамовъ 50 / 54; Ефимовъ сынъ Ипполитъ
# 8 / 12». РС-8 1834 г. ведёт ту же семью дальше («Ефимъ Абрамовъ 54, умеръ въ 1821 году;
# Ефимовъ сынъ Ипполитъ 12 / 30»), РС-10 1857 г. — Ипполитъ Ефимовъ Гусовъ. Полуектовичи и
# Ефимовичи — двоюродные, обе линии от Абрама Дорофеева.
#
# Возрасты: первая графа — по 6-й ревизии 1811 г., вторая — на март 1816 г.; разница везде 4
# (Ипполитъ 8→12, Иванъ 27→31), как и в дмитриевогорской сказке того же года.
#
# reviewed=False: прочитано 28.10.2026 по кадрам 280 и 290 при ~1×; вычитать в Verso.

census = census_records(
    "ГАВО", "301", "5", "371", "Нижняя Верея", 1816,
    *page("895об",
          household("16",
                    member(1, person("Ефимъ", "Абрамовъ"), CensusRole.HEAD, previous_age=50, age=54),
                    member(2, person("Ипполитъ"), CensusRole.SON, ref_member=1, previous_age=8, age=12),
                    # женская страница л. 896: «Ефима Абрамова жена Авдотья 52; его же дочь Пелагея 20»
                    member(3, person("Авдотья"), CensusRole.WIFE, ref_member=1, age=52),
                    member(4, person("Пелагея"), CensusRole.DAUGHTER, ref_member=1, age=20),
                    ),
          ),
    *page("896об",
          household("17",
                    member(1, person("Пантелей", "Андреевъ"), CensusRole.HEAD, previous_age=46, age=50),
                    member(2, person("Авдотья"), CensusRole.WIFE, ref_member=1, age=45),
                    ),
          household("18",
                    member(1, person("Полиевктъ", "Абрамовъ"), CensusRole.HEAD, previous_age=61, age=65,
                           comment="в той же строке и «полуектовъ сынъ» — оба написания"),
                    member(2, person("Иванъ"), CensusRole.SON, ref_member=1, previous_age=27, age=31),
                    member(3, person("Ксенофонтъ"), CensusRole.SON, ref_member=2, previous_age=4, age=8),
                    member(4, person("Ефимъ"), CensusRole.SON, ref_member=2, previous_age=3, age=7),
                    member(5, person("Осипъ"), CensusRole.SON, ref_member=2, previous_age="полгода",
                           departure_year=1813, departure_reason="умер"),
                    # «новорожденной» в первой графе, «году» во второй
                    member(6, person("Ѳедоръ"), CensusRole.SON, ref_member=2, age=1),
                    # женская страница л. 897: «Полиевкта Абрамова жена Авдотья 63; Ивана Полуектова
                    # жена Прасковья 31» (в ИР 1805 г. — «Прасковья Панфилова, 22»)
                    member(7, person("Авдотья"), CensusRole.WIFE, ref_member=1, age=63),
                    member(8, person("Прасковья"), CensusRole.WIFE, ref_member=2, age=31),
                    ),
          ),
    record_month=Month.MARCH,
    prev_revision_year=1811,
    defaults=RecordDefaults(residence="Нижняя Верея", status_male=ECON_PEASANT_MALE,
                            status_female=ECON_PEASANT_FEMALE),
    reviewed=False,
)
