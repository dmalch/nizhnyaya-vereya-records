from verso.ru.dsl import (Gender, Month, RecordDefaults, birth, birth_month, birth_records, page,
                          person)
from verso.ru.dsl.statuses import (KAZENNYJ_PEASANT_FEMALE, KAZENNYJ_PEASANT_GIRL,
                                   KAZENNYJ_PEASANT_MALE, KAZENNYJ_PEASANT_WIFE)

# Метрическая книга Николаевской церкви с. Степанькова за 1812 г., часть первая.
# **ГАВО ф. 556 оп. 106 д. 298, л. 74** (альбом «Степаньково 1812 (ГАВО 556-106-298)»).
# Часть первая — 39 записей, ведомость (19 м / 20 ж) сходится. НВ в начале XIX в. — приход
# Степанькова (см. `../ARCHIVES.md`). Взята одна запись — рода Гусевых.
#
# reviewed=False: найдено при сплошном чтении года (агент), запись перечитана по скану.

DEFAULTS = RecordDefaults(residence="Нижняя Верея", status_male=KAZENNYJ_PEASANT_MALE,
                          status_female=KAZENNYJ_PEASANT_FEMALE, status_mother=KAZENNYJ_PEASANT_WIFE)

nizhnyaya_vereya_births_1812 = birth_records(
    "ГАВО", "556", "106", "298", "Нижняя Верея", "Николаевская",
    1812,
    *page("74",
          *birth_month(Month.FEBRUARY,
                       # Брат Ксенофонта (1806). «…казеннаго вѣдомства деревни Нижней Вѣри у крестьянина Ивана
                       # Полиектова отъ жены его Параскови Памфиловой родился сынъ Алексѣй, молитвованъ и
                       # крещенъ въ домѣ… воспріемники были Климъ Тихоновъ да дѣвка Палагея Ефимова того жъ
                       # вѣдомства и деревни крестьяне». ⚠ В РС-10 1857 г. в дворе 18 Алексѣя Иванова нет ⇒
                       # умер или выбыл до 1850 г.
                       birth(10, Gender.MALE, 7, 8,
                             child=person("Алексѣй"),
                             father=person("Иванъ", "Полуектовъ"),
                             mother=person("Прасковья", "Панфилова"),
                             god_parent1=person("Климъ", "Тихоновъ"),
                             god_parent2=person("Пелагея", "Ефимова", status=KAZENNYJ_PEASANT_GIRL)),
                       ),
          ),
    defaults=DEFAULTS,
    reviewed=False,
)
