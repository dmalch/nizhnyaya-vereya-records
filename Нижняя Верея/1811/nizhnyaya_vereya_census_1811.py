from verso.ru.dsl import (CensusRole, Month, RecordDefaults, census_records, household, member,
                          page, person)
from verso.ru.dsl.statuses import ECON_PEASANT_FEMALE, ECON_PEASANT_MALE

# 6-я ревизия 1811 г., сказка № 87 «Экономическаго села Степанькова», поданная 12 сентября
# 1811 г. **ГАВО ф. 301 оп. 3 д. 161, лл. 279–288об** (сканы ЭЧЗ 0546–0565; скачано по
# абонементу 06.10.2026), двор 17 — л. 282.
#
# ⚠ Отдельной сказки д. Нижней Вереи 1811 г. в оцифрованных делах нет (оп. 3 дд. 128, 158 А,
# 161 просмотрены), а в 1795 г. деревни ещё не было: её **выселили изъ Степанькова в 1801 г.**
# Степаньковская сказка 1811 г. перечисляет выселенцев с пометой «вышли оного жъ вѣдомства въ
# деревню Нижнюю Верь 1801 года» — возраст у них только по 5-й ревизии 1795 г.
# Взяты ВСЕ дворы выселенцев 1801 г. — 1, 4, 5, 12, 17, 22, 25 (ветвь Якова), 27 (Анисимъ), 40 — и двор 18
# (Максимъ Абрамовъ, третий сынъ Абрама, ушёл въ купечество 1804). Сказка прочитана целиком 12.10.2026
# (50 дворов, итог 227 / 122); индекс прочих дворов — в `../ARCHIVES.md`.
#
# reviewed=False: двор 17 найден агентом и перечитан по скану; прочие прочитаны 12.10.2026 при ~1×, спорные цифры
# при 1.6×.

census = census_records(
    "ГАВО", "301", "3", "161", "Степаньково", 1811,
    *page("279",
          # [НВ] «Григорій Пантелеевъ 50; Григорьевы дѣти Алексѣй 26, Семіонъ 23, Максимъ 21; Григорьевъ же
          # племянникъ Авдей Ивановъ 21». РС-3 1762: Пантелей Ивановъ 56, сыновья Иванъ 19, Григорей 18 —
          # тот же двор. ⚑ Авдей Ивановъ (ок. 1774) — вероятный отец Ивана и Евсигнея Авдѣевыхъ ИР 1855 (дворъ 343)
          household("1",
                    member(1, person("Григорій", "Пантелеевъ"), CensusRole.HEAD, previous_age=50, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    member(2, person("Алексѣй"), CensusRole.SON, ref_member=1, previous_age=26, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    member(3, person("Семіонъ"), CensusRole.SON, ref_member=1, previous_age=23, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    member(4, person("Максимъ"), CensusRole.SON, ref_member=1, previous_age=21, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    member(5, person("Авдей", "Ивановъ"), CensusRole.NEPHEW, ref_member=1, parent_member=6, previous_age=21, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    member(6, person("Иванъ", "Пантелеевъ"), CensusRole.BROTHER, hidden=True,
                           comment="в сказке его нет; восстановлен по «Григорьевъ племянникъ Авдей Ивановъ»"),
                    ),
          ),
    *page("279об",
          # [НВ] «Ѳедора Никитина дѣти: Емельянъ 64…» — сам Ѳедоръ (РС-3 1762: 56 л.) умер до 1795 г.; Емельянъ
          # и Еремей — его сыновья (1762: Емельянъ 32, Ерема 14). Павелъ 26 написан с меньшим отступом, чем
          # Иванъ: чей он сын — Емельяна или Еремея, — по отступу не решается; поставлен сыном Емельяна по
          # порядку строк. ⚑ Павелъ, сынъ Павла, 1 (ок. 1794) — вероятно «Павелъ Павловъ 61» ИР 1855 (дворъ 335)
          household("4",
                    member(1, person("Емельянъ", "Ѳедоровъ"), CensusRole.HEAD, previous_age=64, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    member(2, person("Иванъ"), CensusRole.SON, ref_member=1, previous_age=36, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    member(3, person("Петръ"), CensusRole.SON, ref_member=2, previous_age=10, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    member(4, person("Григорій"), CensusRole.SON, ref_member=2, previous_age=6, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    member(5, person("Павелъ"), CensusRole.SON, ref_member=1, previous_age=26, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею", comment="отступ строки не говорит, чей он сын — Емельяна или Еремея"),
                    member(6, person("Павелъ"), CensusRole.SON, ref_member=5, previous_age=1, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    member(7, person("Еремей", "Ѳедоровъ"), CensusRole.BROTHER, ref_member=1, previous_age=49, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    member(8, person("Никита"), CensusRole.SON, ref_member=7, previous_age=29, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    member(9, person("Филиппъ"), CensusRole.SON, ref_member=7, previous_age=25, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    member(10, person("Иванъ"), CensusRole.SON, ref_member=7, previous_age=19, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    member(11, person("Иванъ"), CensusRole.SON, ref_member=7, previous_age=15, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею", comment="«Иванъ же»"),
                    ),
          # [НВ] «Степанъ Романовъ 55; Степана сынъ Пименъ 29». РС-3 1762: Романъ Никитинъ, сынъ Степанъ 23
          household("5",
                    member(1, person("Степанъ", "Романовъ"), CensusRole.HEAD, previous_age=55, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    member(2, person("Пименъ"), CensusRole.SON, ref_member=1, previous_age=29, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    ),
          ),
    *page("281",
          # [НВ] «Маркелъ Григорьевъ 52; его племянникъ Николай Яковлевъ 26; Николаевъ сынъ Никита 3»
          household("12",
                    member(1, person("Маркелъ", "Григорьевъ"), CensusRole.HEAD, previous_age=52, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    member(2, person("Николай", "Яковлевъ"), CensusRole.NEPHEW, ref_member=1, parent_member=4, previous_age=26, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    member(3, person("Никита"), CensusRole.SON, ref_member=2, previous_age=3, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    member(4, person("Яковъ", "Григорьевъ"), CensusRole.BROTHER, hidden=True,
                           comment="в сказке его нет; восстановлен по «его племянникъ Николай Яковлевъ»"),
                    ),
          ),
    *page("282",
          # 🏆 **ПОЛУЕКТЪ — ОТЕЦ ИВАНА ПОЛУЕКТОВА; ЕФИМЪ — ВЕРОЯТНЫЙ ОТЕЦ ИППОЛИТА ЕФИМОВА.**
          # «Абрамъ Дорофеевъ 65; Абрамовы дѣти: Полиектъ 45, Полиекта сынъ Иванъ 11; Ефимъ 34, Ефима
          # сынъ Иванъ 2; Абрама внукъ Пантелей Андреевъ 30 — вышли оного жъ вѣдомства въ деревню Нижнюю
          # Верь 1801 года». ⇒ Иванъ Полуектовъ (11 въ 1795 ⇒ ок. 1784; РС-10 1857 даёт ок. 1785 —
          # сходится) — сынъ Полуекта Абрамова. Ипполитъ Ефимовъ род. ок. 1804, уже въ НВ, и сказки НВ
          # нет ⇒ что его отецъ — этот Ефимъ Абрамовъ, **гипотеза**: другого Ефима среди выселенцевъ нет.
          # Тогда Полуектовичи и Ефимовичи — двоюродные (Гусевы обѣихъ линий — потомки Абрама Дорофеева).
          # 🔗 «Пантелей Андреевъ» — кумъ у дочери Ипполита Мавры въ 1834 г. (МК Степаньково, ж. № 23).
          household("17",
                    member(1, person("Абрамъ", "Дорофеевъ"), CensusRole.HEAD, previous_age=65,
                           departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    member(2, person("Полуектъ"), CensusRole.SON, ref_member=1, previous_age=45,
                           departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    member(3, person("Иванъ"), CensusRole.GRANDSON, ref_member=1, parent_member=2,
                           previous_age=11, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею",
                           comment="«Полиекта сынъ Иванъ»"),
                    member(4, person("Ефимъ"), CensusRole.SON, ref_member=1, previous_age=34,
                           departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    member(5, person("Иванъ"), CensusRole.GRANDSON, ref_member=1, parent_member=4,
                           previous_age=2, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею",
                           comment="«Ефима сынъ Иванъ»"),
                    member(6, person("Пантелей", "Андреевъ"), CensusRole.GRANDSON, ref_member=1, parent_member=7,
                           previous_age=30, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею",
                           comment="«Абрама внукъ Пантелей Андреевъ»"),
                    member(7, person("Андрей"), CensusRole.SON, ref_member=1, hidden=True,
                           comment="Отсутствует в РС-6; восстановлен по отчеству внука Пантелея Андреева"),
                    ),
          ),
    *page("282–282об",
          # 🆕 **ТРЕТИЙ СЫНЪ АБРАМА ДОРОФЕЕВА** (РС-3 1762: Максимъ 7 ⇒ ок. 1755; здесь 39 въ 1795 ⇒ ок. 1756).
          # Свой двор рядом с отцовским (17), но не въ НВ: «вышли въ Меленковское купечество 1804 года»
          household("18",
                    member(1, person("Максимъ", "Абрамовъ"), CensusRole.HEAD, previous_age=39, departure_year=1804, departure_reason="вышел в меленковское купечество"),
                    member(2, person("Андреянъ"), CensusRole.SON, ref_member=1, previous_age=17, departure_year=1804, departure_reason="вышел в меленковское купечество"),
                    member(3, person("Василій"), CensusRole.SON, ref_member=1, previous_age=14, departure_year=1804, departure_reason="вышел в меленковское купечество"),
                    member(4, person("Антонъ"), CensusRole.SON, ref_member=1, previous_age=5, departure_year=1804, departure_reason="вышел в меленковское купечество"),
                    member(5, person("Лаврентій"), CensusRole.SON, ref_member=1, previous_age=2, departure_year=1804, departure_reason="вышел в меленковское купечество"),
                    ),
          ),
    *page("283",
          # [НВ] «Никона Иванова дѣти: Иванъ 42; Ивана сынъ Ефремъ 12; Сидоръ 28; Яковъ 22». РС-3 1762: Никонъ
          # Ивановъ 27, сынъ Иванъ 10
          household("22",
                    member(1, person("Иванъ", "Никоновъ"), CensusRole.HEAD, previous_age=42, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею", comment="«Никона Иванова дѣти»"),
                    member(2, person("Ефремъ"), CensusRole.SON, ref_member=1, previous_age=12, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    member(3, person("Сидоръ", "Никоновъ"), CensusRole.BROTHER, ref_member=1, previous_age=28, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    member(4, person("Яковъ", "Никоновъ"), CensusRole.BROTHER, ref_member=1, previous_age=22, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    ),
          ),
    *page("283об",
          # Выселена въ НВ только ветвь Якова Осипова (скобка «вышли … въ деревню Нижнюю Верь 1801» против
          # Якова, Іона и Харитона); ветвь Семена осталась въ Степанковѣ
          household("25",
                    member(1, person("Семенъ", "Осиповъ"), CensusRole.HEAD, previous_age=53, departure_year=1809, departure_reason="умер", comment="«Осипа Григорьева дѣти»"),
                    member(2, person("Спиридонъ"), CensusRole.SON, ref_member=1, previous_age=23, departure_year=1802, departure_reason="умер"),
                    member(3, person("Кузма"), CensusRole.SON, ref_member=1, age=35, previous_age=19),
                    member(4, person("Левъ"), CensusRole.SON, ref_member=3, age=2),
                    member(5, person("Дмитрій"), CensusRole.SON, ref_member=1, age=28, previous_age=12),
                    member(6, person("Яковъ", "Осиповъ"), CensusRole.BROTHER, ref_member=1, previous_age=51, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    member(7, person("Іонъ"), CensusRole.SON, ref_member=6, previous_age=27, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    member(8, person("Харитонъ"), CensusRole.SON, ref_member=6, previous_age=13, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    # «Осипа внукъ Максима Осипова дѣти» — самого Максима в сказке нет
                    member(9, person("Максимъ", "Осиповъ"), CensusRole.BROTHER, hidden=True, comment="в сказке его нет; восстановлен по «Максима Осипова дѣти»"),
                    member(10, person("Григорій", "Максимовъ"), CensusRole.NEPHEW, ref_member=1, parent_member=9, previous_age=19, departure_year=1807, departure_reason="отдан в милицию"),
                    member(11, person("Осипъ", "Максимовъ"), CensusRole.NEPHEW, ref_member=1, parent_member=9, previous_age=17, departure_year=1807, departure_reason="умер"),
                    ),
          ),
    *page("283об–284",
          # Выселенъ въ НВ только Анисимъ (скобка против него). ⚑ Анисимъ Леонтьевъ (ок. 1769) — вероятный
          # отецъ «Емельяна Анисимова 56» ИР 1855 (дворъ 329)
          household("27",
                    member(1, person("Леонтій", "Андреевъ"), CensusRole.HEAD, age=70, previous_age=54, comment="«Андрея Леонтьева дѣти»"),
                    member(2, person("Наумъ"), CensusRole.SON, ref_member=1, age=45, previous_age=29),
                    member(3, person("Анисимъ"), CensusRole.SON, ref_member=1, previous_age=26, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    member(4, person("Терентій"), CensusRole.SON, ref_member=1, previous_age=21, departure_year=1807, departure_reason="отдан в милицию"),
                    member(5, person("Логинъ"), CensusRole.SON, ref_member=4, age=12),
                    member(6, person("Григорій"), CensusRole.SON, ref_member=4, age=10),
                    member(7, person("Никита"), CensusRole.SON, ref_member=1, previous_age=19, departure_year=1791, departure_reason="отдан в рекруты"),
                    member(8, person("Евстигней"), CensusRole.SON, ref_member=1, age=30, previous_age=14),
                    member(9, person("Титъ"), CensusRole.SON, ref_member=1, age=25, previous_age=9),
                    member(10, person("Архипъ", "Андреевъ"), CensusRole.BROTHER, ref_member=1, previous_age=52, departure_year=1806, departure_reason="умер"),
                    member(11, person("Петръ"), CensusRole.SON, ref_member=10, previous_age=17, departure_year=1808, departure_reason="умер"),
                    ),
          ),
    *page("287",
          # [НВ] «Ивана Васильева дѣти: Тихонъ 44, Елисей 39, Иванъ 31» — РС-3 1762: Василей Дмитріевъ 63, сынъ
          # Иванъ 44, внуки Тихонъ 12, Миней 9, Елисей 7, Иванъ 3. ⚑ **Степанъ, сынъ Ивана, 5 (ок. 1790)** —
          # вероятно «Степанъ Ивановъ вд. 65» ИР 1855 (дворъ 352), отецъ Харлампія Степанова; **Савелій, сынъ
          # Тихона, 3 (ок. 1792)** — вероятный отецъ Тихона и Ивана Савельевыхъ (ИР 1855, дворъ 332); **Іонъ 12**
          # — вероятный отецъ Петра и Василія Іоновыхъ (дворъ 327). Всё — по имени и возрасту, не доказано
          household("40",
                    member(1, person("Тихонъ", "Ивановъ"), CensusRole.HEAD, previous_age=44, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею", comment="«Ивана Васильева дѣти»"),
                    member(2, person("Андрей"), CensusRole.SON, ref_member=1, previous_age=22, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    member(3, person("Ефремъ"), CensusRole.SON, ref_member=2, previous_age='году', departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    member(4, person("Іонъ"), CensusRole.SON, ref_member=1, previous_age=12, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    member(5, person("Ѳролъ"), CensusRole.SON, ref_member=1, previous_age=5, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    member(6, person("Савелій"), CensusRole.SON, ref_member=1, previous_age=3, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    member(7, person("Елисей", "Ивановъ"), CensusRole.BROTHER, ref_member=1, previous_age=39, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    member(8, person("Иванъ"), CensusRole.SON, ref_member=7, previous_age=9, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    member(9, person("Иванъ", "Ивановъ"), CensusRole.BROTHER, ref_member=1, previous_age=31, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею", comment="РС-3 1762 даёт ему 3 ⇒ ждали бы 36"),
                    member(10, person("Степанъ"), CensusRole.SON, ref_member=9, previous_age=5, departure_year=1801, departure_reason="переселен в д. Нижнюю Верею"),
                    ),
          ),
    record_month=Month.SEPTEMBER,
    prev_revision_year=1795,
    defaults=RecordDefaults(status_male=ECON_PEASANT_MALE, status_female=ECON_PEASANT_FEMALE),
    reviewed=False,
)
