from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MAIDEN, PEASANT_MALE

nizhnyaya_vereya_marriages_1914 = marriage_records(
    "ЦАНО", "2800", "1", "14", "Нижняя Верея", "Николаевская",
    1914,
    *page("465об-466",
          *marriage_month(Month.JANUARY,
                          marriage(1, 8,
                                   groom=person("Андреян", "Архипов", last_name_orig="Гусев", residence="Старая Верея"), groom_marriage_num=2, groom_age=40,
                                   bride=person("Екатерина", "Иоаннова", last_name_orig="Макарова", residence="Тамболес"), bride_marriage_num=1, bride_age=29,
                                   witness1=person("Александр", "Алексеев", last_name_orig="Макаров"),
                                   witness2=person("Петр", "Алексеев", last_name_orig="Макаров"),
                                   witness3=person("Михаил", "Петров", last_name_orig="Калинин"),
                                   witness4=person("Сергей", "Алексеев", last_name_orig="Макаров")),
                          ),
          ),
    *page("466об-467",
          *marriage_month(Month.JANUARY,
                          marriage(2, 20,
                                   groom=person("Иоанн", "Михайлов", last_name_orig="Липатов", residence="Старая Верея"), groom_marriage_num=1, groom_age=18,
                                   bride=person("Пелагия", "Андреева", last_name_orig="Ладугина"), bride_marriage_num=1, bride_age=16,
                                   witness1=person("Алексей", "Максимов", last_name_orig="Гаврилов", residence="Тамболес"),
                                   witness2=person("Андрей", "Семенов", last_name_orig="Гребнев", residence="Тамболес"),
                                   witness3=person("Петр", "Иосифов", last_name_orig="Ладугин"),
                                   witness4=person("Николай", "Минеев", last_name_orig="Фролов")),
                          ),
          ),
    defaults=RecordDefaults(
        residence="Нижняя Верея",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_MAIDEN
    ),
)
