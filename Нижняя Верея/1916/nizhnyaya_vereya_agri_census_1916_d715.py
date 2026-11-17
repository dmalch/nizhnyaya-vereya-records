from verso.ru.dsl import CensusRole, census_records, household, member, person

# Всероссийская сельскохозяйственная и поземельная перепись 1916 г. —
# подворные карточки, с. Нижняя Верея Шиморской волости.
# ГАВО Ф.431 Оп.2 Д.715. Только главы домохозяйств + листы;
# состав дворов не транскрибирован (заготовки, только глава).
census = census_records(
    "ГАВО", "431", "2", "715", "Нижняя Верея", 1916,

    household("1",
              member(1, person("Федор", "Григорьев", "Гусев"), CensusRole.HEAD, age="?"), page="5-5 об."),

    household("2",
              member(1, person("Аксинья", "Семенова", "Гусева"), CensusRole.HEAD, age="?"), page="32-32 об."),

    household("3",
              member(1, person("Анна", "Григорьева", "Гусева"), CensusRole.HEAD, age="?"), page="33-33 об."),

    household("4",
              member(1, person("Леонтий", "Савватеев", "Ладугин"), CensusRole.HEAD, age="?"), page="34-34 об."),

    document_type="Всероссийская сельскохозяйственная и поземельная перепись",
    document_type_genitive="Всероссийской сельскохозяйственной и поземельной переписи",
    volost="Шиморская",
    archive_suffix="431-2-715",
    suffix_in_res_names=True,
)
