from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import DIARRHEA, PLEURISY, SMALLPOX, SUFFOCATION
from verso.ru.dsl.statuses import KAZENNYJ_PEASANT_FEMALE, KAZENNYJ_PEASANT_MALE, SOLDIER_WIFE

# Метрическая книга Успенской церкви с. ШИМОРСКОГО за 1839 г., часть третья — погребения
# «Казеннаго вѣдомства деревни Нижней Верьи». **ГАВО ф. 556 оп. 106 д. 635, лл. 502об–514об**
# (альбом «Шиморское 1839 (ГАВО 556-106-635)»). Итог книги: умерло 58 м / 29 ж.
#
# Прочитана вся часть третья. Не вынесены: ч. 3 № 73 ж (21/23 сентября, «онаго вѣдомства и
# деревни», т. е. НВ) — имя отца и умершей не прочитаны; и запись между № 88 и № 89 м (ноябрь,
# без номера и даты): «Казеннаго вѣдомства деревни Нижней Верьи крестьянинъ Максимъ Григорьевъ
# Ко…?», 67 л., отъ удушья — см. `../ARCHIVES.md`.
#
# reviewed=False: прочитано при 1.2–2.6×; спорное — в комментариях.

DEFAULTS = RecordDefaults(residence="Нижняя Верея", status_male=KAZENNYJ_PEASANT_MALE,
                          status_female=KAZENNYJ_PEASANT_FEMALE)

nizhnyaya_vereya_deaths_1839 = death_records(
    "ГАВО", "556", "106", "635", "Нижняя Верея", "Успенская",
    1839,
    *page("502об",
          *death_month(Month.JANUARY,
                       # 🔴🔴 «Меленковской округи казеннаго вѣдомства деревни Нижней Верьи Солдатки **Варвары
                       # Силантьевой** сынъ незаконнорожденный младенецъ Павелъ», 17 дней, отъ колотья. Варвара
                       # Силантьева — вторая жена Савватея Никитина по РС-10 1857 г. (двор 35, 42 г. ⇒ ок.
                       # 1815): в 1839 г. она **солдатка**, то есть замужем за рекрутом прежде Савватея.
                       # Отчество указывает на «Силана Аврамова» (МК 1837 № 142 м, 1839 № 107 ж) — не доказано
                       death(1, Gender.MALE, 1, 3,
                             deceased=person("Павелъ"),
                             age="17 дней",
                             relatives=[relative(person("Варвара", "Силантьева", status=SOLDIER_WIFE), Relationship.MOTHER)],
                             cause_of_death=PLEURISY),
                       ),
          ),
    *page("505об",
          *death_month(Month.FEBRUARY,
                       # ⚠ Отчество отца «Авдѣевъ?» прочитано неуверенно
                       death(12, Gender.FEMALE, 22, 24,
                             deceased=person("Анна"),
                             age=1,
                             relatives=[relative(person("Герасимъ", "Авдѣевъ"), Relationship.FATHER)],
                             cause_of_death=PLEURISY),
                       ),
          ),
    *page("507об",
          *death_month(Month.APRIL,
                       death(26, Gender.MALE, 14, 16,
                             deceased=person("Семенъ", "Григорьевъ"),
                             age=67,
                             cause_of_death=SUFFOCATION),
                       ),
          ),
    *page("511об",
          *death_month(Month.JUNE,
                       death(67, Gender.MALE, 12, 14,
                             deceased=person("Трофимъ"),
                             age=2,
                             relatives=[relative(person("Ѳедоръ", "Ѳедоровъ"), Relationship.FATHER)],
                             cause_of_death=SMALLPOX),
                       ),
          ),
    *page("512об",
          *death_month(Month.SEPTEMBER,
                       # ⚠ Имя отца («Ки…ій/Каллиникъ?») не прочитано; отчество — «Игнатьевъ»
                       death(72, Gender.FEMALE, 21, 23,
                             deceased=person("Васса"),
                             age=4,
                             cause_of_death=SMALLPOX,
                             comment="«крестьянина Ки…я Игнатьева дочь» — имя отца не прочитано"),
                       ),
          ),
    *page("513об",
          *death_month(Month.OCTOBER,
                       death(84, Gender.MALE, 15, 17,
                             deceased=person("Иванъ"),
                             age="полгода",
                             relatives=[relative(person("Илья", "Яковлевъ"), Relationship.FATHER)],
                             cause_of_death=DIARRHEA),
                       ),
          ),
    defaults=DEFAULTS,
    reviewed=False,
)
