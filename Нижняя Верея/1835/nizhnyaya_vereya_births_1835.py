from verso.ru.dsl import Gender, Month, RecordDefaults, birth, birth_month, birth_records, page, person
from verso.ru.dsl.statuses import (KAZENNYJ_PEASANT_FEMALE, KAZENNYJ_PEASANT_LEGAL_WIFE,
                                   KAZENNYJ_PEASANT_MALE, KAZENNYJ_PEASANT_WIFE)

# Метрическая книга Николаевской церкви с. Степанькова за 1835 г., часть первая. **ГАВО ф. 556 оп. 111 д. 348,
# лл. 237–243об** (альбом «Степаньково 1835 (ГАВО 556-111-348)», pk 1006). Прочитана вся часть 07.11.2026;
# НВ («казенной деревни Нижней Вѣрьи») — одна запись. reviewed=False.

DEFAULTS = RecordDefaults(residence="Нижняя Верея", status_male=KAZENNYJ_PEASANT_MALE,
                          status_female=KAZENNYJ_PEASANT_FEMALE, status_mother=KAZENNYJ_PEASANT_LEGAL_WIFE)

nizhnyaya_vereya_births_1835 = birth_records(
    "ГАВО", "556", "111", "348", "Нижняя Верея", "Николаевская",
    1835,
    *page("242об",
          *birth_month(Month.NOVEMBER,
                       birth(39, Gender.MALE, 2, 2,
                             child=person("Михаилъ"),
                             father=person("Ульянъ", "Ивановъ"),
                             mother=person("Акилина", "Яковлева"),
                             god_parent1=person("Маркіанъ", "Никифоровъ"),
                             god_parent2=person("Наталья", "Яковлева", status=KAZENNYJ_PEASANT_WIFE),
                             comment="крестилъ свящ. Михаилъ Яковлевъ Казанскій, при крещеніи дьячекъ Семенъ Ѳоминъ"),
                       ),
          ),
    defaults=DEFAULTS,
    reviewed=False,
)
