from verso.ru.dsl import Gender, Month, RecordDefaults, birth, birth_month, birth_records, page, person
from verso.ru.dsl.statuses import (ECON_PEASANT_LEGAL_WIFE, ECON_PEASANT_MALE, KAZENNYJ_PEASANT_FEMALE,
                                   KAZENNYJ_PEASANT_GIRL, KAZENNYJ_PEASANT_LEGAL_WIFE,
                                   KAZENNYJ_PEASANT_MALE, KAZENNYJ_PEASANT_WIFE, PRIEST, SOLDIER_WIFE,
                                   UNTER_OFFICER)

# Метрическая книга Успенской церкви с. ШИМОРСКОГО за 1859 г., часть первая — записи
# «Казеннаго вѣдомства деревни Нижней Верьи». **ГАВО ф. 590 оп. 5 д. 4, лл. 853–891об**
# (альбом «Шиморское 1859 (ГАВО 590-5-4)»; консисторская копия).
#
# Прочитана ВСЯ часть первая (лл. 853об–891об, ~385 записей), взяты ВСЕ 27 записей НВ (28
# младенцев: двойни № 86/87 ж). Деревню каждой записи («Нижней»/«Верхней») решали по зуму:
# писец пишет «казенной» и при Верхней Верьѣ, а Нижнюю трижды зоветъ «экономической».
#
# ⚠ Форма меняется внутри части: до л. 873об воспріемники — на обороте, в правой колонке; на
# recto — «Кто совершалъ таинство» и подписи. С л. 874об воспріемники уходят на recto.
# Крестили свящ. Стефанъ (Яковлевъ) Свавицкій (так пишет книга; в ИР 1855 — «Савицкій») и
# іерей Андрей Н. Половодовъ? / Полисадовъ? (росчерк); причт в DSL не вынесен.
#
# reviewed=False: часть прочитана тремя агентами при 2.4×, имена — при 4–8×, НЕ сверено
# человеком; «?» и альтернативы — в комментариях. Итоги месяцев: апрель 13 м / 20 ж, май 19/19,
# июнь 19/13, июль 12/28, август 18/9, сентябрь 14/15, октябрь 9/19, ноябрь 16/11; общего итога нет.

DEFAULTS = RecordDefaults(residence="Нижняя Верея", status_male=KAZENNYJ_PEASANT_MALE,
                          status_female=KAZENNYJ_PEASANT_FEMALE, status_mother=KAZENNYJ_PEASANT_LEGAL_WIFE)

nizhnyaya_vereya_births_1859 = birth_records(
    "ГАВО", "590", "5", "4", "Нижняя Верея", "Успенская",
    1859,
    *page("854об",
          *birth_month(Month.JANUARY,
                       # Кумъ — «Ва?силій Григорьевъ», кума — «жена Е[ли]?завета Ксенофонтова» (разрыв бумаги):
                       # по РС-10 1857 — сестра отца, жена Ерѳима Харлампіева (двор 29)
                       birth(12, Gender.MALE, 3, 4,
                             child=person("Григорій"),
                             father=person("Димитрій", "Ксенофонтовъ"),
                             mother=person("Ѳеврония", "Афонасьева"),
                             god_parent1=person("Василій", "Григорьевъ"),
                             god_parent2=person("Елизавета", "Ксенофонтова", status=KAZENNYJ_PEASANT_WIFE)),
                       ),
          ),
    *page("855об",
          *birth_month(Month.JANUARY,
                       # Мать «Мавра Анисимова?»; кумъ «Деревни Сам…? крестьянинъ Яковъ Анисимовъ? (Акимовъ?)»
                       # — деревня не прочитана, оставлена НВ по умолчанию; кума «Сем[ена]? Доронина жена
                       # Матрона Іовлева» (по отчеству — сестра отца)
                       birth(9, Gender.FEMALE, 6, 6,
                             child=person("Марья"),
                             father=person("Дорофей", "Іовлевъ"),
                             mother=person("Мавра", "Анисимова"),
                             god_parent1=person("Яковъ", "Анисимовъ"),
                             god_parent2=person("Матрона", "Іовлева", status=KAZENNYJ_PEASANT_WIFE)),
                       # «Онаго же Вѣдомства и деревни» — по № 9. Кума «дѣвица Ульяна? Степанова»
                       birth(10, Gender.FEMALE, 6, 6,
                             child=person("Мелания"),
                             father=person("Макаръ", "Степановъ"),
                             mother=person("Аксинья", "Ильева"),
                             god_parent1=person("Парамонъ", "Степановъ"),
                             god_parent2=person("Ульяна", "Степанова", status=KAZENNYJ_PEASANT_GIRL)),
                       ),
          ),
    *page("857об",
          *birth_month(Month.JANUARY,
                       # 🔴 Прямая линия Ефимовичей (Ипполитъ → Семёнъ). Мать при 4× — «Прасковья Герасимова»;
                       # в указателе РС-10 1857 (чтение агента, не сверено) жена Семёна — «Прасковья
                       # Ермоніева» 25 ⇒ перечитать сказку. Кумъ «Унтеръ Офицеръ Антонъ Васильевъ Пуловъ?»
                       birth(18, Gender.FEMALE, 17, 17,
                             child=person("Ксенія"),
                             father=person("Семенъ", "Ипполитовъ"),
                             mother=person("Прасковья", "Герасимова"),
                             god_parent1=person("Антонъ", "Васильевъ", "Пуловъ", status=UNTER_OFFICER),
                             god_parent2=person("Прасковья", "Григорьева", status=KAZENNYJ_PEASANT_GIRL)),
                       # «Онагоже вѣдомства и деревни» — по № 18 ж
                       birth(21, Gender.MALE, 17, 18,
                             child=person("Григорій"),
                             father=person("Герасимъ", "Ивановъ"),
                             mother=person("Наталья", "Иванова"),
                             god_parent1=person("Ѳедоръ", "Ивановъ"),
                             god_parent2=person("Татіана", "Герасимова", status=SOLDIER_WIFE)),
                       ),
          ),
    *page("858об",
          *birth_month(Month.JANUARY,
                       # 🔴 Ефимовичи: Григорій Ипполитовъ (РС-10 двор 17). Имя матери не прочитано —
                       # перенос «Ки|та»; отчество «Димитріева»
                       birth(24, Gender.MALE, 21, 22,
                             child=person("Іоаннъ"),
                             father=person("Григорій", "Ипполитовъ"),
                             mother=person("?", "Димитріева"),
                             god_parent1=person("Матвѣй", "Андреевъ"),
                             god_parent2=person("Прасковья", "Григорьева", status=KAZENNYJ_PEASANT_GIRL)),
                       ),
          ),
    *page("859об",
          *birth_month(Month.JANUARY,
                       # «Экономической деревни Нижней Верьи крестьянинъ Николай Ла…симигѣевъ?» — отчество
                       # не прочитано; мать «Е…фрья (Евфросинія?) Іоакимова»; кума «дѣвица Наталья Лари…тіева?»
                       # (не вынесена). Крестилъ іерей Андрей
                       birth(25, Gender.FEMALE, 28, 29,
                             child=person("Анна"),
                             father=person("Николай", status=ECON_PEASANT_MALE),
                             mother=person("Евфросинія", "Іоакимова", status=ECON_PEASANT_LEGAL_WIFE),
                             god_parent1=person("Димитрій", "Маркинъ")),
                       ),
          *birth_month(Month.FEBRUARY,
                       # Мать «Дарья Авивова?»; воспріемники — «Священникъ Савицкій съ Вур…инской? дѣвицей
                       # Натальей Ав[ив]овой?» (вторая не вынесена: фамилия не прочитана)
                       birth(28, Gender.FEMALE, 2, 5,
                             child=person("Анна"),
                             father=person("Иванъ", "Трофимовъ"),
                             mother=person("Дарья", "Авивова"),
                             god_parent1=person("Стефанъ", last_name_orig="Савицкій", residence="Шиморское", status=PRIEST)),
                       ),
          ),
    *page("860об",
          *birth_month(Month.FEBRUARY,
                       # Отец — Евѳимъ Евстигнѣевъ (РС-10 двор 15: «Ерѳимъ», жена Екатерина Иванова, дочь
                       # Евдокія 3 мѣс в 1857 — та умерла?); книга пишет «Ефимъ Евсигнѣевъ»
                       birth(34, Gender.FEMALE, 12, 13,
                             child=person("Евдокія"),
                             father=person("Ефимъ", "Евсигнѣевъ"),
                             mother=person("Екатерина", "Иванова"),
                             god_parent1=person("Григорій", "Максимовъ"),
                             god_parent2=person("Анастасія", "Герасимова", status=KAZENNYJ_PEASANT_WIFE)),
                       ),
          ),
    *page("861об",
          *birth_month(Month.FEBRUARY,
                       # «Онагоже вѣдомства» — по № 43 ж («Экономическаго вѣдомства» Верхней Верьи), деревня
                       # названа прямо. Кумъ — «Тогоже семейства крестьянинъ Андрей» (без отчества: братъ
                       # отца?), кума «дѣвица Елена Никитина» — сестра отца (РС-10 двор 15? «Никиты дочь
                       # Елена 15»)
                       birth(44, Gender.FEMALE, 24, 25,
                             child=person("Евдокія"),
                             father=person("Ѳедоръ", "Никитинъ", "Мудриловъ"),
                             mother=person("Агафья", "Игнатова"),
                             god_parent1=person("Андрей", "Никитинъ"),
                             god_parent2=person("Елена", "Никитина", status=KAZENNYJ_PEASANT_GIRL)),
                       ),
          ),
    *page("863об",
          *birth_month(Month.MARCH,
                       # «Экономическаго вѣдомства деревни Нижней Верьи». Мать «Аку[ли]на? Тарасова»; кумъ
                       # «Деревни Конкова? крестьянинъ Максимъ Тарасовъ» (по отчеству — братъ матери; Конново
                       # Степаньковского прихода?), кума «Нижней Вер[ьи] дѣвица Наталья Харитонова?
                       # (Ларионова?)». Крестилъ іерей Андрей
                       birth(47, Gender.MALE, 25, 26,
                             child=person("Іоаннъ"),
                             father=person("Павелъ", "Алексѣевъ", status=ECON_PEASANT_MALE),
                             mother=person("Акулина", "Тарасова", status=ECON_PEASANT_LEGAL_WIFE),
                             god_parent1=person("Максимъ", "Тарасовъ", residence="Конново"),
                             god_parent2=person("Наталья", "Харитонова", status=KAZENNYJ_PEASANT_GIRL)),
                       ),
          ),
    *page("864об",
          *birth_month(Month.APRIL,
                       # Кумъ — «Ученикъ Стефанъ Успенскій» (причетникъ Шиморского), кума «дѣв?кой
                       # Евфросиньей Алексѣевой»
                       birth(59, Gender.FEMALE, 5, 6,
                             child=person("Марья"),
                             father=person("Алексѣй", "Емельяновъ"),
                             mother=person("Матрона", "Павлова"),
                             god_parent1=person("Стефанъ", last_name_orig="Успенскій", residence="Шиморское", status="ученик"),
                             god_parent2=person("Евфросинья", "Алексѣева", status=KAZENNYJ_PEASANT_GIRL)),
                       # Кума «вдова? Матрона Ксенофонтова» (жена Осипа Симонова в РС-10, двор 25)
                       birth(51, Gender.MALE, 6, 7,
                             child=person("Ѳедоръ"),
                             father=person("Иванъ", "Ѳедоровъ"),
                             mother=person("Мавра", "Димитріева"),
                             god_parent1=person("Димитрій", "Ксенофонтовъ"),
                             god_parent2=person("Матрона", "Ксенофонтова")),
                       # Мать «Дарья Ѳомина?»; кумъ «Парамонъ? Степановъ»
                       birth(52, Gender.MALE, 7, 8,
                             child=person("Ѳедоръ"),
                             father=person("Филимонъ", "Евсигнѣевъ"),
                             mother=person("Дарья", "Ѳомина"),
                             god_parent1=person("Парамонъ", "Степановъ"),
                             god_parent2=person("Анна", "Емельянова", status=KAZENNYJ_PEASANT_WIFE)),
                       ),
          ),
    *page("866об",
          *birth_month(Month.APRIL,
                       # «Тогоже вѣдомства» — по № 75 ж «Экономическаго вѣдомства деревни Верхней Верьи»,
                       # деревня названа прямо. Отец — «Никита Іосифовъ» (вычитано владельцемъ 07.11.2026; прежде
                       # «Ипатъ»): РС-10 1857 двор 32 — Никита Осиповъ, жена Ефимья Никитина; погреб. № 57 ж —
                       # его дочь Александра. Мать «Евфро|сія? (Евфросинія?) Никитина» — по РС-10, быть можетъ,
                       # Евфимія; кумъ «Никонъ? (Нилонъ?) Никитинъ»
                       birth(76, Gender.FEMALE, 28, 30,
                             child=person("Ирина"),
                             father=person("Никита", "Іосифовъ", status=ECON_PEASANT_MALE),
                             mother=person("Евфросинія", "Никитина", status=ECON_PEASANT_LEGAL_WIFE),
                             god_parent1=person("Никонъ", "Никитинъ"),
                             god_parent2=person("Агафья", "Григорьева", status=KAZENNYJ_PEASANT_GIRL)),
                       # «Тогоже вѣдомства и деревни». Отец «Гавріилъ Хламовъ? (Халамовъ?)» — прозвание не
                       # отчество, в DSL не вынесено; мать «Соломонія Евсигнѣева?»; кумъ «Парамонъ? Степановъ»
                       birth(61, Gender.MALE, 28, 30,
                             child=person("Іоаннъ"),
                             father=person("Гавріилъ"),
                             mother=person("Соломонія", "Евсигнѣева"),
                             god_parent1=person("Парамонъ", "Степановъ"),
                             god_parent2=person("Анна", "Трофимова", status=KAZENNYJ_PEASANT_GIRL)),
                       ),
          ),
    *page("867об",
          *birth_month(Month.MAY,
                       # Мать «Е…|фанида? Евсигнѣева» — начало имени надстрочно (Епифанида? Ѳеофанида?)
                       birth(82, Gender.FEMALE, 2, 4,
                             child=person("Пелагія"),
                             father=person("Василій", "Никитинъ"),
                             mother=person("?", "Евсигнѣева"),
                             god_parent1=person("Петръ", "Корниловъ"),
                             god_parent2=person("Матрона", "Никитина", status=KAZENNYJ_PEASANT_WIFE)),
                       ),
          ),
    *page("868об",
          *birth_month(Month.MAY,
                       # Двойни. Отец «Андрей … Калининъ?» (отчество/фамилия переписаны жирнее), мать
                       # «Акилина Ипполитова?» — по отчеству дочь Ипполита Ефимова (кума 1839 г.). Воспріемники
                       # на обеих: «Унтеръ-Офицеръ Іоаннъ? (Іона?) Алексѣевъ, дѣвица Прасковья Григорьева и жена
                       # Ирина Агафонова»
                       birth(86, Gender.FEMALE, 15, 17,
                             child=person("Елена"),
                             father=person("Андрей", last_name_orig="Калининъ"),
                             mother=person("Акилина", "Ипполитова"),
                             god_parent1=person("Іона", "Алексѣевъ", status=UNTER_OFFICER),
                             god_parent2=person("Прасковья", "Григорьева", status=KAZENNYJ_PEASANT_GIRL),
                             god_parent3=person("Ирина", "Агафонова", status=KAZENNYJ_PEASANT_WIFE)),
                       birth(87, Gender.FEMALE, 15, 17,
                             child=person("Ѳеодосія"),
                             father=person("Андрей", last_name_orig="Калининъ"),
                             mother=person("Акилина", "Ипполитова"),
                             god_parent1=person("Іона", "Алексѣевъ", status=UNTER_OFFICER),
                             god_parent2=person("Прасковья", "Григорьева", status=KAZENNYJ_PEASANT_GIRL),
                             god_parent3=person("Ирина", "Агафонова", status=KAZENNYJ_PEASANT_WIFE)),
                       # «Мудриловъ?» — РС-10 1857 двор 15 «Мудриновъ(?)»
                       birth(89, Gender.FEMALE, 20, 21,
                             child=person("Ѳеодосія"),
                             father=person("Константинъ", "Ивановъ", "Мудриловъ"),
                             mother=person("Анна", "Родіонова"),
                             god_parent1=person("Савватій", "Макаровъ"),
                             god_parent2=person("Авдотья", "Митрофанова", status=KAZENNYJ_PEASANT_WIFE)),
                       ),
          ),
    *page("870об",
          *birth_month(Month.JUNE,
                       # Отец «Варѳоломей Ма…ровъ» — «Макаровъ» (вычитано владельцемъ 07.11.2026; прежде
                       # «Митровъ»): погреб. № 92 м и № 97 м, РС-10 двор 41. Кумъ — «Ученикъ Высшаго отд.
                       # Семинаріи Николай Свавицкій» (сынъ священника?)
                       birth(86, Gender.MALE, 12, 14,
                             child=person("Петръ"),
                             father=person("Варѳоломей", "Макаровъ"),
                             mother=person("Анисья", "Дмитріева"),
                             god_parent1=person("Николай", last_name_orig="Свавицкій", residence="Шиморское", status="ученик высшего отделения семинарии"),
                             god_parent2=person("Прасковья", "Игнатова", status=KAZENNYJ_PEASANT_GIRL)),
                       ),
          ),
    *page("872об",
          *birth_month(Month.JUNE,
                       # Отец «Григорій Калининъ?» — РС-10 двор 13 (Калинникъ Пименовъ); его жена Ирина
                       # Агафонова — кума двойнят № 86/87
                       birth(93, Gender.MALE, 21, 23,
                             child=person("Петръ"),
                             father=person("Григорій", "Калининъ"),
                             mother=person("Ирина", "Агафонова"),
                             god_parent1=person("Іона", "Алексѣевъ", status=UNTER_OFFICER),
                             god_parent2=person("Марья", "Васильева", status=KAZENNYJ_PEASANT_GIRL)),
                       # Отец «Степанъ Ми-|левъ» — буквы «х» нѣтъ (вычитано владельцемъ 07.11.2026; прежде
                       # «Михѣевъ»). Вписано «Мильевъ» (Милій) — ближайшее извѣстное отчество
                       birth(98, Gender.MALE, 28, 29,
                             child=person("Павелъ"),
                             father=person("Степанъ", "Мильевъ"),
                             mother=person("Мавра", "Титова"),
                             god_parent1=person("Кононъ", "Ѳедотовъ"),
                             god_parent2=person("Татіана", "Иванова", status=KAZENNYJ_PEASANT_GIRL)),
                       ),
          ),
    *page("873об",
          *birth_month(Month.JULY,
                       # РС-10 1857 двор 11: Иванъ Денисовъ, жена Лукерья Семенова. Кума одна — «Оной же деревни
                       # жена Ѳеоро|нія? (Ѳевронія?) Егорова». Крестилъ іерей Андрей
                       birth(113, Gender.FEMALE, 2, 5,
                             child=person("Ольга"),
                             father=person("Иванъ", "Денисовъ"),
                             mother=person("Лукерья", "Семенова"),
                             god_parent1=person("Ѳевронія", "Егорова", status=KAZENNYJ_PEASANT_WIFE)),
                       ),
          ),
    *page("883об",
          *birth_month(Month.OCTOBER,
                       # Воспріемники на recto л. 884
                       birth(145, Gender.MALE, 15, 17,
                             child=person("Іоаннъ"),
                             father=person("Василій", "Ананьевъ"),
                             mother=person("Прасковья", "Маркова"),
                             god_parent1=person("Ефимъ", "Евсигнѣевъ"),
                             god_parent2=person("Марья", "Маркина", status=KAZENNYJ_PEASANT_GIRL)),
                       ),
          ),
    *page("884об",
          *birth_month(Month.OCTOBER,
                       # Имя младенца сокращено «Матрон.»; отчество матери не написано. Воспріемники (recto
                       # л. 885): «Тойже деревни крестьянинъ Гав-|лактій Макаровъ и женка Анастасія» — кумъ
                       # Галактіонъ (вычитано владельцемъ 07.11.2026; прежде «?»)
                       birth(174, Gender.FEMALE, 30, 1, k_month=Month.NOVEMBER,
                             child=person("Матрона"),
                             father=person("Макаръ", "Ивановъ"),
                             mother=person("Мавра"),
                             god_parent1=person("Галактіонъ", "Макаровъ"),
                             god_parent2=person("Анастасія", status=KAZENNYJ_PEASANT_WIFE)),
                       ),
          ),
    *page("886об",
          *birth_month(Month.NOVEMBER,
                       # Воспріемники (recto л. 887): «Иванъ Ѳедоровъ и женка Елисавета Венедиктова?»
                       birth(161, Gender.MALE, 8, 11,
                             child=person("Ѳеодоръ"),
                             father=person("Семенъ", "Трофимовъ"),
                             mother=person("Анастасья", "Кондратьева"),
                             god_parent1=person("Иванъ", "Ѳедоровъ"),
                             god_parent2=person("Елисавета", "Венедиктова", status=KAZENNYJ_PEASANT_WIFE)),
                       ),
          ),
    *page("890об",
          *birth_month(Month.DECEMBER,
                       # Мать «Ульяна Авивова», кума (recto л. 891) «дѣвка Наталья Авивова» — вычитано владельцемъ
                       # 07.11.2026 (прежде «Акимова» у обеих). Тѣ же Авивовы въ № 28 ж (л. 859об: мать Дарья, кума
                       # Наталья) — вероятно сестры. Крещена 25-го (последняя цифра неясна)
                       birth(197, Gender.FEMALE, 22, 25,
                             child=person("Анастасія"),
                             father=person("Емельянъ", "Мироновъ"),
                             mother=person("Ульяна", "Авивова"),
                             god_parent1=person("Ѳедоръ", "Ивановъ"),
                             god_parent2=person("Наталья", "Авивова", status=KAZENNYJ_PEASANT_GIRL)),
                       ),
          ),
    defaults=DEFAULTS,
    reviewed=False,
)
