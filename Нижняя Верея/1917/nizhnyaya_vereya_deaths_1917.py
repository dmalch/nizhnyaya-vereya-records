from verso.ru.dsl import (Gender, Month, RecordDefaults, death, death_month, death_records, page,
                          person)
from verso.ru.dsl.causes_of_death import COLD, CONSUMPTION, NATURAL
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

nizhnyaya_vereya_deaths_1917 = death_records(
    "ЦАНО", "2800", "1", "15", "Нижняя Верея", "Николаевская",
    1917,
    *page("107 об",
          *death_month(Month.AUGUST,
                       death(1, Gender.MALE, 20, 22,
                             deceased=person("Василий", "Васильев", last_name_orig="Гусев"), age=34,
                             cause_of_death=CONSUMPTION),
                       ),
          ),
    *page("109 об",
          *death_month(Month.SEPTEMBER,
                       death(1, Gender.MALE, 14, 16,
                             deceased=person("Иоанн", "Антонов", last_name_orig="Гусев"), age=59,
                             cause_of_death=COLD),
                       ),
          ),
    defaults=RecordDefaults(
        residence="Нижняя Верея",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        cause_of_death=NATURAL
    ),
)
