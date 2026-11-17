from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import COLD, NATURAL, WEAKNESS
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE, WIDOW

nizhnyaya_vereya_deaths_1909 = death_records(
    "ЦАНО", "2800", "1", "14", "Нижняя Верея", "Николаевская",
    1909,
    *page("262об",
          *death_month(Month.FEBRUARY,
                       death(1, Gender.MALE, 16, 18,
                             deceased=person("Василий"),
                             relatives=[relative(person("Феодор", "Семенов", last_name_orig="Гусев"), Relationship.FATHER)],
                             cause_of_death=WEAKNESS),
                       ),
          ),
    *page("270об",
          *death_month(Month.SEPTEMBER,
                       death(2, Gender.FEMALE, 17, 19,
                             deceased=person("Параскева"), age=11,
                             relatives=[relative(person("Матрона", "Платонова", last_name_orig="Ладугина", status=WIDOW), Relationship.STEP_MOTHER)],
                             cause_of_death=COLD),
                       ),
          ),
    *page("271об",
          *death_month(Month.DECEMBER,
                       death(3, Gender.FEMALE, 22, 24,
                             deceased=person("Ксения", "Митрофанова", last_name_orig="Гусева", residence="Старая Верея"),
                             age=78),
                       ),
          ),
    defaults=RecordDefaults(
        residence="Нижняя Верея",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        cause_of_death=NATURAL
    ),
)
