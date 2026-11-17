from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import DIARRHEA, NATURAL, WEAKNESS
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

nizhnyaya_vereya_deaths_1910 = death_records(
    "ЦАНО", "2800", "1", "14", "Нижняя Верея", "Николаевская",
    1910,
    *page("311об",
          *death_month(Month.JANUARY,
                       death(1, Gender.MALE, 27, 29,
                             deceased=person("Иоанн"), age="4 мес",
                             relatives=[relative(person("Василий", "Аврамов", last_name_orig="Гусев", residence="Старая Верея"), Relationship.FATHER)],
                             cause_of_death=WEAKNESS),
                       ),
          ),
    *page("313об",
          *death_month(Month.JUNE,
                       death(2, Gender.MALE, 4, 6,
                             deceased=person("Павел"), age="7 мес",
                             relatives=[relative(person("Андреян", "Архипов", last_name_orig="Гусев", residence="Старая Верея"), Relationship.FATHER)],
                             cause_of_death=WEAKNESS),
                       death(3, Gender.FEMALE, 27, 29,
                             deceased=person("Екатерина"), age="8 мес",
                             relatives=[relative(person("Иоанн", "Феодоров", last_name_orig="Гусев"), Relationship.FATHER)],
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
