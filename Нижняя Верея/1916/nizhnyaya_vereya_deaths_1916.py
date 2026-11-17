from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import NATURAL, WEAKNESS
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

nizhnyaya_vereya_deaths_1916 = death_records(
    "ЦАНО", "2800", "1", "15", "Нижняя Верея", "Николаевская",
    1916,
    *page("72 об",
          *death_month(Month.MAY,
                       death(1, Gender.FEMALE, 9, 11,
                             deceased=person("Александра"), age=1,
                             relatives=[relative(person("Павел", "Иоаннов", last_name_orig="Гусев"), Relationship.FATHER)],
                             cause_of_death=WEAKNESS),
                       ),
          ),
    defaults=RecordDefaults(
        residence="Нижняя Верея",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        cause_of_death=NATURAL
    ),
)
