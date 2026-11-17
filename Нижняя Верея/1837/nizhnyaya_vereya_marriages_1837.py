from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          page, person)
from verso.ru.dsl.statuses import (KAZENNYJ_PEASANT_FEMALE, KAZENNYJ_PEASANT_GIRL,
                                   KAZENNYJ_PEASANT_MALE)

# Метрическая книга Успенской церкви с. ШИМОРСКОГО за 1837 г., часть вторая — венчания с
# участием «Казеннаго вѣдомства деревни Нижней Верьи». **ГАВО ф. 556 оп. 106 д. 611, л. 168**
# (альбом «Шиморское 1837 (ГАВО 556-106-611)»). Прочитана вся часть вторая (57 венчаній):
# из НВ — одна невѣста.
#
# reviewed=False: прочитано при 2.2×.

DEFAULTS = RecordDefaults(residence="Нижняя Верея", status_male=KAZENNYJ_PEASANT_MALE,
                          status_female=KAZENNYJ_PEASANT_FEMALE)

nizhnyaya_vereya_marriages_1837 = marriage_records(
    "ГАВО", "556", "106", "611", "Нижняя Верея", "Успенская",
    1837,
    *page("168",
          *marriage_month(Month.NOVEMBER,
                          # «Казеннаго вѣдомства деревни Верхней Верьи крестьянинъ Лука Ѳедоровъ холостой тогожъ
                          # вѣдомства деревни Нижней Верьи съ крестьянскою дѣвкою Ксеніею Степановою». Поручители
                          # «онагожъ вѣдомства и деревни по женихѣ Семенъ Дорофеевъ и Иларіонъ Семеновъ, а по
                          # невѣстѣ Маркелъ Ивановъ и Харлампій Степановъ». ⚠ «Маркелъ» прочитан так, но по
                          # смыслу это, скорее всего, Марко Ивановъ, мужъ тёзки невѣсты (МК 1837 № 14 ж);
                          # Харлампій Степановъ — по отчеству брат невѣсты
                          marriage(50, 8,
                                   groom=person("Лука", "Ѳедоровъ", residence="Верхние Вереи"),
                                   bride=person("Ксенія", "Степанова", status=KAZENNYJ_PEASANT_GIRL),
                                   groom_marriage_num=1,
                                   witness1=person("Семенъ", "Дорофеевъ", residence="Верхние Вереи", side=Side.GROOM),
                                   witness2=person("Иларіонъ", "Семеновъ", residence="Верхние Вереи", side=Side.GROOM),
                                   witness3=person("Маркелъ", "Ивановъ", side=Side.BRIDE),
                                   witness4=person("Харлампій", "Степановъ", side=Side.BRIDE)),
                          ),
          ),
    defaults=DEFAULTS,
    reviewed=False,
)
