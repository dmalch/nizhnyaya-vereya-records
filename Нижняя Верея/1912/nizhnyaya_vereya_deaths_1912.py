from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import NATURAL, WEAKNESS
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

nizhnyaya_vereya_deaths_1912 = death_records(
    "ЦАНО", "2800", "1", "14", "Нижняя Верея", "Николаевская",
    1912,
    *page("364об",
          *death_month(Month.MARCH,
                       death(1, Gender.MALE, 5, 7,
                             deceased=person("Иоанн", "Феодоров", last_name_orig="Гусев"),
                             age=80),
                       ),
          ),
    *page("366об",
          *death_month(Month.MAY,
                       death(2, Gender.FEMALE, 20, 22,
                             deceased=person("Анна"), age=1,
                             relatives=[relative(person("Иоанн", "Ионов", last_name_orig="Ладугин"), Relationship.FATHER)],
                             cause_of_death=WEAKNESS),
                       ),
          ),
    *page("368об",
          *death_month(Month.AUGUST,
                       death(3, Gender.FEMALE, 16, 18,
                             deceased=person("Евдокия", "Афанасьева", last_name_orig="Гусева", residence="Старая Верея"),
                             age=76),
                       ),
          ),
    defaults=RecordDefaults(
        residence="Нижняя Верея",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        cause_of_death=NATURAL
    ),
)
