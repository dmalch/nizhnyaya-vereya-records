from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import PLEURISY, THROAT
from verso.ru.dsl.statuses import (KAZENNYJ_PEASANT_FEMALE, KAZENNYJ_PEASANT_MALE,
                                   KAZENNYJ_PEASANT_WIDOW, SOLDIER_WIFE)

# Метрическая книга Успенской церкви с. ШИМОРСКОГО за 1837 г., часть третья — погребения
# «Казеннаго вѣдомства деревни Нижней Верьи». **ГАВО ф. 556 оп. 106 д. 611, лл. 169об–172**
# (альбом «Шиморское 1837 (ГАВО 556-106-611)»). Прочитана вся часть третья; в графе одна
# дата — дня смерти, погребенія книга не пишет.
#
# reviewed=False: прочитано при 1.6–2.2×; спорное — в комментариях.

DEFAULTS = RecordDefaults(residence="Нижняя Верея", status_male=KAZENNYJ_PEASANT_MALE,
                          status_female=KAZENNYJ_PEASANT_FEMALE)

nizhnyaya_vereya_deaths_1837 = death_records(
    "ГАВО", "556", "106", "611", "Нижняя Верея", "Успенская",
    1837,
    *page("169об",
          *death_month(Month.FEBRUARY,
                       # Та же солдатка Пелагея Ананьина родила Марью 25 генваря (ч. 1 № 15, л. 143об — там
                       # она записана «деревни Верхней Верьи»); здесь — «Нижней Верьи». Одна из двух записей
                       # ошибается деревней. «Отъ колотья» — чтение неуверенно
                       death(8, Gender.FEMALE, 6,
                             deceased=person("Марья"),
                             age="3 недели",
                             relatives=[relative(person("Пелагея", "Ананьина", status=SOLDIER_WIFE), Relationship.MOTHER)],
                             cause_of_death=PLEURISY),
                       ),
          ),
    *page("170об",
          *death_month(Month.MAY,
                       # «у вдовы Марьи Семеновой сынъ младенецъ Максимъ» — сын вдовы, отца книга не называет
                       death(21, Gender.MALE, 8,
                             deceased=person("Максимъ"),
                             age="2 недели",
                             relatives=[relative(person("Марья", "Семенова", status=KAZENNYJ_PEASANT_WIDOW), Relationship.MOTHER)],
                             cause_of_death=PLEURISY),
                       death(20, Gender.FEMALE, 21,
                             deceased=person("Гликерія"),
                             age=1,
                             relatives=[relative(person("Макарій", "Кириловъ"), Relationship.FATHER)],
                             cause_of_death=PLEURISY),
                       ),
          ),
    *page("171",
          *death_month(Month.JUNE,
                       # «у крестьянина Ульяна Иванова пріемышъ Ольга» — пріемная дочь; причина «отъ и…» не
                       # прочитана
                       death(28, Gender.FEMALE, 9,
                             deceased=person("Ольга"),
                             age=2,
                             relatives=[relative(person("Ульянъ", "Ивановъ"), Relationship.FOSTER_FATHER)]),
                       ),
          ),
    *page("172",
          *death_month(Month.AUGUST,
                       death(34, Gender.MALE, 19,
                             deceased=person("Георгій"),
                             age="полгода",
                             relatives=[relative(person("Макаръ", "Савельевъ"), Relationship.FATHER)],
                             cause_of_death=THROAT),
                       ),
          ),
    defaults=DEFAULTS,
    reviewed=False,
)
