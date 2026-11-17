from verso.ru.dsl import (Gender, Month, NOT_IN_DOCUMENT, RecordDefaults, Relationship, death,
                          death_month, death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import DIARRHEA, NATURAL
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE, SOLDIER

nizhnyaya_vereya_deaths_1905 = death_records(
    "ЦАНО", "2800", "1", "14", "Нижняя Верея", "Николаевская",
    1905,
    *page("92",
          *death_month(Month.FEBRUARY,
                       death(1, Gender.FEMALE, None, 13,
                             deceased=person("Ксения"), age="21 дн",
                             relatives=[relative(person("Андрей", "Леонтьев", last_name_orig="Ладугин"), Relationship.FATHER)],
                             cause_of_death=NOT_IN_DOCUMENT),
                       ),
          ),
    *page("97об",
          *death_month(Month.JUNE,
                       death(2, Gender.MALE, 30, 2, b_month=Month.JULY,
                             deceased=person("Михаил"), age="1 мес 2 нед",
                             relatives=[relative(person("Василий", "Леонтьев", last_name_orig="Ладугин", status=SOLDIER), Relationship.FATHER)],
                             cause_of_death=DIARRHEA),
                       ),
          ),
    *page("98об",
          *death_month(Month.JULY,
                       death(3, Gender.MALE, 26, 28,
                             deceased=person("Феодор"), age=1.5,
                             relatives=[relative(person("Иоанн", "Ионов", last_name_orig="Ладугин"), Relationship.FATHER)],
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
