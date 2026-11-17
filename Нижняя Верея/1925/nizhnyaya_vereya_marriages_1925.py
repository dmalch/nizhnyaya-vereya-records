from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MAIDEN, PEASANT_MALE

nizhnyaya_vereya_marriages_1925 = marriage_records(
    "ЦАНО", "2800", "1", "15", "Нижняя Верея", "Николаевская",
    1925,
    *page("195 об - 196",
          *marriage_month(Month.FEBRUARY,
                          marriage(1, 8,
                                   groom=person("Николай", "Владимиров", last_name_orig="Ладугин"), groom_marriage_num=1, groom_age=24,
                                   bride=person("Евдокия", "Васильева", last_name_orig="Здобнова", residence="п. Озерное"), bride_marriage_num=2, bride_age=20),
                          ),
          ),
    *page("196 об - 197",
          *marriage_month(Month.MAY,
                          marriage(1, 31,
                                   groom=person("Дмитрий", "Васильев", last_name_orig="Гусев"), groom_marriage_num=1, groom_age=20,
                                   bride=person("Екатерина", "Феодорова", last_name_orig="Суслова"), bride_marriage_num=1, bride_age=18),
                          ),
          ),
    defaults=RecordDefaults(
        residence="Нижняя Верея",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_MAIDEN
    ),
)
