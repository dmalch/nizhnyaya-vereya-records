from verso.ru.dsl import (Gender, Month, RecordDefaults, birth, birth_month, birth_records, page,
                          person)
from verso.ru.dsl.statuses import (KAZENNYJ_PEASANT_FEMALE, KAZENNYJ_PEASANT_MAIDEN,
                                   KAZENNYJ_PEASANT_MALE, KAZENNYJ_PEASANT_WIFE)

# Метрическая книга Николаевской церкви с. Степанькова за 1806 г., часть первая.
# **ГАВО ф. 556 оп. 106 д. 208, л. 180** (альбом «Степаньково 1806 (ГАВО 556-106-208)»).
#
# ⚠ **В начале XIX в. Нижнюю Верею записывает Степаньково** («казеннаго вѣдомства деревни
# Нижней Вѣри»), а к 1859 г. — уже Шиморское (см. `../ARCHIVES.md`). Шиморскія книги
# 1803–1824 гг. НВ не называют вовсе (прочитаны 05.10.2026).
# Взята одна запись — рода Гусевых; остальной год в DSL не вынесен.
#
# reviewed=False: найдено при сплошном чтении года (агент), запись перечитана по скану.

DEFAULTS = RecordDefaults(residence="Нижняя Верея", status_male=KAZENNYJ_PEASANT_MALE,
                          status_female=KAZENNYJ_PEASANT_FEMALE, status_mother=KAZENNYJ_PEASANT_WIFE)

nizhnyaya_vereya_births_1806 = birth_records(
    "ГАВО", "556", "106", "208", "Нижняя Верея", "Николаевская",
    1806,
    *page("180",
          *birth_month(Month.JANUARY,
                       # 🏆 **МЕТРИКА КСЕНОФОНТА ИВАНОВА** — главы двора 18 РС-10 1857 г. (линия Гусевых).
                       # «Казеннаго вѣдомства деревни Нижней Вѣри у крестьянина Ивана Полуектова отъ жены его
                       # Прасковьи Панфиловой родился сынъ Ксенофонтъ генваря 26 дня, молитвованъ и крещенъ въ
                       # домѣ того жъ числа… воспріемники были крестьянинъ Никита Никитинъ, дѣвица Пелагея
                       # Еримова [Ефимова?]». ⚠ РС-10 даёт ему «49 лѣтъ 5 мѣс» в ноябре 1857 г. ⇒ ок. 1808;
                       # метрика — **январь 1806**, на два года раньше. ⓘ Кума «Пелагея Ефимова» стоит и у его
                       # брата Алексѣя в 1812 г. — вероятно, дочь Ефима, сестра Ипполита Ефимова
                       birth(4, Gender.MALE, 26, 26,
                             child=person("Ксенофонтъ"),
                             father=person("Иванъ", "Полуектовъ"),
                             mother=person("Прасковья", "Панфилова"),
                             god_parent1=person("Никита", "Никитинъ"),
                             god_parent2=person("Пелагея", "Ефимова", status=KAZENNYJ_PEASANT_MAIDEN)),
                       ),
          ),
    defaults=DEFAULTS,
    reviewed=False,
)
