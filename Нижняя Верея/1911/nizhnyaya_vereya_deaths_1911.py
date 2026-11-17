from verso.ru.dsl import (Gender, Month, RecordDefaults, death, death_month, death_records, page,
                          person)
from verso.ru.dsl.causes_of_death import NATURAL
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

nizhnyaya_vereya_deaths_1911 = death_records(
    "ЦАНО", "2800", "1", "14", "Нижняя Верея", "Николаевская",
    1911,
    *page("360об",
          *death_month(Month.FEBRUARY,
                       death(1, Gender.MALE, 13, 15,
                             deceased=person("Кондратий", "Алексеев", last_name_orig="Ладугин"),
                             age=75,
                             cause_of_death="скоропостижно"),
                       ),
          ),
    defaults=RecordDefaults(
        residence="Нижняя Верея",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        cause_of_death=NATURAL
    ),
)
