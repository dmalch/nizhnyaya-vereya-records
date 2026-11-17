from verso.ru.dsl import (Gender, Month, RecordDefaults, birth, birth_month, birth_records, page,
                          person)
from verso.ru.dsl.statuses import (KAZENNYJ_PEASANT_FEMALE, KAZENNYJ_PEASANT_GIRL,
                                   KAZENNYJ_PEASANT_MALE, KAZENNYJ_PEASANT_WIFE)

# Метрическая книга Николаевской церкви с. Степанькова за 1834 г., часть первая.
# **ГАВО ф. 556 оп. 106 д. 573, лл. 147об–148об** (альбом «Степаньково 1834 (ГАВО 556-106-573)»).
# Часть первая — 109 записей (52 м / 57 ж), сходится с итогом книги (л. 162). НВ ещё в приходѣ
# Степанькова. Взяты две записи рода Гусевых. ⛔ Семёна Ипполитова (ок. 1831) в году нет.
#
# reviewed=False: найдено агентом, записи перечитаны по скану.

DEFAULTS = RecordDefaults(residence="Нижняя Верея", status_male=KAZENNYJ_PEASANT_MALE,
                          status_female=KAZENNYJ_PEASANT_FEMALE, status_mother=KAZENNYJ_PEASANT_WIFE)

nizhnyaya_vereya_births_1834 = birth_records(
    "ГАВО", "556", "106", "573", "Нижняя Верея", "Николаевская",
    1834,
    *page("147об",
          *birth_month(Month.FEBRUARY,
                          # Дочь Ксенофонта Иванова (двор 18 РС-10). «…Казенной деревни Нижней Вѣри у крестьянина
                          # Ксенофонта Иванова и законной его жены Соломіи Максимовой родилась дочь Авдотья»,
                          # 12 февраля; воспріемники «показанной деревни крестьянинъ Анисимъ Семеновъ и дѣвка Анна
                          # Иванова». ⚠ По чтению агента погребена 7 мѣс. 10 октября 1834 г. (ч. 3 ж. № 17) — не
                          # сверено, в DSL не вынесено
                       birth(14, Gender.FEMALE, 12, 12,
                             child=person("Авдотья"),
                             father=person("Ксенофонтъ", "Ивановъ"),
                             mother=person("Соломія", "Максимова"),
                             god_parent1=person("Анисимъ", "Семеновъ"),
                             god_parent2=person("Анна", "Иванова", status=KAZENNYJ_PEASANT_GIRL)),
                       ),
          ),
    *page("148об",
          *birth_month(Month.APRIL,
                       # Дочь Ипполита Ефимова и Аксиньи Леонтьевой (линия Гусевых). «Четвертаго надесять числа
                       # Казенной деревни Нижней Вѣри у крестьянина Ипполита Ефимова и законной его жены Аксиньи
                       # Леонтьевой родилась дочь Мавра». ⚠ Воспріемники («Пантелей … и дѣвица …») не прочитаны
                       # уверенно — не вынесены. В РС-10 1857 г. её в дворе 17 нет (замужем или умерла)
                       birth(23, Gender.FEMALE, 14, 14,
                             child=person("Мавра"),
                             father=person("Ипполитъ", "Ефимовъ"),
                             mother=person("Аксинья", "Леонтьева")),
                       ),
          ),
    defaults=DEFAULTS,
    reviewed=False,
)
