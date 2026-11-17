from verso.ru.dsl import Month, RecordDefaults, marriage, marriage_month, marriage_records, page, person
from verso.ru.dsl.statuses import (KAZENNYJ_PEASANT_FEMALE, KAZENNYJ_PEASANT_GIRL, KAZENNYJ_PEASANT_MALE,
                                   KAZENNYJ_PEASANT_WIDOW)

# Метрическая книга Николаевской церкви с. Степанькова за 1835 г., часть вторая. **ГАВО ф. 556 оп. 111 д. 348,
# лл. 247–249** (альбом «Степаньково 1835 (ГАВО 556-111-348)»). Прочитана вся часть (22 брака) 07.11.2026; НВ —
# два брака. Поручители записаны общимъ спискомъ, безъ стороны. Вѣнчалъ свящ. Василій Алексѣевъ Канторскій.
# reviewed=False.

DEFAULTS = RecordDefaults(residence="Нижняя Верея", status_male=KAZENNYJ_PEASANT_MALE,
                          status_female=KAZENNYJ_PEASANT_FEMALE)

nizhnyaya_vereya_marriages_1835 = marriage_records(
    "ГАВО", "556", "111", "348", "Нижняя Верея", "Николаевская",
    1835,
    *page("247",
          *marriage_month(Month.JANUARY,
                          marriage(3, 13,
                                   groom=person("Маркъ", "Савинъ"),
                                   groom_marriage_num=1,
                                   bride=person("Варвара", "Силина", status=KAZENNYJ_PEASANT_GIRL, residence="Высоково"),
                                   witness1=person("Трофимъ", "Флоровъ"),
                                   witness2=person("Евстигнѣй", "Павловъ")),
                          ),
          ),
    *page("248",
          *marriage_month(Month.JULY,
                          # Женихъ овдовѣлъ 20 марта (погреб. № 8 ж: «Петра Ефремова жена Анна Ильева», 29)
                          marriage(14, 1,
                                   groom=person("Петръ", "Ефремовъ"),
                                   groom_marriage_num=2,
                                   bride=person("Маланья", "Григорьева", status=KAZENNYJ_PEASANT_WIDOW, residence="Степаньково"),
                                   bride_marriage_num=2,
                                   witness1=person("Николай", "Яковлевъ"),
                                   witness2=person("Климъ", "Яковлевъ")),
                          ),
          ),
    defaults=DEFAULTS,
    reviewed=False,
)
