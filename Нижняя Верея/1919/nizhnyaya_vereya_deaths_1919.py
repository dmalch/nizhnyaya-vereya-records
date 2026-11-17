from verso.ru.dsl import (Gender, Month, NOT_IN_DOCUMENT, RecordDefaults, Relationship, death,
                          death_month, death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import NATURAL
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

nizhnyaya_vereya_deaths_1919 = death_records(
    "ЦАНО", "2800", "1", "15", "Нижняя Верея", "Николаевская",
    1919,
    *page("152 об",
          *death_month(Month.JUNE,
                       death(1, Gender.MALE, 22, 23,
                             deceased=person("Леонтий", "Савватиев", "Ладугин"), age=80,
                             cause_of_death=NOT_IN_DOCUMENT),
                       ),
          ),
    *page("153 об",
          *death_month(Month.JULY,
                       death(1, Gender.FEMALE, None, None,
                             deceased=person("Матрена", "Иоаннова", last_name_orig="Ладугина")),
                       ),
          ),
    *page("156 об",
          *death_month(Month.OCTOBER,
                       death(1, Gender.MALE, None, 5,
                             deceased=person("Дмитрей", "Ксенофонтов", last_name_orig="Гусев"), age=72),
                       ),
          *death_month(Month.NOVEMBER,
                       death(1, Gender.FEMALE, None, 10,
                             deceased=person("Мария"),
                             relatives=[relative(person("Василий", "Семенов", last_name_orig="Гусев"), Relationship.FATHER)],
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
