from verso.ru.dsl import (CensusRole, Month, RecordDefaults, census_records, household, member,
                          page, person)
from verso.ru.dsl.statuses import GOSUDARSTVENNYJ_PEASANT_FEMALE, GOSUDARSTVENNYJ_PEASANT_MALE

# 9-я ревизия 1850 г., «1850 года іюня 7 дня Владимирской губерніи Меленковскаго уѣзда деревни
# Нижней Верей». **ГАВО ф. 301 оп. 5 д. 633, лл. 415–435** (заказ № 5003, получен 28.10.2026;
# Photos «Нижняя Верея 1850 РС-9 (ГАВО 301-5-633)», pk 3754). Заказывали лл. 59–98об — архив
# нашёл сказку деревни на лл. 415–435. 42 семьи; итог и заверка — л. 434об.
#
# Взяты Гусевы (`../Гусев.md`) — семьи 17 (Ипполитъ Ефимовъ Гусевъ), 18 (Пантелей Андреевъ)
# и 19 (Иванъ Полуектовъ Гусевъ) — и Ладугины (`../Ладугин.md`) — семья 37 (Алексей Никитинъ).
# Фамилия «Гусевъ» здесь впервые в ревизии (РС-10 1857 г. пишет «Гусовъ»).
#
# ✅ Все возрасты сходятся с РС-8 1834 г. (первая графа) и с previous_age РС-10 1857 г.
# 🆕 Даты рождения, которых нет в РС-10: Дмитрій Ксенофонтовъ 3.02.1836, Филиппъ Григорьевъ
# 7.11.1843, Василій Савватеевъ 14.05.1838, Леонтій 15.06.1843, Осипъ 28.10.1846.
# 🆕 Ѳедоръ Ивановъ «умеръ въ 1836 году»; Іона Алексеевъ «отданъ въ рекруты въ 1845 году».
#
# reviewed=False: прочитано 28.10.2026 по кадрам 1010 и 1100; вычитать в Verso.

census = census_records(
    "ГАВО", "301", "5", "633", "Нижняя Верея", 1850,
    *page("424об",
          household("17",
                    member(1, person("Ипполитъ", "Ефимовъ", "Гусевъ"), CensusRole.HEAD, previous_age=30, age=46),
                    member(2, person("Григорій"), CensusRole.SON, ref_member=1, previous_age=10, age=26),
                    member(3, person("Семенъ"), CensusRole.SON, ref_member=1, previous_age=3, age=19),
                    # женская страница л. 425
                    member(4, person("Аксинья", "Леонтьева"), CensusRole.WIFE, ref_member=1, age=45),
                    member(5, person("Марья"), CensusRole.DAUGHTER, ref_member=1, age=16),
                    member(6, person("Улита", "Дмитріева"), CensusRole.WIFE, ref_member=2, age=26),
                    member(7, person("Прасковья"), CensusRole.DAUGHTER, ref_member=2, age=7),
                    member(8, person("Прасковья", "Ермоніева"), CensusRole.WIFE, ref_member=3, age=18),
                    ),
          household("18",
                    member(1, person("Пантелей", "Андреевъ"), CensusRole.HEAD, previous_age=68,
                           departure_year=1837, departure_reason="умер"),
                    ),
          household("19",
                    member(1, person("Иванъ", "Полуектовъ", "Гусевъ"), CensusRole.HEAD, previous_age=49, age=65),
                    member(2, person("Ксенофонтъ"), CensusRole.SON, ref_member=1, previous_age=26, age=42),
                    member(3, person("Григорій"), CensusRole.SON, ref_member=2, previous_age=11, age=27),
                    member(4, person("Филиппъ"), CensusRole.SON, ref_member=3, age="6½",
                           birth_day=7, birth_month=Month.NOVEMBER, birth_year=1843),
                    member(5, person("Антонъ"), CensusRole.SON, ref_member=2, previous_age=2, age=18),
                    member(6, person("Дмитрій"), CensusRole.SON, ref_member=2, age="14 лет 4 мес",
                           birth_day=3, birth_month=Month.FEBRUARY, birth_year=1836),
                    member(7, person("Ѳедоръ"), CensusRole.SON, ref_member=1, previous_age=19,
                           departure_year=1836, departure_reason="умер",
                           comment="«Ивана Полуектова другой сынъ Ѳедоръ»"),
                    member(8, person("Иванъ"), CensusRole.SON, ref_member=7, previous_age="4 мес",
                           age="16 лет 4 мес"),
                    # женская страница л. 425
                    member(9, person("Прасковья", "Панфилова"), CensusRole.WIFE, ref_member=1, age=65),
                    member(10, person("Соломія", "Максимова"), CensusRole.WIFE, ref_member=2, age=44),
                    member(11, person("Елизавета"), CensusRole.DAUGHTER, ref_member=2, age=12),
                    member(12, person("Варвара", "Ѳедорова"), CensusRole.WIFE, ref_member=3, age=27),
                    member(13, person("Наталья"), CensusRole.DAUGHTER, ref_member=3, age=4),
                    member(14, person("Авдотья", "Климова"), CensusRole.WIFE, ref_member=5, age=18),
                    # «Ѳедора Иванова жена Марья Авдѣева» — вдова; в РС-8 1834 г. жена Ѳедора — «Мавра, 22»
                    member(15, person("Марья", "Авдѣева"), CensusRole.WIFE, ref_member=7, age=36),
                    ),
          ),
    *page("432об",
          household("37",
                    member(1, person("Алексей", "Никитинъ"), CensusRole.HEAD, previous_age=32, age=48),
                    member(2, person("Іона"), CensusRole.SON, ref_member=1, previous_age=9,
                           departure_year=1845, departure_reason="отдан в рекруты"),
                    member(3, person("Кондратій"), CensusRole.SON, ref_member=1, previous_age="3 недели",
                           age="16 лет 3 недели"),
                    member(4, person("Власъ"), CensusRole.SON, ref_member=1, age=15),
                    member(5, person("Савватей", "Никитинъ"), CensusRole.BROTHER, ref_member=1,
                           previous_age="20½", age="36½"),
                    member(6, person("Василій"), CensusRole.SON, ref_member=5, age=12,
                           birth_day=14, birth_month=Month.MAY, birth_year=1838, comment="от 1-й жены"),
                    member(7, person("Леонтій"), CensusRole.SON, ref_member=5, age="6 лет 11 мес",
                           birth_day=15, birth_month=Month.JUNE, birth_year=1843, comment="от 2-й жены"),
                    member(8, person("Осипъ"), CensusRole.SON, ref_member=5, age="3 года 7 мес",
                           birth_day=28, birth_month=Month.OCTOBER, birth_year=1846),
                    # женская страница л. 433
                    member(9, person("Наталья"), CensusRole.DAUGHTER, ref_member=1, age=9),
                    member(10, person("Варвара", "Силантьева"), CensusRole.WIFE, ref_member=5, age=35),
                    ),
          ),
    record_day=7,
    record_month=Month.JUNE,
    prev_revision_year=1834,
    defaults=RecordDefaults(residence="Нижняя Верея", status_male=GOSUDARSTVENNYJ_PEASANT_MALE,
                            status_female=GOSUDARSTVENNYJ_PEASANT_FEMALE),
    reviewed=False,
)
