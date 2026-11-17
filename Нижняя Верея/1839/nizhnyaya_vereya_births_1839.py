from verso.ru.dsl import (Gender, Month, RecordDefaults, birth, birth_month, birth_records, page,
                          person)
from verso.ru.dsl.statuses import (KAZENNYJ_PEASANT_FEMALE, KAZENNYJ_PEASANT_LEGAL_WIFE,
                                   KAZENNYJ_PEASANT_MAIDEN, KAZENNYJ_PEASANT_MALE,
                                   KAZENNYJ_PEASANT_WIDOW, PEASANT_MALE, SOLDIER_WIFE)

# Метрическая книга Успенской церкви с. ШИМОРСКОГО за 1839 г., часть первая — записи
# «Казеннаго вѣдомства деревни Нижней Верьи». **ГАВО ф. 556 оп. 106 д. 635, лл. 460об–489об**
# (альбом «Шиморское 1839 (ГАВО 556-106-635)»). Итог книги: родилось 147 м / 140 ж.
#
# ⚠ Часть первая ПОДШИТА НЕ ПО ПОРЯДКУ: лл. 460об–468об — январь–апрель, лл. 478об–489об —
# май–октябрь, лл. 469об–477об — октябрь–декабрь. Номер записи и месяц — по счёту книги.
#
# Прочитана ВСЯ часть первая, взяты ВСЕ четырнадцать записей НВ (не только прямые линии).
# Чего в году НЕТ: рождений Леонтія Савватеева (по погребению 1919 г. ок. 1839), Власа
# Алексѣева, Іоны и сыновей Савватея Никитина вообще.
#
# reviewed=False: прочитано при 1.3–2.4×, спорные слова — при 3–4×; спорное — в комментариях.

DEFAULTS = RecordDefaults(residence="Нижняя Верея", status_male=KAZENNYJ_PEASANT_MALE,
                          status_female=KAZENNYJ_PEASANT_FEMALE, status_mother=KAZENNYJ_PEASANT_LEGAL_WIFE)

nizhnyaya_vereya_births_1839 = birth_records(
    "ГАВО", "556", "106", "635", "Нижняя Верея", "Успенская",
    1839,
    *page("461об",
          *birth_month(Month.JANUARY,
                       # Кумъ — «Онагожъ вѣдомства деревни Высокова крестьянинъ Константинъ Дементьевъ» (по
                       # отчеству — родня матери); кума «Нижней Верьи Салдатка Надежда Абрамова» — фамилия на
                       # строке под краем кропа, перечитать
                       birth(6, Gender.MALE, 6, 11,
                             child=person("Ермилъ"),
                             father=person("Харлампій", "Степановъ"),
                             mother=person("Авдотья", "Дементьева"),
                             god_parent1=person("Константинъ", "Дементьевъ", residence="Высоково"),
                             god_parent2=person("Надежда", "Абрамова", status=SOLDIER_WIFE)),
                       ),
          ),
    *page("462об",
          *birth_month(Month.JANUARY,
                       birth(11, Gender.MALE, 14, 15,
                             child=person("Ефимъ"),
                             father=person("Евсигней", "Павловъ"),
                             mother=person("Анна", "Емельянова"),
                             god_parent1=person("Алексѣй", "Емельяновъ"),
                             god_parent2=person("Агафья", "Евсигнѣева", status=KAZENNYJ_PEASANT_MAIDEN)),
                       ),
          ),
    *page("465об",
          *birth_month(Month.FEBRUARY,
                       # ⚠ Кумъ «Оной же деревни крестьянинъ …» — имя не прочитано и не вынесено; кума «Марѳа
                       # Ананьина» стоит после слова «и …ка» (дѣвка? жинка?) — она же кума в № 39 м
                       birth(24, Gender.MALE, 19, 21,
                             child=person("Василій"),
                             father=person("Ананій", "Семеновъ"),
                             mother=person("Матрона", "Андреева"),
                             god_parent2=person("Марѳа", "Ананьина")),
                       ),
          ),
    *page("466об",
          *birth_month(Month.FEBRUARY,
                       # Отец — «Ѳедотъ Ѳедоровъ» (первым чтением было «Никита»; исправлено 12.10.2026 по ИР 1855,
                       # двор 355: «Ѳедотъ Ѳедоровъ 43, жена его 2-го брака Наталья Иванова», сынъ Кононъ 15) ⇒
                       # Авдотья Кирилова — его первая жена
                       birth(32, Gender.MALE, 28, 28,
                             child=person("Кононъ"),
                             father=person("Ѳедотъ", "Ѳедоровъ"),
                             mother=person("Авдотья", "Кирилова"),
                             god_parent1=person("Онисифоръ", "Семеновъ"),
                             god_parent2=person("Прасковья", "Егорова", status=KAZENNYJ_PEASANT_WIDOW)),
                       ),
          ),
    *page("467об",
          *birth_month(Month.MARCH,
                       # ⚠ Имя отца — «Авивъ» по чтению при 4×, перечитать. «Гуровъ» — отчество (ср. «Иванъ
                       # Гуровъ» МК 1837, № 14 м). Кума «деревни Верьи дѣвица» — какой Верьи, не сказано
                       birth(35, Gender.FEMALE, 9, 13,
                             child=person("Дарья"),
                             father=person("Авивъ", "Гуровъ"),
                             mother=person("Анна", "Иванова"),
                             god_parent1=person("Митрофанъ", "Макаровъ", status=PEASANT_MALE, residence="Шиморское"),
                             god_parent2=person("Дарья", "Иванова", status=KAZENNYJ_PEASANT_MAIDEN)),
                       # Кума «Марѳа Ананьина» после «и …ка», как в № 24 м
                       birth(39, Gender.MALE, 23, 30,
                             child=person("Иванъ"),
                             father=person("Емельянъ", "Яковлевъ"),
                             mother=person("Ѳекла", "Ананьина"),
                             god_parent1=person("Ананій", "Семеновъ"),
                             god_parent2=person("Марѳа", "Ананьина")),
                       ),
          ),
    *page("481об",
          *birth_month(Month.JUNE,
                       # ⚠ Имя матери — «Наталья» или «Настасья», и кумъ «Севастьянъ? Никифоровъ» — оба
                       # перечитать вычиткой
                       birth(73, Gender.FEMALE, 28, 30,
                             child=person("Марѳа"),
                             father=person("Никифоръ", "Ивановъ"),
                             mother=person("Наталья", "Ильина"),
                             god_parent1=person("Севастьянъ", "Никифоровъ"),
                             god_parent2=person("Евфимія", "Никитина", status=KAZENNYJ_PEASANT_MAIDEN)),
                       ),
          ),
    *page("483об",
          *birth_month(Month.JULY,
                       # Кумъ — Харлампій Степановъ, отец Ермила (№ 6 м); та же пара родителей крестит дочь
                       # Анну в 1837 г. (№ 14 ж)
                       birth(83, Gender.FEMALE, 29, 30,
                             child=person("Марья"),
                             father=person("Марко", "Ивановъ"),
                             mother=person("Ксенія", "Степанова"),
                             god_parent1=person("Харлампій", "Степановъ"),
                             god_parent2=person("Дарья", "Иванова", status=KAZENNYJ_PEASANT_MAIDEN)),
                       ),
          ),
    *page("485об",
          *birth_month(Month.AUGUST,
                       # ⚠ Имя в графе написано «(Анна)», а под ним ещё слово на «Е…» — правка писца или
                       # двойное имя, не решено. Мать — «Надежда Яковлева», как в 1837 г. (№ 100 ж)
                       birth(89, Gender.FEMALE, 25, 25,
                             child=person("Анна"),
                             father=person("Василій", "Григорьевъ"),
                             mother=person("Надежда", "Яковлева"),
                             god_parent1=person("Мина", "Абрамовъ"),
                             god_parent2=person("Анна", "Силина", status=KAZENNYJ_PEASANT_MAIDEN)),
                       # 🏆 **ДОЧЬ КСЕНОФОНТА ИВАНОВА** (двор 18 РС-10, ветвь Полуектовичей Гусевых), которой РС-10
                       # 1857 г. не знает. Кумъ — **Григорій Ипполитовъ** (двор 17, Ефимовичи): ещё одно кумовство
                       # двух линий Гусевых, как Ипполитъ Ефимовъ у Дмитрія Ксенофонтова в 1836 г. ⚠ Кума
                       # «**Акилина Ипполитова**» стоит после «и …на» (жена? дѣвица?). По отчеству — сестра
                       # Григорія, дочь Ипполита Ефимова, которой корпус не знает: жена Григорія по РС-10 —
                       # Улита Дмитріева
                       birth(92, Gender.FEMALE, 30, 31,
                             child=person("Елисавета"),
                             father=person("Ксенофонтъ", "Ивановъ"),
                             mother=person("Соломія", "Максимова"),
                             god_parent1=person("Григорій", "Ипполитовъ"),
                             god_parent2=person("Акилина", "Ипполитова")),
                       ),
          ),
    *page("489об",
          *birth_month(Month.OCTOBER,
                       # 🔴 «Силанъ Аврамовъ» — тот же отец, что в 1837 г. (№ 142 м), но жена там «Ксенія
                       # Корнильева», здесь «Ирина Корнилова». **Кандидат в отцы Варвары Силантьевой**, второй
                       # жены Савватея Никитина (РС-10, двор 35), — она солдатка уже в 1839 г. (ч. 3 № 1 м). ⚠
                       # Кума «Дарья А…рова/Аврамова» — фамилию перечитать
                       birth(107, Gender.FEMALE, 4, 6,
                             child=person("Аѳанасія"),
                             father=person("Силанъ", "Аврамовъ"),
                             mother=person("Ирина", "Корнилова"),
                             god_parent1=person("Василій", "Григорьевъ"),
                             god_parent2=person("Дарья", "Аврамова", status=KAZENNYJ_PEASANT_MAIDEN)),
                       ),
          ),
    *page("469об",
          *birth_month(Month.OCTOBER,
                       # ⚠ Отчество матери («Ирина Се…ова/Осипова») не прочитано
                       birth(107, Gender.MALE, 8, 9,
                             child=person("Ефимъ"),
                             father=person("Елисѣй", "Ивановъ"),
                             mother=person("Ирина"),
                             god_parent1=person("Макарій", "Кириловъ"),
                             god_parent2=person("Улита", "Иванова", status=KAZENNYJ_PEASANT_MAIDEN)),
                       ),
          ),
    *page("470об",
          *birth_month(Month.OCTOBER,
                       # Одна кума: «Онагожъ вѣдомства и деревни дѣвица Мавра Емельянова»
                       birth(116, Gender.FEMALE, 17, 19,
                             child=person("Неонила"),
                             father=person("Алексѣй", "Емельяновъ"),
                             mother=person("Матрона", "Павлова"),
                             god_parent2=person("Мавра", "Емельянова", status=KAZENNYJ_PEASANT_MAIDEN)),
                       ),
          ),
    *page("472об",
          *birth_month(Month.OCTOBER,
                       # Отец — «Иванъ Авдѣевъ» (первым чтением было «Андреевъ»; исправлено 12.10.2026 по ИР 1855,
                       # двор 343: «Иванъ Авдѣевъ 44, жена его Наталья Яковлева 43»)
                       birth(120, Gender.MALE, 30, 31,
                             child=person("Павелъ"),
                             father=person("Иванъ", "Авдѣевъ"),
                             mother=person("Наталья", "Яковлева"),
                             god_parent1=person("Иванъ", "Савельевъ"),
                             god_parent2=person("Марья", "Андреева", status=KAZENNYJ_PEASANT_WIDOW)),
                       ),
          ),
    defaults=DEFAULTS,
    reviewed=False,
)
