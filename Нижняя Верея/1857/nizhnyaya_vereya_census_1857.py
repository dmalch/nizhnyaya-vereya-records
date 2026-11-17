from verso.ru.dsl import (CensusRole, Month, RecordDefaults, census_records, household, member,
                          page, person)
from verso.ru.dsl.statuses import GOSUDARSTVENNYJ_PEASANT_FEMALE, GOSUDARSTVENNYJ_PEASANT_MALE

# РС 10 (Десятая ревизия) 1857 года, с. Нижняя Верея
# Архив: ГАВО 301-5-787
census = census_records(
    "ГАВО",
    "301",
    "5",
    "787",
    "Нижняя Верея",
    1857,
    *page("717об-718",
          household("17",
                    member(1, person("Ипполитъ", "Ефимовъ", "Гусовъ"), CensusRole.HEAD, age="53 года 5 мес", previous_age=46),
                    member(2, person("Аксінья", "Леонтьева"), CensusRole.WIFE, age=52),
                    member(3, person("Григорій"), CensusRole.SON, age="33 года 5 мес", previous_age=26, comment="Ипполита Ефимова первый сын"),
                    member(4, person("Улита", "Дмитріева"), CensusRole.WIFE, ref_member=3, age=33, comment="Григорья Ипполитова жена"),
                    member(5, person("Иванъ"), CensusRole.SON, ref_member=3, age="1 год 1 мес", birth_day=6, birth_month=Month.OCTOBER, birth_year=1856, comment="Григорьев сын"),
                    member(6, person("Прасковья"), CensusRole.DAUGHTER, ref_member=3, age=14, comment="Григорья Ипполитова его же дочь"),
                    member(7, person("Анна"), CensusRole.DAUGHTER, ref_member=3, age=6, comment="Григорья Ипполитова его же дочь"),
                    member(8, person("Марья"), CensusRole.DAUGHTER, ref_member=3, age=3, comment="Григорья Ипполитова его же дочь"),
                    member(9, person("Семеонъ"), CensusRole.SON, age="26 года 5 мес", previous_age=19, comment="Ипполита Ефимова другой сын"),
                    member(10, person("Прасковья", "Ермоніева"), CensusRole.WIFE, ref_member=9, age=25, comment="Семеона Ипполитова жена"),
                    member(11, person("Андрей"), CensusRole.SON, ref_member=9, age=4, birth_day=12, birth_month=Month.NOVEMBER, birth_year=1853, comment="Семеонов сын"),
                    member(12, person("Александръ"), CensusRole.SON, ref_member=9, age="1 год 8 мес", birth_day=15, birth_month=Month.FEBRUARY, birth_year=1856, comment="Семеонов сын"),
                    member(13, person("Елизавета"), CensusRole.DAUGHTER, ref_member=9, age=5, comment="Семеона Ипполитова его же дочь")),
          household("18",
                    member(1, person("Иванъ", "Полуектовъ", "Гусовъ"), CensusRole.HEAD, age="72 года 5 мес", previous_age=65),
                    member(2, person("Прасковья", "Панфилова"), CensusRole.WIFE, age=73),
                    member(3, person("Ксенофонтъ"), CensusRole.SON, age="49 лет 5 мес", previous_age=42, comment="Ивана Полуектова сын"),
                    member(4, person("Соломѣя", "Максимова"), CensusRole.WIFE, ref_member=3, age=51, comment="Ксенофонта Иванова жена"),
                    member(5, person("Григорій"), CensusRole.SON, ref_member=3, age="34 года 5 мес", previous_age=27, comment="Ксенофонтов сын"),
                    member(6, person("Варвара", "Ѳедорова"), CensusRole.WIFE, ref_member=5, age=34, comment="Григорья Ксенофонтова жена"),
                    member(7, person("Филиппъ"), CensusRole.SON, ref_member=5, age="13 лет 11 мес", previous_age="6 лет 6 мес", comment="Григорьев сын"),
                    member(8, person("Ѳедоръ"), CensusRole.SON, ref_member=5, age="6 лет 5 мес", birth_day=26, birth_month=Month.MAY, birth_year=1851, comment="Григорьев сын"),
                    member(9, person("Василій"), CensusRole.SON, ref_member=5, age="6 мес", birth_day=11, birth_month=Month.APRIL, birth_year=1857, comment="Григорьев сын"),
                    member(10, person("Наталья"), CensusRole.DAUGHTER, ref_member=5, age=11, comment="Григорья Ксенофонтова его же дочь"),
                    member(11, person("Антонъ"), CensusRole.SON, ref_member=3, age="25 лет 5 мес", previous_age=18, comment="Ксенофонтов другой сын"),
                    member(12, person("Авдотья", "Климова"), CensusRole.WIFE, ref_member=11, age=25, comment="Антона Ксенофонтова жена"),
                    member(13, person("Иванъ"), CensusRole.SON, ref_member=11, age="2 года 3 мес", birth_day=18, birth_month=Month.JUNE, birth_year=1855, comment="Антона сын"),
                    member(14, person("Дмитрій"), CensusRole.SON, ref_member=3, age="21 год 9 мес", previous_age="14 лет 4 мес", comment="Ксенофонтов третий сын"),
                    member(15, person("Февронья", "Афанасьева"), CensusRole.WIFE, ref_member=14, age=22, comment="Дмитрия Ксенофонтова жена"),
                    member(16, person("Алексѣй"), CensusRole.SON, ref_member=14, age="1 год 7 мес", birth_day=6, birth_month=Month.MARCH, birth_year=1856, comment="Дмитриев сын"),
                    member(17, person("Иванъ", "Ѳедоровъ"), CensusRole.GRANDSON, parent_member=21, age="23 лет 9 мес", previous_age="16 лет 4 мес", comment="Ивана Полуектова внук"),
                    member(18, person("Мавра", "Димитріева"), CensusRole.WIFE, ref_member=17, age=22, comment="Ивана Федорова жена"),
                    member(19, person("Василій"), CensusRole.SON, ref_member=17, age="7 мес", birth_day=3, birth_month=Month.MARCH, birth_year=1857, comment="Ивана Федорова сын"),
                    # Пропущена при первом вводе; вписана 05.10.2026 по скану (кадр 719, женская сторона):
                    # «Ивана Ѳедорова мать Марья Авдѣева — 43». Итог страницы «женскаго пола на лицо 6»
                    # сходится только с ней. Отец Ивана (сын главы Ѳедоръ) в сказке не назван — умер до 1850 г.
                    member(20, person("Марья", "Авдѣева"), CensusRole.MOTHER, ref_member=17, age=43, comment="Ивана Федорова мать"),
                    # Отец Ивана — сын главы Ѳедоръ: «Ивана Полуектова внукъ Иванъ Ѳедоровъ» и «Ивана Ѳедорова
                    # мать Марья Авдѣева». В сказке его нет (умер до 9-й ревизии) — восстановлен.
                    member(21, person("Ѳедоръ"), None, ref_member=20, parent_member=1, hidden=True,
                           spouse_member=20,
                           comment="Отсутствует в РС 1857; восстановлен по отчеству внука Ивана и его матери Марье Авдѣевой")),
          ),
    *page("727об-729",
          household("35",
                    member(1, person("Алексѣй", "Никитинъ"), CensusRole.HEAD, age="55 года 5 мес", previous_age=48),
                    member(2, person("Кондратій"), CensusRole.SON, ref_member=1, age="23 года 6 мес", previous_age="16 лет 3 нед", comment="Алексея сын"),
                    member(3, person("Прасковья", "Николаева"), CensusRole.WIFE, ref_member=2, age=22, comment="Кондратия Алексеева жена"),
                    member(4, person("Анна"), CensusRole.DAUGHTER, ref_member=2, age=3, comment="Кондратия Алексеева его же дочь"),
                    member(5, person("Власъ"), CensusRole.SON, ref_member=1, age="22 года 5 мес", previous_age=15, comment="Алексея сын"),
                    member(6, person("Матрена", "Власова"), CensusRole.WIFE, ref_member=5, age=20, comment="Власа Алексеева жена"),
                    member(7, person("Савватей", "Никитинъ"), CensusRole.BROTHER, ref_member=1, age="43 года 11 мес", previous_age="36 лет 6 мес", comment="Алексея Никитина брат"),
                    member(8, person("Варвара", "Силантьева"), CensusRole.WIFE, ref_member=7, age=42, comment="Савватея Никитина вторая жена"),
                    member(9, person("Василій"), CensusRole.SON, ref_member=7, age="19 лет 5 мес", previous_age=12, comment="Савватея Никитина сын от первой жены"),
                    member(10, person("Татьяна", "Евстратова"), CensusRole.WIFE, ref_member=9, age=19, comment="Василия Савватеева жена"),
                    member(11, person("Леонтій"), CensusRole.SON, ref_member=7, age="14 лет 4 мес", previous_age="6 лет 11 мес", comment="Савватея Никитина сын от второй жены"),
                    member(12, person("Осипъ"), CensusRole.SON, ref_member=7, age=11, previous_age="3 года 7 мес", comment="Савватея Никитина сын от второй жены"),
                    # Пропущены при первом вводе; вписаны 05.10.2026 по скану (кадр 729, женская сторона):
                    # «его же дочери отъ второй жены: Марья — 6, Прасковья — 1 недѣли». Итог страницы
                    # «женскаго пола на лицо 9» сходится только с ними.
                    member(13, person("Марья"), CensusRole.DAUGHTER, ref_member=7, age=6, comment="Савватея Никитина дочь от второй жены"),
                    member(14, person("Прасковья"), CensusRole.DAUGHTER, ref_member=7, age="1 неделя", comment="Савватея Никитина дочь от второй жены")),
          ),
    record_day=6,
    record_month=Month.NOVEMBER,
    prev_revision_year=1850,
    defaults=RecordDefaults(
        status_male=GOSUDARSTVENNYJ_PEASANT_MALE,
        status_female=GOSUDARSTVENNYJ_PEASANT_FEMALE,
    ),
    # 05.10.2026: дворы сверены со сканом при чтении всей сказки (три пропуска и две цифры
    # исправлены), но ждут вычитки в Verso; на Geni остаются по храповику.
    reviewed=False,
)
