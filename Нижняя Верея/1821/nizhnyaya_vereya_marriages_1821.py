from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import (KAZENNYJ_PEASANT_DAUGHTER_MAIDEN, KAZENNYJ_PEASANT_FEMALE,
                                   KAZENNYJ_PEASANT_MALE, KAZENNYJ_PEASANT_SON)

# Метрическая книга Николаевской церкви с. Степанькова за 1821 г., часть вторая.
# **ГАВО ф. 556 оп. 106 д. 416, л. 379** (альбом «Степаньково 1821 (ГАВО 556-106-416)»).
# Часть вторая — 9 венчаній, ведомость сходится. НВ в начале XIX в. — приход Степанькова
# (см. `../ARCHIVES.md`). Взята одна запись — рода Гусевых.
#
# reviewed=False: найдено при сплошном чтении года (агент), запись перечитана по скану.

DEFAULTS = RecordDefaults(residence="Нижняя Верея", status_male=KAZENNYJ_PEASANT_MALE,
                          status_female=KAZENNYJ_PEASANT_FEMALE)

nizhnyaya_vereya_marriages_1821 = marriage_records(
    "ГАВО", "556", "106", "416", "Нижняя Верея", "Николаевская",
    1821,
    *page("379",
          *marriage_month(Month.JANUARY,
                          # 🏆 **ВЕНЧАНІЕ КСЕНОФОНТА ИВАНОВА И СОЛОМЕИ МАКСИМОВОЙ** — главы двора 18 РС-10 1857 г.
                          # «…Казеннаго вѣдомства деревни Нижней Вѣри крестьянской сынъ Ксенофонтъ Ивановъ того жъ
                          # вѣдомства деревни Коннова съ крестьянскою дѣвкою Соломеею Максимовою по добровольному
                          # ихъ и родителей ихъ согласію… оба 1-мъ бракомъ». Поручители «тоя деревни крестьяне
                          # Анисимъ Семеновъ и Андрей Ивановъ». ⓘ Невѣста, как и Аксинья Леонтьева в 1819 г., —
                          # изъ Конново
                          marriage(2, 30,
                                   groom=person("Ксенофонтъ", "Ивановъ", status=KAZENNYJ_PEASANT_SON),
                                   bride=person("Соломея", "Максимова", status=KAZENNYJ_PEASANT_DAUGHTER_MAIDEN, residence="Конново"),
                                   groom_marriage_num=1, bride_marriage_num=1,
                                   witness1=person("Анисимъ", "Семеновъ"),
                                   witness2=person("Андрей", "Ивановъ")),
                          ),
          ),
    defaults=DEFAULTS,
    reviewed=False,
)
