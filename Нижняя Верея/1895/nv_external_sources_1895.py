from verso.ru.dsl import EventDate, Month, criminal_record, external_source_records, person
from verso.ru.dsl.statuses import PEASANT_MALE

nv_external_sources_1895 = external_source_records(
    "Нижняя Верея",
    criminal_record(
        person("Николай", "Михѣевъ", "Фроловъ", status=PEASANT_MALE, residence="Нижняя Верея"),
        age=50,  # → birth year derived: 1895 − 50 = 1845
        record_number=67315,
        page="368",
        date=EventDate(1895, Month.NOVEMBER, 11),
        source_url="https://viewer.rsl.ru/ru/rsl01005433067?page=186",
        # Re-host the scanned gazette page (RSL viewer API
        # /document/rsl01005433067/page/186, С. 368) as the document body — Geni
        # can't snapshot the RSL JS viewer (Git LFS, present via filebase64).
        scan_file="scans/sudimost_nikolaj_frolov_1895.jpg",
        original_text=(
            "67315. ФРОЛОВ, Николай Михеев. Кр. Меленков. у., Шиморск. в., "
            "с. Нижняго Верея (хлебопаш.), 50 л.; приг. Владимир. Окр. С., по 3 ч. 354 ст. "
            "Улож. и Выс. маниф. 14 Нояб. 1894 г., в тюрьму на 40 дней. Исп. 11 Нояб. 1895 г."
        ),
        bibliography=(
            "Ведомость справок о судимости / М-во юстиции. — СПб.: Тип. "
            "Правительствующего Сената, 1870–1929. 1895, кн. 10, ч. 1: "
            "Списки осужденных в 1894 году. С. 368."
        ),
        # Source records the patronymic as «Михеев»; in our metric-book records
        # the same man appears as «Минеевич» (Михей/Миней scribal variant) —
        # to be reconciled onto that profile.
        #
        # Расшифровка записи: крестьянин-хлебопашец с. Нижняя Верея, 50 лет,
        # осуждён Владимирским окружным судом (т.е. дело серьёзнее мировых —
        # с участием суда) по ч. 3 ст. 354 Уложения о наказаниях уголовных и
        # исправительных; срок сокращён по Высочайшему манифесту от 14 ноября
        # 1894 г. (амнистия по случаю бракосочетания/восшествия Николая II) до
        # 40 дней тюрьмы. Исполнено 11 ноября 1895 г.
        # NB: ст. 354 Уложения (изд. 1845 и 1885) формально относится к
        # «недозволенному оставлению отечества» — нетипично для местного
        # крестьянина; точный состав по ч. 3 ст. 354 требует сверки со сканом.
        comment=(
            "В МК записан как Николай Минеевич Фролов (вариант отчества "
            "Михеев/Минеев). Суд: Владимирский окружной суд по ч. 3 ст. 354 "
            "Уложения о наказаниях. Наказание: тюрьма, сокращена по Высочайшему "
            "манифесту 14 ноября 1894 г. до 40 дней. Исполнено 11 ноября 1895 г. "
            "(точный состав преступления по ст. 354 требует уточнения по источнику)."
        ),
    ),
)
