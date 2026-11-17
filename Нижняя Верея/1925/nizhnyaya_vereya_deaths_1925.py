from verso.ru.dsl import (Gender, Month, NOT_IN_DOCUMENT, RecordDefaults, death, death_month,
                          death_records, page, person)
from verso.ru.dsl.causes_of_death import NATURAL
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

nizhnyaya_vereya_deaths_1925 = death_records(
    "ЦАНО", "2800", "1", "15", "Нижняя Верея", "Николаевская",
    1925,
    *page("201 об",
          *death_month(Month.APRIL,
                       death(1, Gender.FEMALE, 17, 19,
                             deceased=person("Евдокия", "Алексеева", last_name_orig="Ладугина"),
                             cause_of_death=NOT_IN_DOCUMENT),
                       ),
          ),
    defaults=RecordDefaults(
        residence="Нижняя Верея",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        cause_of_death=NATURAL
    ),
)
