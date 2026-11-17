from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import (KAZENNYJ_PEASANT_DAUGHTER_MAIDEN, KAZENNYJ_PEASANT_FEMALE,
                                   KAZENNYJ_PEASANT_MALE, KAZENNYJ_PEASANT_SON)

# Метрическая книга Николаевской церкви с. Степанькова за 1830 г., часть вторая.
# **ГАВО ф. 556 оп. 106 д. 524, л. 800** (альбом «Степаньково 1830 (ГАВО 556-106-524)»).
# НВ ещё в приходѣ Степанькова (см. `../ARCHIVES.md`). Взята одна запись — рода Ладугиных.
#
# reviewed=False: найдено агентом, запись перечитана по скану.

DEFAULTS = RecordDefaults(residence="Нижняя Верея", status_male=KAZENNYJ_PEASANT_MALE,
                          status_female=KAZENNYJ_PEASANT_FEMALE)

nizhnyaya_vereya_marriages_1830 = marriage_records(
    "ГАВО", "556", "106", "524", "Нижняя Верея", "Николаевская",
    1830,
    *page("800",
          *marriage_month(Month.JANUARY,
                          # 🏆 **ПЕРВЫЙ БРАК САВВАТЕЯ НИКИТИНА** (линия Ладугиныхъ). «…Казенной деревни Нижней
                          # Вѣри крестьянскій сынъ Савватей Никитинъ того жъ вѣдомства деревни Коннова съ
                          # крестьянскою дѣвкою Татіаною Алексѣевою по добровольному ихъ родителей ихъ согласію…
                          # оба 1-мъ бракомъ», 13 генваря. Поручители «…крестьяне Іосифъ [Осипъ? Иванъ? — имя неуверенно] Еремеевъ и
                          # Алексѣй Никитинъ» — второй, по всей видимости, его брат (РС-10 1857, двор 35).
                          # ⇒ **Татіана Алексѣева — первая жена**, мать Василія («отъ первой жены», РС-10, ок.
                          # 1838); вторая — Варвара Силантьева, мать Леонтія и Осипа. Невѣста — изъ Конново, как
                          # и жены Ипполита Ефимова (1819) и Ксенофонта Иванова (1821)
                          marriage(3, 13,
                                   groom=person("Савватей", "Никитинъ", status=KAZENNYJ_PEASANT_SON),
                                   bride=person("Татіана", "Алексѣева", status=KAZENNYJ_PEASANT_DAUGHTER_MAIDEN, residence="Конново"),
                                   groom_marriage_num=1, bride_marriage_num=1,
                                   witness1=person("Іосифъ", "Еремеевъ"),
                                   witness2=person("Алексѣй", "Никитинъ")),
                          ),
          ),
    defaults=DEFAULTS,
    reviewed=False,
)
