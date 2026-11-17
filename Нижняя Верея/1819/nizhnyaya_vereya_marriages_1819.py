from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import (KAZENNYJ_PEASANT_DAUGHTER_MAIDEN, KAZENNYJ_PEASANT_FEMALE,
                                   KAZENNYJ_PEASANT_MALE, KAZENNYJ_PEASANT_SON)

# Метрическая книга Николаевской церкви с. Степанькова за 1819 г., часть вторая.
# **ГАВО ф. 556 оп. 106 д. 390, л. 94об** (альбом «Степаньково 1819 (ГАВО 556-106-390)»).
# Часть вторая — 12 венчаній, ведомость сходится. НВ в начале XIX в. — приход Степанькова
# (см. `../ARCHIVES.md`). Взята одна запись — рода Гусевых.
#
# reviewed=False: найдено при сплошном чтении года (агент), запись перечитана по скану.

DEFAULTS = RecordDefaults(residence="Нижняя Верея", status_male=KAZENNYJ_PEASANT_MALE,
                          status_female=KAZENNYJ_PEASANT_FEMALE)

nizhnyaya_vereya_marriages_1819 = marriage_records(
    "ГАВО", "556", "106", "390", "Нижняя Верея", "Николаевская",
    1819,
    *page("94об",
          *marriage_month(Month.FEBRUARY,
                          # 🏆 **ВЕНЧАНІЕ ИППОЛИТА ЕФИМОВА И АКСИНЬИ ЛЕОНТЬЕВОЙ** — родителей Григорія (1824) и
                          # Семёна Ипполитовыхъ, прямая линия Гусевых. «…Казеннаго вѣдомства деревни Нижней Вѣри
                          # крестьянской сынъ Ипполитъ Ефимовъ того жъ вѣдомства деревни Коннова съ крестьянскою
                          # дѣвкою Аксиньею Леонтьевою по добровольному ихъ и родителей согласію… оба 1-мъ бракомъ».
                          # Поручители «тоя жъ деревни крестьяне Иванъ Полуектовъ и Андрей Тихоновъ» — Иванъ
                          # Полуектовъ, глава двора 18 РС-10 (отец Ксенофонта). ⇒ **Аксинья — изъ деревни Конново**,
                          # не изъ НВ; её отца Леонтія книги НВ не знают
                          marriage(5, 4,
                                   groom=person("Ипполитъ", "Ефимовъ", status=KAZENNYJ_PEASANT_SON),
                                   bride=person("Аксинья", "Леонтьева", status=KAZENNYJ_PEASANT_DAUGHTER_MAIDEN, residence="Конново"),
                                   groom_marriage_num=1, bride_marriage_num=1,
                                   witness1=person("Иванъ", "Полуектовъ"),
                                   witness2=person("Андрей", "Тихоновъ")),
                          ),
          ),
    defaults=DEFAULTS,
    reviewed=False,
)
