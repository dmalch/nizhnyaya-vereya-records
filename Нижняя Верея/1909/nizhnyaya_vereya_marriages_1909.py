from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import MAIDEN, PEASANT_FEMALE, PEASANT_MAIDEN, PEASANT_MALE, PEASANT_SON

nizhnyaya_vereya_marriages_1909 = marriage_records(
    "ЦАНО", "2800", "1", "14", "Нижняя Верея", "Николаевская",
    1909,
    *page("255об-256",
          *marriage_month(Month.JANUARY,
                          marriage(1, 9,
                                   groom=person("Александр", "Симеонов", last_name_orig="Гусев"), groom_marriage_num=1, groom_age=18,
                                   bride=person("Елена", "Павлова", last_name_orig="Здобнова", residence="Дмитриевы Горы", status=MAIDEN, comment="возраст в документе 16,5"), bride_marriage_num=1, bride_age=16,
                                   witness1=person("Александр", "Семионов", last_name_orig="Гусев"),
                                   witness2=person("Василий", "Андреев", last_name_orig="Витушкин"),
                                   witness3=person("Василий", "Сергеев", last_name_orig="Здобнов", residence="Дмитриевы Горы"),
                                   witness4=person("Иоанн", "Иоаннов", last_name_orig="Калинин")),
                          marriage(2, 9,
                                   groom=person("Григорий", "Владимиров", last_name_orig="Ладугин", status=PEASANT_SON), groom_marriage_num=1, groom_age=19,
                                   bride=person("Евдокия", "Прокопиева", last_name_orig="Дерюгина", residence="Домнино", status=MAIDEN, comment="возраст в документе 15,5"), bride_marriage_num=1, bride_age=15,
                                   witness1=person("Андрей", "Леонтьев", last_name_orig="Ладугин"),
                                   witness2=person("Алексей", "Владимиров", last_name_orig="Ладугин"),
                                   witness3=person("Василий", "Алексеев", last_name_orig="Кочетков"),
                                   witness4=person("Василий", "Димитриев", last_name_orig="Большаков", residence="д. Тамбо?")),
                          ),
          ),
    defaults=RecordDefaults(
        residence="Нижняя Верея",
        status_male=PEASANT_MALE,
        status_female=PEASANT_FEMALE,
        status_bride=PEASANT_MAIDEN
    ),
)
