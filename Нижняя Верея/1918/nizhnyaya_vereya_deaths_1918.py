from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import NATURAL
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

nizhnyaya_vereya_deaths_1918 = death_records(
    "ЦАНО", "2800", "1", "15", "Нижняя Верея", "Николаевская",
    1918,
    *page("115 об",
          *death_month(Month.MAY,
                       death(1, Gender.MALE, 6, 6,
                             deceased=person("Архипп", "Поликарпов", last_name_orig="Гусев", status="гражданин", residence="Старая Верея")),
                       ),
          ),
    *page("117 об",
          *death_month(Month.SEPTEMBER,
                       death(1, Gender.FEMALE, 20, 23,
                             deceased=person("Евдокия", "Васильева", last_name_orig="Ладугина", status="гражданка"), age=25),
                       death(2, Gender.MALE, 28, 30,
                             deceased=person("Василий"), age="9 мес",
                             relatives=[relative(person("Василий", "Аврасов", last_name_orig="Гусев", residence="Старая Верея"), Relationship.FATHER)]),
                       ),
          ),
    defaults=RecordDefaults(
        residence="Нижняя Верея",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        cause_of_death=NATURAL
    ),
)
