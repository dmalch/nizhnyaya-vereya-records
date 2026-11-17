from verso.ru.dsl import EventDate, Month, criminal_record, external_source_records, person
from verso.ru.dsl.statuses import PEASANT_MALE

nv_external_sources_1909 = external_source_records(
    "Нижняя Верея",
    criminal_record(
        person("Гавріилъ", "Дмитріевъ", "Комаровъ", status=PEASANT_MALE, residence="Нижняя Верея"),
        age=27,
        record_number=116120,
        page="134",
        date=EventDate(1909, Month.AUGUST, 21),
        source_url="https://viewer.rsl.ru/ru/rsl01005455248?page=74",
        # Re-host the scanned gazette page (RSL viewer API
        # /document/rsl01005455248/page/74, С. 134) as the document body — Geni
        # can't snapshot the RSL JS viewer (Git LFS, present via filebase64).
        scan_file="scans/sudimost_gavriil_komarov_1909.jpg",
        original_text=(
            "116120. КОМАРОВ, Гавриил Дмитриев. К. Меленков. у., Шиморск. в., "
            "с. Нижней-Вереи, 27 л.; — З. Н. 2 уч. Меленков. у., 154 и 169 М., "
            "тюр. 3 м. Исп. 21 Авг. 909."
        ),
        bibliography=(
            "Ведомость справок о судимости / М-во юстиции. — СПб.: Тип. "
            "Правительствующего Сената, 1870–1929. 1909, кн. 9. С. 134."
        ),
        # Расшифровка записи: крестьянин с. Нижняя Верея, 27 лет, осуждён
        # земским начальником 2-го участка Меленковского уезда по ст. 154 и 169
        # Устава о наказаниях, налагаемых мировыми судьями — кража: ст. 169 =
        # кража имущества ценою не свыше 300 руб.; ст. 154 = похищение уже
        # заготовленного (срубленного) леса. Наказание: тюрьма 3 месяца (в
        # пределах 3–6 мес. по ст. 169). Исполнено 21 августа.
        comment=(
            "Преступление: кража (ст. 169 — кража до 300 руб.; "
            "ст. 154 — похищение заготовленного леса), Устав о наказаниях. "
            "Суд: земский начальник 2-го уч. Меленковского уезда. "
            "Наказание: тюрьма 3 месяца. Исполнено 21 августа."
        ),
    ),
)
