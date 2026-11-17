from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import MAIDEN, PEASANT_FEMALE, PEASANT_MAIDEN, PEASANT_MALE, PEASANT_SON

nizhnyaya_vereya_marriages_1910 = marriage_records(
    "ЦАНО", "2800", "1", "14", "Нижняя Верея", "Николаевская",
    1910,
    *page("308об-309",
          *marriage_month(Month.OCTOBER,
                          marriage(1, 24,
                                   groom=person("Петр", "Матфеев", last_name_orig="Суслов?"), groom_marriage_num=1, groom_age=18,
                                   bride=person("Мария", "Прохорова", last_name_orig="Ладугина", status=MAIDEN), bride_marriage_num=1, bride_age=18,
                                   witness1=person("Алексей", "Васильев", last_name_orig="Ладугин"),
                                   witness2=person("Ермолай", "Дорофеев", last_name_orig="Орлов"),
                                   witness3=person("Михаил", "Георгиев", last_name_orig="Суслов"),
                                   witness4=person("Иоанн", "Николаев", "Фролов")),
                          ),
          ),
    defaults=RecordDefaults(
        residence="Нижняя Верея",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_MAIDEN,
        status_groom=PEASANT_SON,
    ),
)
