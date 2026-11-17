from verso.ru.dsl import CensusRole, census_records, household, member, person

# Всероссийская сельскохозяйственная и поземельная перепись 1916 г. —
# подворные карточки, с. Нижняя Верея Шиморской волости.
# ГАВО Ф.431 Оп.2 Д.714. Источник содержит только глав домохозяйств +
# листы; состав дворов (члены семьи, возраст) не транскрибирован —
# карточки заводятся как заготовки (только глава), расширяются позже.
census = census_records(
    "ГАВО", "431", "2", "714", "Нижняя Верея", 1916,

    household("1",
              member(1, person("Мария", "Васильева", "Гусева"), CensusRole.HEAD, age="?"), page="26-26 об."),

    household("2",
              member(1, person("Федор", "Семенов", "Гусев"), CensusRole.HEAD, age="?"), page="29-29 об."),

    household("3",
              member(1, person("Александра", "Филиппова", "Гусева"), CensusRole.HEAD, age="?"), page="39-39 об."),

    household("4",
              member(1, person("Анна", "Трофимова", "Гусева"), CensusRole.HEAD, age="?"), page="40-40 об."),

    household("5",
              member(1, person("Дмитрий", "Ксенофонтов", "Гусев"), CensusRole.HEAD, age="?"), page="45-45 об."),

    household("6",
              member(1, person("Иван", "Антонов", "Гусев"), CensusRole.HEAD, age="?"), page="65-65 об."),

    household("7",
              member(1, person("Федор", "Владимиров", "Ладугин"), CensusRole.HEAD, age="?"), page="66-66 об."),

    document_type="Всероссийская сельскохозяйственная и поземельная перепись",
    document_type_genitive="Всероссийской сельскохозяйственной и поземельной переписи",
    volost="Шиморская",
    archive_suffix="431-2-714",
    suffix_in_res_names=True,
)
