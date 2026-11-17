from verso.ru.dsl import CensusRole, census_records, household, member, person
from verso.ru.dsl.marital_status import SINGLE, SINGLE_FEMALE, WIDOW, WIDOWER

census = census_records(
    "ГАВО", "433", "1", "129", "Нижняя Верея", 1897,

    # Л. 88-89 — Гусев Василий Григорьев
    household("1",
              member(1, person("Василий", "Григорьев", "Гусев"), CensusRole.HEAD, age=45, occupation="лесной объездчик", comment="грамотный (дома)"),
              member(2, person("Марья", "Максимова"), CensusRole.WIFE, age=36),
              member(3, person("Василий"), CensusRole.SON, age=16, marital_status=SINGLE, comment="грамотный (дома)"),
              member(4, person("Петр"), CensusRole.SON, age=19, comment="грамотный (дома)"),
              member(5, person("Федор"), CensusRole.SON, age=13, comment="грамотный (дома)"),
              member(6, person("Иван"), CensusRole.SON, age=11, comment="грамотный (дома)"),
              member(7, person("Анна"), CensusRole.DAUGHTER, age=7, origin="Ардатовский уезд", comment="в источнике: родилась в Ардатовском уезде"),
              member(8, person("Марья"), CensusRole.DAUGHTER, age=11),
              member(9, person("Матрена", "Александрова"), CensusRole.DAUGHTER_IN_LAW, ref_member=4, age=18),
              page="88-89", comment="семья в полном составе отсутствует – Нижегородская губ. Ардатовский уезд"),

    # Л. 90-91, 92 об.-93 — Гусев Семен Ипполитов
    household("2",
              member(1, person("Семен", "Ипполитов", "Гусев"), CensusRole.HEAD, age=67, comment="грамотный (дома у солдата)"),
              member(2, person("Неонила", "Ксенофонтова"), CensusRole.WIFE, age=48),
              member(3, person("Иван"), CensusRole.SON, age=27, occupation="ломовая работа в казенном бору", comment="грамотный (дома у солдата)"),
              member(4, person("Мария"), CensusRole.DAUGHTER, age=15, comment="грамотная (дома у девицы)"),
              member(5, person("Феодор"), CensusRole.SON, age=12, comment="грамотный (в школе грамоты)"),
              member(6, person("Василий"), CensusRole.SON, age=10, comment="грамотный (в школе грамоты)"),
              member(7, person("Алексий"), CensusRole.SON, age=5),
              member(8, person("Петр"), CensusRole.SON, age=3),
              member(9, person("Александра", "Филипова"), CensusRole.WIFE, ref_member=3, age=27, comment="грамотная (дома у девицы)"),
              member(10, person("Александр", "Иванов"), CensusRole.GRANDSON, ref_member=1, age=7, parent_member=3, comment="роль в оригинале: внук и сын №3"),
              member(11, person("Павел", "Иванов"), CensusRole.GRANDSON, ref_member=1, age=3, parent_member=3, comment="роль в оригинале: внук и сын №3"),
              member(12, person("Михаил", "Иванов"), CensusRole.GRANDSON, ref_member=1, age=1, parent_member=3, comment="роль в оригинале: внук и сын №3"), page="90-91, 92об-93"),

    # Л. 98-99 — Гусев Иван Антонов
    household("3",
              member(1, person("Иван", "Антонов", "Гусев"), CensusRole.HEAD, age=45, occupation="извоз и пчеловодство"),
              member(2, person("Петр", "Антонов", "Гусев"), CensusRole.BROTHER, age=24, comment="отсутствует – на военной службе; грамотный (дома у священника)"),
              member(3, person("Параскева", "Савватеева"), CensusRole.WIFE, ref_member=1, age=45),
              member(4, person("Евдокия", "Яковлева"), CensusRole.WIFE, ref_member=2, age=24, origin="Черничка", comment="в источнике: род. в д. Черничка Меленковского у."),
              member(5, person("Наталия"), CensusRole.DAUGHTER, ref_member=2, age=4),
              member(6, person("Анна"), CensusRole.DAUGHTER, ref_member=2, age="5 мес"),
              page="98-99"),

    # Л. 118-119 — Ладугин Леонтий Савватеев
    household("4",
              member(1, person("Леонтий", "Савватеев", "Ладугин"), CensusRole.HEAD, age=53, marital_status=WIDOWER, comment="грамотный (дома у солдата)"),
              member(2, person("Андрей"), CensusRole.SON, age=25, occupation="рубка леса в казенном лесу", comment="грамотный (дома у солдата)"),
              member(3, person("Василий"), CensusRole.SON, age=22, comment="отсутствует – на военной службе; грамотный (дома у девицы)"),
              member(4, person("Мария", "Ерофеева"), CensusRole.WIFE, ref_member=2, age=18),
              member(5, person("Иван", "Андреев"), CensusRole.GRANDSON, ref_member=1, age=4, parent_member=2,
                     secondary_role=CensusRole.SON, secondary_ref_member=8,
                     comment="роль в оригинале: внук и сын №2"),
              member(6, person("Екатерина", "Григорьева"), CensusRole.WIFE, ref_member=3, age=19),
              member(7, person("Анна", "Васильева"), CensusRole.GRANDDAUGHTER, ref_member=1, age="3 мес", parent_member=3, comment="роль в оригинале: внука и дочь №3"),
              member(8, person("Ксения", "Васильева"), CensusRole.WIFE, ref_member=2, age="?", hidden=True,
                     departure_reason="умерла",
                     comment="Отсутствует в переписи 1897; первая жена Андрея Леонтьевича и мать Ивана "
                             "(МК 1892 №5). Мария Ерофеева (№4) — 18 лет в 1897, т.е. не мать "
                             "четырёхлетнего Ивана; добавлена вручную для генеалогической цепочки"),
              page="118-119"),

    # Л. 120-121, 122 об. – 123 — Ладугин Влас Алексеев
    household("5",
              member(1, person("Влас", "Алексеев", "Ладугин"), CensusRole.HEAD, age=63, comment="грамотный (дома у солдата)"),
              member(2, person("Матрона", "Иванова"), CensusRole.WIFE, age=55, origin="Черничка", comment="в источнике: род. в д. Черничка"),
              member(3, person("Владимир"), CensusRole.SON, age=40, occupation="ломовая работа в казенном бору", comment="грамотный (дома у солдата)"),
              member(4, person("Наталья", "Яковлева"), CensusRole.WIFE, ref_member=3, age=40, origin="Черничка", comment="в источнике: род. в д. Черничка"),
              member(5, person("Алексей"), CensusRole.SON, ref_member=3, age=18, marital_status=SINGLE, comment="грамотный (дома у девицы)"),
              member(6, person("Феодор"), CensusRole.SON, ref_member=3, age=16, marital_status=SINGLE, comment="грамотный (дома у девицы)"),
              member(7, person("Николай"), CensusRole.SON, ref_member=3, age=14, comment="грамотный (в школе грамоты)"),
              member(8, person("Андрей"), CensusRole.SON, ref_member=3, age=12, comment="грамотный (в школе грамоты)"),
              member(9, person("Александра"), CensusRole.DAUGHTER, ref_member=3, age=10),
              member(10, person("Григорий"), CensusRole.SON, ref_member=3, age=7),
              member(11, person("Иван"), CensusRole.SON, ref_member=3, age=4),
              member(12, person("Мария"), CensusRole.DAUGHTER, ref_member=3, age=1),
              page="120-121, 122об–123"),

    # Л. 124-125 — Ладугин Кондратий Алексеев
    household("6",
              member(1, person("Кондратий", "Алексеев", "Ладугин"), CensusRole.HEAD, age=63, marital_status=WIDOWER),
              member(2, person("Прохор"), CensusRole.SON, age=27, occupation="ломовой рабочий в казенном бору", comment="грамотный (дома у священника)"),
              member(3, person("Матрона", "Платонова"), CensusRole.WIFE, ref_member=2, age=27),
              member(4, person("Мария"), CensusRole.DAUGHTER, ref_member=2, age=6),
              member(5, person("Анна"), CensusRole.DAUGHTER, ref_member=2, age=2),
              member(6, person("Алексей", "Васильев"), CensusRole.GRANDSON, ref_member=1, age=17, marital_status=SINGLE), page="124-125"),

    # Л. 150-151 — Ладугин Иосиф Савватеев
    household("7",
              member(1, person("Иосиф", "Савватеев", "Ладугин"), CensusRole.HEAD, age=51, occupation="рубка леса в казенном бору", comment="грамотный (дома у солдата)"),
              member(2, person("Евдокия", "Алексеева"), CensusRole.WIFE, age=43),
              member(3, person("Петр"), CensusRole.SON, age=18, marital_status=SINGLE, comment="грамотный (дома у девицы)"),
              member(4, person("Александра"), CensusRole.DAUGHTER, age=14),
              member(5, person("Иван"), CensusRole.SON, age=12),
              member(6, person("Татьяна"), CensusRole.DAUGHTER, age=10),
              member(7, person("Агрипина"), CensusRole.DAUGHTER, age=8),
              member(8, person("Мария"), CensusRole.DAUGHTER, age=1), page="150-151"),

    # Л. 160-161 — Гусев Федор Григорьев
    household("8",
              member(1, person("Федор", "Григорьев", "Гусев"), CensusRole.HEAD, age=47, occupation="рубка леса в казенном бору"),
              member(2, person("Надежда", "Меркулова"), CensusRole.WIFE, age=45),
              member(3, person("Алексей"), CensusRole.SON, age=21, occupation="рубка леса в казенном бору", comment="грамотный (дома у девицы)"),
              member(4, person("Иван"), CensusRole.SON, age=18, marital_status=SINGLE),
              member(5, person("Татьяна"), CensusRole.DAUGHTER, age=16),
              member(6, person("Мария"), CensusRole.DAUGHTER, age=14),
              member(7, person("Василий"), CensusRole.SON, age=12),
              member(8, person("Елена"), CensusRole.DAUGHTER, age=10),
              member(9, person("Евдокия", "Федорова"), CensusRole.WIFE, ref_member=3, age=20),
              page="160-161"),

    # Л. 170-171 — Ладугина Татьяна Евстратова
    household("9",
              member(1, person("Татьяна", "Евстратова", "Ладугина"), CensusRole.HEAD, age=60, marital_status=WIDOW, occupation="повивальная бабка"),
              member(2, person("Евдокия", "Васильева", "Ладугина"), CensusRole.DAUGHTER, age=18, marital_status=SINGLE_FEMALE),
              member(3, person("Ксения", "Васильева", "Ладугина"), CensusRole.DAUGHTER, age=16), page="170-171"),

    # Л. 196-197 — Ладугин Петр Ионов
    household("10",
              member(1, person("Петр", "Ионов", "Ладугин"), CensusRole.HEAD, age=34, occupation="приказчик в винной лавке", comment="грамотный (дома)"),
              member(2, person("Анна", "Елизарова"), CensusRole.WIFE, age=32),
              member(3, person("Иван"), CensusRole.SON, age=15, comment="грамотный (в земск. 1-классн. школе)"),
              member(4, person("Федор"), CensusRole.SON, age=12),
              member(5, person("Марья"), CensusRole.DAUGHTER, age=10),
              member(6, person("Анна"), CensusRole.DAUGHTER, age=6), page="196-197",
              comment="семья в полном составе отсутствует – Нижегородская губ. Ардатовский у. винная лавка"),

    # Л. 212-213 — Гусев Иван Федоров
    household("11",
              member(1, person("Иван", "Федоров", "Гусев"), CensusRole.HEAD, age=64, occupation="поденные заработки", comment="грамотный (дома)"),
              member(2, person("Мавра", "Дмитриева"), CensusRole.WIFE, age=62), page="212-213",
              comment="семья в полном составе отсутствует – Ардатовский уезд завод Кулебаки"),

    # Л. 214-215 — Гусев Павел Иванов
    household("12",
              member(1, person("Павел", "Иванов", "Гусев"), CensusRole.HEAD, age=27, occupation="плетение корзин"),
              member(2, person("Евфросиния", "Кириллова"), CensusRole.WIFE, age=27, origin="Казнево", comment="в источнике: род. в с. Казнево"), page="214-215"),

    # Л. 246-247 — Ладугин Андрей Иосифов
    household("13",
              member(1, person("Андрей", "Иосифов", "Ладугин"), CensusRole.HEAD, age=30, occupation="пильщик", comment="временно в отлучке; грамотный (дома у девицы)"),
              member(2, person("Анна", "Филиппова"), CensusRole.WIFE, age=29),
              member(3, person("Василий"), CensusRole.SON, age=7),
              member(4, person("Елена"), CensusRole.DAUGHTER, age=1), page="246-247"),

    # Л. 268 об. – 269 — Гусев Александр Семенов
    household("14",
              member(1, person("Александр", "Семенов", "Гусев"), CensusRole.HEAD, age=42, occupation="лесопромышленник в казенном бору", comment="грамотный (дома у девицы)"),
              member(2, person("Мария", "Дорофеева"), CensusRole.WIFE, age=42), page="268об–269"),

    # Л. 276-277 — Гусев Филипп Григорьев
    household("15",
              member(1, person("Филипп", "Григорьев", "Гусев"), CensusRole.HEAD, age=50, occupation="дроворуб", comment="грамотный (дома у солдата)"),
              member(2, person("Прасковья", "Андреева"), CensusRole.WIFE, age=42, origin="Окшово", comment="в источнике: род. в с. Окшово"),
              member(3, person("Василий"), CensusRole.SON, age=17, marital_status=SINGLE, comment="грамотный (дома у девицы)"),
              member(4, person("Алексей"), CensusRole.SON, age=16),
              member(5, person("Надежда"), CensusRole.DAUGHTER, age=9), page="276-277"),

    # Л. 290-291 — Гусев Феодор Иванов
    household("16",
              member(1, person("Феодор", "Иванов", "Гусев"), CensusRole.HEAD, age=37, occupation="лесной сторож"),
              member(2, person("Анна", "Ульянова"), CensusRole.WIFE, age=36),
              member(3, person("Василий", "Федоров"), CensusRole.SON, age=16, marital_status=SINGLE, comment="грамотный (дома)"),
              member(4, person("Алексей", "Федоров"), CensusRole.SON, age=12),
              member(5, person("Марья", "Федорова"), CensusRole.DAUGHTER, age=8, origin="Ардатовский уезд", comment="в источнике: род. в Ардатовском уезде"),
              member(6, person("Елена", "Федорова"), CensusRole.DAUGHTER, age=7),
              member(7, person("Александра", "Федорова"), CensusRole.DAUGHTER, age=6), page="290-291",
              comment="семья в полном составе отсутствует – Ардатовский уезд, казенная дача"),

    # Л. 292-293, 294 об. – 295 — Гусев Дмитрий Ксенофонтов
    household("17",
              member(1, person("Дмитрий", "Ксенофонтов", "Гусев"), CensusRole.HEAD, age=63, occupation="пчеловодство"),
              member(2, person("Феврония", "Афонасьева"), CensusRole.WIFE, age=52, comment="приписана к селу Окшово"),
              member(3, person("Василий"), CensusRole.SON, age=36, comment="грамотный (дома у девицы)"),
              member(4, person("Екатерина"), CensusRole.DAUGHTER, age=28, marital_status=SINGLE_FEMALE, comment="во временной отлучке"),
              member(5, person("Елена", "Анисимова"), CensusRole.WIFE, ref_member=3, age=36),
              member(6, person("Прасковья"), CensusRole.DAUGHTER, ref_member=3, age=13),
              member(7, person("Евдокия"), CensusRole.DAUGHTER, ref_member=3, age=11),
              member(8, person("Мария"), CensusRole.DAUGHTER, ref_member=3, age=4),
              member(9, person("Ольга"), CensusRole.DAUGHTER, ref_member=3, age="6 мес"),
              member(10, person("Дмитрий", "Васильев", "Дмитриев"), CensusRole.LODGER, age=26, occupation="портной", destination="Тамболино", comment="проживает д. Тамболино; грамотный (у девицы)"),
              member(11, person("Василий", "Кузьмин", "Смыслов"), CensusRole.LODGER, age=26,
                     occupation="портной подмастерье", destination="Урваново",
                     comment="проживает с. Урваново; грамотный (в народной школе)"),
              member(12, person("Тимофей", "Степанов", "Кузьмин"), CensusRole.LODGER, age=21,
                     occupation="портной подмастерье", destination="Урваново",
                     comment="проживает с. Урваново; грамотный (в народной школе)"),
              member(13, person("Егор", "Степанов", "Кузьмин"), CensusRole.LODGER, age=18,
                     occupation="портной подмастерье", destination="Урваново",
                     comment="проживает с. Урваново; грамотный (в народной школе)"), page="292-293, 294об–295"),

    # Л. 320-321 — Гусева Анна Григорьева
    household("18",
              member(1, person("Анна", "Григорьева", "Гусева"), CensusRole.HEAD, age=46, marital_status=SINGLE_FEMALE,
                     occupation="сучит восковые свечи", comment="раскольница; грамотная (дома у девицы)"),
              page="320-321"),

    document_type="1-я всеобщая перепись",
    document_type_genitive="1-й всеобщей переписи",
    district="20",
    volost="Шиморская",
)
