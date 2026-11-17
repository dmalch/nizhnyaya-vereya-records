from verso.ru.dsl import CensusRole, census_records, household, member, person

# Всероссийская сельскохозяйственная и поземельная перепись 1916 г. —
# подворные карточки, с. Нижняя Верея Шиморской волости.
# ГАВО Ф.431 Оп.2 Д.716. Только главы домохозяйств + листы;
# состав дворов не транскрибирован (заготовки, только глава).
census = census_records(
    "ГАВО", "431", "2", "716", "Нижняя Верея", 1916,

    household("1",
              member(1, person("Ольга", "Петрова", "Гусева"), CensusRole.HEAD, age="?"), page="11-11 об."),

    household("2",
              member(1, person("Марья", "Дорофеева", "Гусева"), CensusRole.HEAD, age="?"), page="15-15 об."),

    household("3",
              member(1, person("Григорий", "Дмитриев", "Гусев"), CensusRole.HEAD, age="?"), page="23-23 об."),

    document_type="Всероссийская сельскохозяйственная и поземельная перепись",
    document_type_genitive="Всероссийской сельскохозяйственной и поземельной переписи",
    volost="Шиморская",
    archive_suffix="431-2-716",
    suffix_in_res_names=True,
)
