from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import DIARRHEA, NATURAL, WEAKNESS
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

nizhnyaya_vereya_deaths_1914 = death_records(
    "ЦАНО", "2800", "1", "14", "Нижняя Верея", "Николаевская",
    1914,
    *page("472об",
          *death_month(Month.JUNE,
                       death(1, Gender.MALE, 10, 12,
                             deceased=person("Феодор"), age="1 нед",
                             relatives=[relative(person("Иоанн", "Федоров", last_name_orig="Гусев"), Relationship.FATHER)],
                             cause_of_death=WEAKNESS),
                       ),
          ),
    *page("473об",
          *death_month(Month.AUGUST,
                       death(2, Gender.MALE, None, 19,
                             deceased=person("Василей"), age="4 мес",
                             relatives=[relative(person("Иоанн", "Иосифов", last_name_orig="Ладугин"), Relationship.FATHER)],
                             cause_of_death=DIARRHEA),
                       ),
          ),
    *page("474об",
          *death_month(Month.SEPTEMBER,
                       death(3, Gender.FEMALE, 24, 25,
                             deceased=person("Параскева"), age=5,
                             relatives=[relative(person("Иоанн", "Иоаннов?", last_name_orig="Ладугин"), Relationship.FATHER)]),
                       ),
          ),
    defaults=RecordDefaults(
        residence="Нижняя Верея",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        cause_of_death=NATURAL
    ),
)
