from verso.ru.dsl import (Gender, Month, RecordDefaults, birth, birth_month, birth_records, page,
                          person)
from verso.ru.dsl.statuses import (KAZENNYJ_PEASANT_FEMALE, KAZENNYJ_PEASANT_LEGAL_WIFE,
                                   KAZENNYJ_PEASANT_MAIDEN, KAZENNYJ_PEASANT_MALE,
                                   KAZENNYJ_PEASANT_WIDOW)

# Метрическая книга Успенской церкви с. ШИМОРСКОГО за 1837 г., часть первая — записи
# «Казеннаго вѣдомства деревни Нижней Верьи». **ГАВО ф. 556 оп. 106 д. 611, лл. 141–162об**
# (альбом «Шиморское 1837 (ГАВО 556-106-611)»); книга «№ 32, Подана Генваря 10 дня 1838».
#
# ⚠ Форма ПОВЕСТВОВАТЕЛЬНАЯ: «У кого кто родился» одним абзацем, и каждая страница — и
# оборот, и лицевая — самостоятельна, воспріемники в своей графе справа. Деревню писец
# называет в каждой записи; Верхнюю и Нижнюю Верью на беглой руке легко спутать — ч. 1
# № 6 м (л. 142, Спиридонъ Моисеевъ) читается как ВЕРХНЯЯ и не вынесен.
#
# ⇒ В 1837 г. НВ пишет уже Шиморское (в 1836 г. — оба прихода, см. `../ARCHIVES.md`).
# Прочитана вся часть первая, взяты все семь записей НВ.
#
# reviewed=False: прочитано при 1.3–2.6×; спорное — в комментариях.

DEFAULTS = RecordDefaults(residence="Нижняя Верея", status_male=KAZENNYJ_PEASANT_MALE,
                          status_female=KAZENNYJ_PEASANT_FEMALE, status_mother=KAZENNYJ_PEASANT_LEGAL_WIFE)

nizhnyaya_vereya_births_1837 = birth_records(
    "ГАВО", "556", "106", "611", "Нижняя Верея", "Успенская",
    1837,
    *page("141об",
          *birth_month(Month.JANUARY,
                       # ⚠ Кумъ «Оной же деревни крестьянинъ Иванъ Е…евъ» — отчество не прочитано, и после
                       # него слова «Об…дного Р…наго бора» (?); кума — «Ивана Яковлева жена Марѳа Андреева»
                       birth(3, Gender.FEMALE, 10, 11,
                             child=person("Татьяна"),
                             father=person("Емельянъ", "Ананьинъ"),
                             mother=person("Евдокія", "Ильина"),
                             god_parent2=person("Марѳа", "Андреева")),
                       ),
          ),
    *page("143",
          *birth_month(Month.JANUARY,
                       # Кума — «дѣвица Ксенія Степанова», тёзка матери: в ноябре того же года «дѣвка Ксенія
                       # Степанова» НВ выходит за Луку Ѳедорова изъ Верхней Верьи (ч. 2 № 50), и Марко Ивановъ
                       # там её поручитель. ⚠ Кумъ «Василій Сав…овъ» — отчество перечитать
                       birth(14, Gender.FEMALE, 25, 26,
                             child=person("Анна"),
                             father=person("Марко", "Ивановъ"),
                             mother=person("Ксенія", "Степанова"),
                             god_parent2=person("Ксенія", "Степанова", status=KAZENNYJ_PEASANT_MAIDEN)),
                       ),
          ),
    *page("143об",
          *birth_month(Month.FEBRUARY,
                       # «Иванъ Гуровъ» — ср. «Авивъ Гуровъ» МК 1839 (№ 35 ж). ⚠ Кумъ «Назаръ? Ивановъ» —
                       # имя перечитать
                       birth(14, Gender.MALE, 1, 2,
                             child=person("Ѳеодоръ"),
                             father=person("Иванъ", "Гуровъ"),
                             mother=person("Авдотья", "Степанова"),
                             god_parent1=person("Назаръ", "Ивановъ"),
                             god_parent2=person("Ульяна", "Яковлева", status=KAZENNYJ_PEASANT_MAIDEN)),
                       ),
          ),
    *page("150",
          *birth_month(Month.JUNE,
                       birth(62, Gender.MALE, 16, 17,
                             child=person("Иванъ"),
                             father=person("Козма", "Ивановъ"),
                             mother=person("Евдокія", "Аѳанасьева"),
                             god_parent1=person("Иванъ", "Еремеевъ"),
                             god_parent2=person("Марѳа", "Ананьина", status=KAZENNYJ_PEASANT_MAIDEN)),
                       ),
          ),
    *page("156об",
          *birth_month(Month.SEPTEMBER,
                       # Те же родители — дочь Анна в 1839 г. (№ 89 ж). ⚠ Первое слово графы воспріемников
                       # (деревня кума?) не прочитано
                       birth(100, Gender.FEMALE, 29, 30,
                             child=person("Любовь"),
                             father=person("Василій", "Григорьевъ"),
                             mother=person("Надежда", "Яковлева"),
                             god_parent1=person("Андрей", "Прохоровъ"),
                             god_parent2=person("Акилина", "Яковлева", status=KAZENNYJ_PEASANT_WIDOW)),
                       ),
          ),
    *page("158об",
          *birth_month(Month.OCTOBER,
                       # ⚠ Крещён «30» — вторая цифра под сгибом. Отец — «Алексѣй Павловъ» (первым чтением было
                       # «Акимъ»; исправлено 12.10.2026 по ИР 1855, двор 353: «Алексѣй Павловъ 51, жена его Меланья
                       # Андреева 51, сынъ ихъ Павелъ 16»)
                       birth(126, Gender.MALE, 30, 30,
                             child=person("Павелъ"),
                             father=person("Алексѣй", "Павловъ"),
                             mother=person("Меланія", "Андреева"),
                             god_parent1=person("Андрей", "Тихоновъ"),
                             god_parent2=person("Стефанида", "Иванова")),
                       ),
          ),
    *page("161об",
          *birth_month(Month.DECEMBER,
                       # «Силанъ Аврамовъ» — тот же, что в 1839 г. (№ 107 ж), но жена там «Ирина Корнилова».
                       # ⚠ Имя младенца «Спиридонъ/Стефанъ» и воспріемники («Алексѣй? Григорьевъ? и жена Ѳекла?
                       # Харитонова») — перечитать
                       birth(142, Gender.MALE, 12, 13,
                             child=person("Спиридонъ"),
                             father=person("Силанъ", "Аврамовъ"),
                             mother=person("Ксенія", "Корнильева")),
                       ),
          ),
    defaults=DEFAULTS,
    reviewed=False,
)
