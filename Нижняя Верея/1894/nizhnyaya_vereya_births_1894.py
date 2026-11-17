from verso.ru.dsl import (Gender, Month, RecordDefaults, birth, birth_month, birth_records, page,
                          person)
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

nizhnyaya_vereya_births_1894 = birth_records(
    "ЦАНО", "2800", "1", "14", "Нижняя Верея", "Николаевская",
    1894,
    *page("6",
          *birth_month(Month.AUGUST,
                       birth(1, Gender.MALE, 21, 22,
                             child=person("Павел"),
                             father=person("Иван", "Семенов", last_name_orig="Гусев"),
                             mother=person("Александра", "Филипова")),
                       ),
          ),
    *page("6об",
          *birth_month(Month.NOVEMBER,
                       birth(2, Gender.FEMALE, None, 3,
                             child=person("Екатерина"),
                             father=person("Андреян", "Архипов", last_name_orig="Гусев", residence="Старая Верея"),
                             mother=person("Анастасия", "Панкратова")),
                       ),
          ),
    defaults=RecordDefaults(
        residence="Нижняя Верея",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE
    ),
)
