from verso.ru.dsl import (Gender, Month, RecordDefaults, death, death_month, death_records, page,
                          person)
from verso.ru.dsl.causes_of_death import NATURAL
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

nizhnyaya_vereya_deaths_1915 = death_records(
    "ЦАНО", "2800", "1", "15", "Нижняя Верея", "Николаевская",
    1915,
    *page("29 об",
          *death_month(Month.FEBRUARY,
                       death(1, Gender.FEMALE, 25, 28,
                             deceased=person("Параскева", "Савватеева", last_name_orig="Гусева")),
                       ),
          ),
    defaults=RecordDefaults(
        residence="Нижняя Верея",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        cause_of_death=NATURAL
    ),
)
