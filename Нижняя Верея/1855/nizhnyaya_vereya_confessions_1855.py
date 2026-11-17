from verso.ru.dsl import (CONFESSION_LIST, CensusRole, Month, RecordDefaults, census_records,
                          household, member, page, person)
from verso.ru.dsl.marital_status import WIDOW, WIDOWER
from verso.ru.dsl.statuses import KAZENNYJ_PEASANT_FEMALE, KAZENNYJ_PEASANT_MALE, SOLDIER_WIFE

# Исповедная ведомость Успенской церкви с. ШИМОРСКОГО за 1855 г. — раздел «Казеннаго вѣдомства
# деревни Нижней Верьи крестьяне», дворы 323–359. **ГАВО ф. 556 оп. 111 д. 681, лл. 262об–267**
# (сканы ЭЧЗ 0514–0523; альбом «Шиморское 1855 ИР (ГАВО 556-111-681)»).
#
# Ведомость № 4 свящ. Стефана Яковлева Савицкаго, «Сентября 12-го дня 1855 года», титул л. 230
# (скан 0449). Шиморское в деле — ДВЕ ведомости двух священников (реэстр: «Шиморская 2 част.»);
# Верхняя Верея — во второй, лл. 223–227. Под ведомостью: дьячекъ Дмитрій Алексѣевъ Орловъ,
# пономарь Павелъ Лавровъ.
#
# Прочитан весь раздел (37 дворов); индекс дворов — в `../ARCHIVES.md`. Взяты дворы прямых
# линий — Гусевых (339, 340), Ладугиных (357) — и двор 348, который называет семью Варвары
# Силантьевой, второй жены Савватея Никитина.
#
# ⚠ Возраст в ИР — свидетельство, а не арифметика; метрическую дату им не поправлять.
#
# reviewed=False: прочитано при 1.55×, четыре двора перечитаны при 2.2×, спорное — при 3–4.5×.

census = census_records(
    "ГАВО", "556", "111", "681", "Нижняя Верея", 1855,
    *page("264об",
          # Ефимовичи Гусевых. Все возрасты ложатся на РС-10 (янв. 1858) с разницей 1–3 года, кроме Елисаветы
          household("339",
                    member(1, person("Ипполитъ", "Ефимовъ"), CensusRole.HEAD, age=53),
                    member(2, person("Ксенія", "Леонтьева"), CensusRole.WIFE, age=50),
                    member(3, person("Григорій"), CensusRole.SON, age=31),
                    member(4, person("Семенъ"), CensusRole.SON, age=24),
                    member(5, person("Улита", "Дмитріева"), CensusRole.WIFE, ref_member=3, age=31),
                    member(6, person("Прасковья"), CensusRole.DAUGHTER, ref_member=3, age=11),
                    member(7, person("Анна"), CensusRole.DAUGHTER, ref_member=3, age=5),
                    member(8, person("Марья"), CensusRole.DAUGHTER, ref_member=3, age=1),
                    # ⚠ «Прасковья Гера[си]мова» (4.5×), а РС-10 1857 г. зовёт её «Прасковья Ермоніева».
                    # Возраст сходится (23 ⇒ 25 в РС-10), отчество — нет; одно из двух чтений перечитать
                    member(9, person("Прасковья", "Герасимова"), CensusRole.WIFE, ref_member=4, age=23),
                    # род. 12.11.1853 по РС-10
                    member(10, person("Андрей"), CensusRole.SON, ref_member=4, age=2),
                    # ⚠ «1» — а РС-10 1857 г. даёт ей 5 лет; не сходится
                    member(11, person("Елисавета"), CensusRole.DAUGHTER, ref_member=4, age=1),
                    ),
          # Полуектовичи Гусевых
          household("340",
                    member(1, person("Иванъ", "Полуектовъ"), CensusRole.HEAD, age=68),
                    member(2, person("Прасковья", "Панфилова"), CensusRole.WIFE, age=65),
                    member(3, person("Ксенофонтъ"), CensusRole.SON, age=49),
                    member(4, person("Соломія", "Максимова"), CensusRole.WIFE, ref_member=3, age=49),
                    member(5, person("Григорій"), CensusRole.SON, ref_member=3, age=32),
                    member(6, person("Антонъ"), CensusRole.SON, ref_member=3, age=24),
                    member(7, person("Дмитрій"), CensusRole.SON, ref_member=3, age=20),
                    # 🏆 Та самая Елисавета, род. 30.08.1839 (МК Шиморского 1839, ч. 1 № 92 ж) — жива в 1855 г.;
                    # РС-10 1857 г. её уже не знает (замужем?)
                    member(8, person("Елисавета"), CensusRole.DAUGHTER, ref_member=3, age=15),
                    member(9, person("Варвара", "Ѳедорова"), CensusRole.WIFE, ref_member=5, age=31),
                    member(10, person("Филиппъ"), CensusRole.SON, ref_member=5, age=11),
                    member(11, person("Наталья"), CensusRole.DAUGHTER, ref_member=5, age=9),
                    member(12, person("Ѳедоръ"), CensusRole.SON, ref_member=5, age=5),
                    member(13, person("Авдотья", "Климова"), CensusRole.WIFE, ref_member=6, age=23),
                    # род. 18.06.1855 по РС-10
                    member(14, person("Иванъ"), CensusRole.SON, ref_member=6, age="2 мес"),
                    member(15, person("Февронья", "Аѳонасьева"), CensusRole.WIFE, ref_member=7, age=19),
                    member(16, person("Марья", "Авдѣева"), CensusRole.DAUGHTER_IN_LAW, ref_member=1, age=43,
                           marital_status=WIDOW, comment="«Вдова Марья Авдѣева»"),
                    member(17, person("Иванъ", "Ѳедоровъ"), CensusRole.GRANDSON, ref_member=1, parent_member=21,
                           age=21, comment="«сынъ ея Иванъ Ѳедоровъ»"),
                    member(18, person("Мавра", "Дмитріева"), CensusRole.WIFE, ref_member=17, age=21),
                    # ⚠ «5м» — 5 мѣсяцевъ ⇒ род. ок. апреля 1855 г. РС-10 1857 г. этого сына у Ивана Ѳедорова
                    # не знает (там Василій, род. 03.03.1857) — умер до 1858 г.?
                    member(19, person("Алексѣй"), CensusRole.SON, ref_member=17, age="5 мес"),
                    member(21, person("Ѳедоръ"), None, ref_member=16, parent_member=1, hidden=True,
                           spouse_member=16,
                           comment="В росписи его нет; восстановлен, как в ИР 1838, по отчеству Ивана Ѳедорова "
                                   "и вдовѣ Марьѣ Авдѣевой"),
                    ),
          ),
    *page("265об",
          # 🔴🔴 **СЕМЬЯ СИЛАНА АВРАМОВА.** «Вдова Ѳекла Корнилова 53, дѣти ея: Іосифъ Силантьевъ 32,
          # Аѳанасія 15» — Аѳанасія род. 4.10.1839 у «Силана Аврамова и Ирины Корниловой» (МК 1839, ч. 1
          # № 107 ж), возраст в женской графѣ сходится; в 1837 г. жена Силана — «Ксенія Корнильева». Имя
          # жены трижды разное, отчество одно ⇒ Силанъ умер до 1855 г., вдова — эта Корнилова.
          # Варвара Силантьева (ок. 1815, РС-10) по отчеству — его дочь, но двор её не называет.
          # Іосифъ Силантьевъ женат на **Матрёне Ксенофонтовой** — дочери Ксенофонта Иванова (двор 340;
          # «Матрона 13» ИР 1838) ⇒ Силантьевы и Полуектовичи Гусевых в свойстве.
          # Глава двора — вдова Ульяна Андреева с сыном Миной Абрамовымъ; как Ѳекла с ней связана, строка
          # не говорит (Силанъ — Аврамовъ, Мина — Абрамовъ: вероятно, братья, но Ульяна 72 л. не может быть
          # матерью Силана, если Варвара — его дочь), поэтому роль Ѳеклы нейтральная
          household("348",
                    member(1, person("Ульяна", "Андреева"), CensusRole.HEAD, age=72, marital_status=WIDOW),
                    member(2, person("Мина", "Абрамовъ"), CensusRole.SON, ref_member=1, age=33),
                    member(3, person("Наталья", "Абрамова"), CensusRole.DAUGHTER, ref_member=1, age=34,
                           comment="«дѣти ея: Мина Абрамовъ, Наталья» — отчество написано один раз на обоих"),
                    member(4, person("Лукерья", "Харитонова"), CensusRole.WIFE, ref_member=2, age=34),
                    member(5, person("Наталья"), CensusRole.DAUGHTER, ref_member=2, age=14),
                    member(6, person("Агафья"), CensusRole.DAUGHTER, ref_member=2, age=10),
                    member(7, person("Николай"), CensusRole.SON, ref_member=2, age=9),
                    member(8, person("Авдотья"), CensusRole.DAUGHTER, ref_member=2, age=5),
                    member(9, person("Ѳекла", "Корнилова"), CensusRole.LODGER, ref_member=1, age=53,
                           marital_status=WIDOW),
                    member(10, person("Іосифъ", "Силантьевъ"), CensusRole.SON, ref_member=9, age=32),
                    member(11, person("Аѳанасія", "Силантьева"), CensusRole.DAUGHTER, ref_member=9, age=15,
                           comment="«дѣти ея: Іосифъ Силантьевъ, Аѳанасія» — отчество написано один раз на обоих"),
                    member(12, person("Матрена", "Ксенофонтова"), CensusRole.WIFE, ref_member=10, age=27),
                    member(13, person("Авдотья"), CensusRole.DAUGHTER, ref_member=10, age=7),
                    member(14, person("Александра"), CensusRole.DAUGHTER, ref_member=10, age=5),
                    ),
          ),
    *page("266об",
          # Ладугины: Савватій и Алексѣй Никитины по-прежнему одним дворомъ, но Савватій теперь первым.
          # Над строкой Савватія «2°» — второй бракъ (жена «Варвара Силина» = Силантьева РС-10)
          household("357",
                    member(1, person("Савватій", "Никитинъ"), CensusRole.HEAD, age=41),
                    member(2, person("Варвара", "Силина"), CensusRole.WIFE, age=37),
                    # «дѣти ихъ», но по РС-10 1857 г. Василій — «отъ первой жены» (Татьяны Алексѣевой)
                    member(3, person("Василій"), CensusRole.SON, age=17),
                    # Леонтій 10 ⇒ ок. 1845 (РС-10: 14 л. 4 мѣс. ⇒ 1843; погребеніе 1919: 80 л. ⇒ 1839)
                    member(4, person("Леонтій"), CensusRole.SON, age=10),
                    member(5, person("Іосифъ"), CensusRole.SON, age=8),
                    member(6, person("Марья"), CensusRole.DAUGHTER, age=4),
                    # Вдовъ. Его жены Екатерины Саввиной, старшего сына Іоны (13 в 1838 г.) и дочери Анны в дворе
                    # уже нет
                    member(7, person("Алексѣй", "Никитинъ"), CensusRole.BROTHER, age=58, marital_status=WIDOWER),
                    member(8, person("Кондратій"), CensusRole.SON, ref_member=7, age=21),
                    member(9, person("Власъ"), CensusRole.SON, ref_member=7, age=18),
                    member(10, person("Прасковья", "Николаева"), CensusRole.WIFE, ref_member=8, age=21),
                    member(11, person("Ольга"), CensusRole.DAUGHTER, ref_member=8, age="3 мес"),
                    # Чья она — строка не говорит. Іоны (ок. 1825) в дворе нет: она может быть его женой, если
                    # он в рекрутахъ, — догадка, не вывод
                    member(12, person("Авдотья", "Иванова", status=SOLDIER_WIFE), CensusRole.LODGER, ref_member=1,
                           age=32),
                    ),
          ),
    record_day=12,
    record_month=Month.SEPTEMBER,
    defaults=RecordDefaults(residence="Нижняя Верея", status_male=KAZENNYJ_PEASANT_MALE,
                            status_female=KAZENNYJ_PEASANT_FEMALE),
    **CONFESSION_LIST,
    reviewed=False,
)
