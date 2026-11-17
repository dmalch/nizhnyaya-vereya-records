from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import WHOOPING_COUGH
from verso.ru.dsl.statuses import (ECON_PEASANT_MALE, KAZENNYJ_PEASANT_FEMALE, KAZENNYJ_PEASANT_MALE,
                                   KAZENNYJ_PEASANT_WIDOW)

# Метрическая книга Успенской церкви с. ШИМОРСКОГО за 1859 г., часть третья — погребения
# «Казеннаго вѣдомства деревни Нижней Верьи». **ГАВО ф. 590 оп. 5 д. 4, лл. 931об–957об**
# (с вставным л. 954а; альбом «Шиморское 1859 (ГАВО 590-5-4)»). Итог книги (л. 957об): умерло
# 122 м / 128 ж, изъ нихъ «отъ коклюша» 91 / 94 — годъ коклюшной эпидеміи; родилось 143 / 138.
#
# Прочитана вся часть третья, взяты все 14 записей НВ (15 умершихъ, двойни № 59/60 ж).
# Вѣдомство писецъ пишетъ то «Казенной», то «Экономической» — у одного отца (Варѳоломей
# Макаровъ, № 92 м и № 97 м) и то и другое. Не вынесено: № 107 ж (6/9 окт., «Экономическаго
# вѣдомства крестьянина Якова Пахомова? дочь Марѳа», 3 г.) — деревня не названа, предыдущая
# запись — Верхняя Верья.
#
# Шесть погребеній — младенцы, чьи рожденія записаны въ ч. 1 этой же книги
# (`nizhnyaya_vereya_births_1859.py`): № 54 ж ← рожд. № 28 ж, № 59/60 ж ← № 86/87 ж, № 61 ж ← № 89 ж,
# № 92 м ← № 86 м (?), № 105 м — сынъ Емельяна Миронова (рожд. 1858?).
#
# reviewed=False: часть прочитана агентомъ при 2.4×, имена и лета — при 4–8×, НЕ сверено
# человекомъ; двойни № 59/60 перечитаны по скану (агентъ читалъ «Кашнина … Анна»).

DEFAULTS = RecordDefaults(residence="Нижняя Верея", status_male=KAZENNYJ_PEASANT_MALE,
                          status_female=KAZENNYJ_PEASANT_FEMALE)

nizhnyaya_vereya_deaths_1859 = death_records(
    "ГАВО", "590", "5", "4", "Нижняя Верея", "Успенская",
    1859,
    *page("937об",
          *death_month(Month.MARCH,
                       # Отецъ — РС-10 1857 двор 18 (Ксенофонтъ Ивановъ, сынъ Антонъ)
                       death(30, Gender.MALE, 28, 31,
                             deceased=person("Михаилъ"),
                             age=1,
                             relatives=[relative(person("Антонъ", "Ксенофонтовъ"), Relationship.FATHER)],
                             cause_of_death=WHOOPING_COUGH),
                       ),
          ),
    *page("939об",
          *death_month(Month.MAY,
                       # «Трофимова» — агентъ: возможно «Трифонова». Рожд. № 28 ж (2 февр. 1859) — та же Анна
                       death(54, Gender.FEMALE, 19, 22,
                             deceased=person("Анна"),
                             age="3 мес",
                             relatives=[relative(person("Иванъ", "Трофимовъ"), Relationship.FATHER)],
                             cause_of_death=WHOOPING_COUGH),
                       ),
          ),
    *page("940об",
          *death_month(Month.MAY,
                       # «Отъ ломоты». РС-10 1857 двор 32: Никита Осиповъ, дочь Александра 4
                       death(57, Gender.FEMALE, 28, 31,
                             deceased=person("Александра"),
                             age=7,
                             relatives=[relative(person("Никита", "Осиповъ"), Relationship.FATHER)],
                             cause_of_death="ломота"),
                       ),
          *death_month(Month.JUNE,
                       # «Деревни Нижней Верьи крестьянина Андрея Калинина дочь Ел|ена и дочь Ѳеодосія
                       # близнецы», «2½ недѣли» — двойни рожд. № 86/87 ж (род. 15 мая)
                       death(59, Gender.FEMALE, 4, 7,
                             deceased=person("Елена"),
                             age="2 нед",
                             relatives=[relative(person("Андрей", last_name_orig="Калининъ"), Relationship.FATHER)],
                             cause_of_death=WHOOPING_COUGH),
                       death(60, Gender.FEMALE, 4, 7,
                             deceased=person("Ѳеодосія"),
                             age="2 нед",
                             relatives=[relative(person("Андрей", last_name_orig="Калининъ"), Relationship.FATHER)],
                             cause_of_death=WHOOPING_COUGH),
                       # «Тоже деревни крестьянина Константина Иванова дочь Ѳе…ся?», 2 недѣли — имя дочитано
                       # по рожд. № 89 ж (Ѳеодосія, род. 20 мая, отецъ Константинъ Ивановъ Мудриловъ?)
                       death(61, Gender.FEMALE, 4, 7,
                             deceased=person("Ѳеодосія"),
                             age="2 нед",
                             relatives=[relative(person("Константинъ", "Ивановъ"), Relationship.FATHER)],
                             cause_of_death=WHOOPING_COUGH),
                       ),
          ),
    *page("944об",
          *death_month(Month.JULY,
                       # Запись другой рукой. Отецъ «Василья Ники…рова» — вычитано владельцемъ 07.11.2026 какъ
                       # «Никиѳоровъ» (прежде «Дмитріевъ» — взято изъ погреб. № 107 м, л. 953об). Лѣта «2½ мѣс.»
                       # — по возрасту это Пелагія рожд. № 82 ж (2 мая), гдѣ отецъ «Василій Никитинъ»
                       death(86, Gender.FEMALE, 14, 17,
                             deceased=person("Пелагея"),
                             age="2 мес",
                             relatives=[relative(person("Василій", "Никиѳоровъ"), Relationship.FATHER)],
                             cause_of_death=WHOOPING_COUGH),
                       ),
          ),
    *page("945об",
          *death_month(Month.JULY,
                       # РС-10 1857 двор 35 (Ладугины): Кондратій Алексѣевъ
                       death(92, Gender.FEMALE, 23, 26,
                             deceased=person("Ольга"),
                             age=3,
                             relatives=[relative(person("Кондратій", "Алексѣевъ"), Relationship.FATHER)],
                             cause_of_death=WHOOPING_COUGH),
                       ),
          ),
    *page("950об",
          *death_month(Month.AUGUST,
                       # РС-10 1857 двор 41: Варѳоломей Макаровъ, «пришелъ изъ кантонистовъ». Сынъ Петръ
                       # «4 мѣсяцовъ» — вѣроятно рожд. № 86 м (12 іюня, отецъ «Варѳоломей Митровъ?»), но тогда
                       # ему 2½ мѣс.
                       death(92, Gender.MALE, 28, 31,
                             deceased=person("Петръ"),
                             age="4 мес",
                             relatives=[relative(person("Варѳоломей", "Макаровъ"), Relationship.FATHER)],
                             cause_of_death=WHOOPING_COUGH),
                       ),
          *death_month(Month.SEPTEMBER,
                       # РС-10 1857 двор 28: у Макара Иванова дочь Наталья 2 (тогда)
                       death(105, Gender.FEMALE, 1, 4,
                             deceased=person("Наталья"),
                             age=2,
                             relatives=[relative(person("Макаръ", "Ивановъ"), Relationship.FATHER)],
                             cause_of_death=WHOOPING_COUGH),
                       ),
          ),
    *page("951об",
          *death_month(Month.SEPTEMBER,
                       # «Экономическаго вѣдомства, деревни Нижней Верьи крестьянина Ефима Чигорѣва? сынъ
                       # Александръ?» — фамилія и имя неувѣренны. ⚠ № 81 ж (л. 943об): «Экономической деревни
                       # Верхней Верьи крестьянина Ефима Макарова Чугунова?/Тугарова? дочь Анна» — вѣроятно
                       # тотъ же отецъ, и одна изъ двухъ деревень — ошибка писца
                       death(95, Gender.MALE, 10, 13,
                             deceased=person("Александръ"),
                             age="6 мес",
                             relatives=[relative(person("Ефимъ", last_name_orig="Чигорѣвъ", status=ECON_PEASANT_MALE),
                                                 Relationship.FATHER)],
                             cause_of_death=WHOOPING_COUGH),
                       death(97, Gender.MALE, 20, 23,
                             deceased=person("Григорій"),
                             age="1 год 6 мес",
                             relatives=[relative(person("Варѳоломей", "Макаровъ", status=ECON_PEASANT_MALE),
                                                 Relationship.FATHER)],
                             cause_of_death=WHOOPING_COUGH),
                       ),
          ),
    *page("953об",
          *death_month(Month.NOVEMBER,
                       # Отецъ рожд. № 197 ж этого года
                       death(105, Gender.MALE, 6, 9,
                             deceased=person("Сергій"),
                             age=1,
                             relatives=[relative(person("Емельянъ", "Мироновъ"), Relationship.FATHER)],
                             cause_of_death=WHOOPING_COUGH),
                       # «Деревни Нижней Верьи вдова Васса Якимова», 77, «отъ коклюша» — такъ написано.
                       # Возможно, «Василиса Якишова» 74 РС-10 1857, двор 5
                       death(113, Gender.FEMALE, 7, 10,
                             deceased=person("Васса", "Якимова", status=KAZENNYJ_PEASANT_WIDOW),
                             age=77,
                             cause_of_death=WHOOPING_COUGH),
                       ),
          ),
    defaults=DEFAULTS,
    reviewed=False,
)
