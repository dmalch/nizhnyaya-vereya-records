from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import DIARRHEA, NATURAL, SMALLPOX
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

nizhnyaya_vereya_deaths_1907 = death_records(
    "ЦАНО", "2800", "1", "14", "Нижняя Верея", "Николаевская",
    1907,
    *page("183об",
          *death_month(Month.AUGUST,
                       death(1, Gender.FEMALE, 11, 12,
                             deceased=person("Анастасия"), age="4 мес",
                             relatives=[relative(person("Димитрий", "Феодоров", last_name_orig="Гусев"), Relationship.FATHER)],
                             cause_of_death=SMALLPOX),
                       ),
          ),
    *page("187об",
          *death_month(Month.OCTOBER,
                       death(2, Gender.FEMALE, 4, 6,
                             deceased=person("Екатерина"), age="11 мес",
                             relatives=[relative(person("Алексей", "Васильев", last_name_orig="Ладугин"), Relationship.FATHER)],
                             cause_of_death=DIARRHEA),
                       ),
          ),
    defaults=RecordDefaults(
        residence="Нижняя Верея",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        cause_of_death=NATURAL
    ),
)
