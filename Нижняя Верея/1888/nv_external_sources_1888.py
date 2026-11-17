from verso.ru.dsl import EventDate, Month, criminal_record, external_source_records, person
from verso.ru.dsl.statuses import PEASANT_MALE

nv_external_sources_1888 = external_source_records(
    "Нижняя Верея",
    criminal_record(
        person("Ѳедоръ", "Григорьевъ", "Гусевъ", status=PEASANT_MALE, residence="Нижняя Верея"),
        age=40,  # → birth year derived: 1888 − 40 = 1848
        record_number=60552,
        page="160",
        date=EventDate(1888, Month.OCTOBER, 10),
        source_url="https://viewer.rsl.ru/ru/rsl01005432875?page=81",
        # Re-host the scanned gazette page (RSL viewer API
        # /document/rsl01005432875/page/81, С. 160) as the document body — Geni
        # can't snapshot the RSL JS viewer, so the scan is uploaded via base64
        # (Git LFS, present via filebase64).
        scan_file="scans/sudimost_fedor_gusev_1888.jpg",
        original_text=(
            "60552. ГУСЕВ, Федор Григорьев. Кр. Меленков. у., Шиморск. в., "
            "д. Нижней Верии (хлебопаш.), 40 л.; приг. М. С. 4 уч. Меленков. окр., "
            "по 155 ст. У. о нак., в тюрьму на 4 м. Исп. 10 Окт. 1888 г."
        ),
        bibliography=(
            "Ведомость справок о судимости / М-во юстиции. — СПб.: Тип. "
            "Правительствующего Сената, 1870–1929. 1890, кн. 7, ч. 1. С. 160."
        ),
        # Расшифровка записи: крестьянин-хлебопашец д. Нижняя Верея, 40 лет,
        # приговорён мировым судьёй 4-го участка Меленковского округа по ст. 155
        # Устава о наказаниях, налагаемых мировыми судьями (самовольная порубка /
        # похищение растущего леса) к заключению в тюрьме на 4 месяца. Тюремный
        # срок по этой статье назначался за повторное (3-е и далее) нарушение —
        # для первого/второго был лишь штраф. Приговор исполнен 10 октября 1888 г.
        comment=(
            "Преступление: самовольная порубка / похищение растущего леса "
            "(ст. 155 Устава о наказаниях, налагаемых мировыми судьями). "
            "Суд: мировой судья 4-го уч. Меленковского округа. "
            "Наказание: тюрьма 4 месяца (срок по этой статье — за повторную "
            "порубку). Исполнено 10 октября 1888 г."
        ),
    ),
)
