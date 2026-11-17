from verso.ru.dsl import (EventDate, Month, WwiDocumentType, external_source_records, person,
                          wwi_record)
from verso.ru.dsl.marital_status import MARRIED, SINGLE

# WWI participant record from gwar.mil.ru («Памяти героев Великой войны»).
nv_external_sources_1917 = external_source_records(
    "Нижняя Верея",
    wwi_record(
        person("Феодоръ", "Павловъ", "Архангельскій", residence="Нижняя Верея"),
        source_url="https://gwar.mil.ru/heroes/chelovek_gospital172706/",
        rank="ст. унтер-офицер",
        military_unit="Владимирская команда выздоравливающих",
        casualty_reason="болен",
        date=EventDate(1917, Month.SEPTEMBER, 11),
        document_type=WwiDocumentType.ARRIVAL_CARD_HIGHER,
        archive="РГВИА",
        fund="Картотека бюро учёта потерь в Первой мировой войне (офицеров и солдат)",
        archive_location="Шкаф без номера, ящик 49-А",
        # Re-host the scanned hospital card (gwar CDN
        # KartotekaPoter/00000049_A/00001103.jpg) — Git LFS, present via filebase64.
        scan_file="scans/wwi_arhangelskij_1917.jpg",
    ),
    wwi_record(
        person("Петръ", "Федоровъ", "Здобновъ", residence="Старая Верея"),
        source_url="https://gwar.mil.ru/heroes/chelovek_gospital1044573/",
        rank="матрос 1 статьи",
        casualty_reason="болен, название болезни неразборчиво",
        date=EventDate(1917, Month.JANUARY, 14),
        document_type=WwiDocumentType.ARRIVAL_CARD_LOWER,
        archive="РГВИА",
        fund="Картотека бюро учёта потерь в Первой мировой войне (офицеров и солдат)",
        archive_location="Шкаф без номера, ящик 1197-З",
        scan_file="scans/wwi_zdobnov_petr_1917.jpg",
        comment="Место службы по карточке: «Штаб Н-ка охраны вод. зап… кр.» (OCR-сокращение); матрос 1-й статьи.",
    ),
    wwi_record(
        person("Николай", "Архиповъ", "Варженковъ", residence="Старая Верея", occupation="кузнец"),
        source_url="https://gwar.mil.ru/heroes/chelovek_gospital454365/",
        rank="рядовой",
        military_unit="108-й пехотный Саратовский полк",
        marital_status=SINGLE,
        age=20,  # → birth year derived: 1917 − 20 = 1897
        casualty_reason="болен",
        date=EventDate(1917, Month.JUNE, 17),
        place_of_casualty="у Минска",
        document_type=WwiDocumentType.WOUNDED_NOTICE,
        archive="РГВИА",
        fund="Картотека бюро учёта потерь в Первой мировой войне (офицеров и солдат)",
        archive_location="Шкаф без номера, ящик 589-В",
        scan_file="scans/wwi_varzheinov_nikolaj_1917.jpg",
        comment="неграмотный"
    ),
    wwi_record(
        person("Николай", "Павловъ", "Молотковъ", residence="Старая Верея"),
        source_url="https://gwar.mil.ru/heroes/chelovek_donesenie14846535/",
        rank="рядовой",
        military_unit="755-й пехотный Литинский полк",
        marital_status=MARRIED,
        casualty_reason="ранен",
        date=EventDate(1917, Month.JULY, 25),
        document_type=WwiDocumentType.CASUALTY_LISTS,
        place_of_casualty="д. Гура-Остра; 8 Сибирский перевязочный отряд",
        archive="РГВИА",
        fund="Ф. 16196 — Особое делопроизводство по сбору и регистрации сведений о выбывших за смертью, ранами и без вести (1914–1918)",
        inventory="Оп. 1, Именные списки потерь солдат и офицеров 1914–1918 (по полкам и бригадам)",
        case="Д. 708, Списки потерь солдат 755 пехотного Литинского полка",
        scan_file="scans/wwi_molotkov_nikolaj_1917.jpg",
    ),
    wwi_record(
        person("Семенъ", "Ивановъ", "Лепиловъ", residence="Старая Верея"),
        source_url="https://gwar.mil.ru/heroes/chelovek_gospital22153404/",
        rank="рядовой",
        military_unit="17-й пехотный запасный полк",
        casualty_reason="болен, гастроэнтерит",
        place_of_casualty="Могилев-Подольский",
        date=EventDate(1917, Month.AUGUST, 2),
        document_type=WwiDocumentType.ARRIVAL_CARD_LOWER,
        archive="РГВИА",
        fund="Картотека бюро учёта потерь в Первой мировой войне (офицеров и солдат)",
        archive_location="Шкаф без номера, ящик 2050-Л",
        scan_file="scans/wwi_lepilov_semen_1917.jpg",
    ),
    # APPENDED, not inserted in date order, on purpose: the per-year record index feeds the
    # res_name (…_ext_gwar_<N>_external), so slotting this 07.06 card before the 02.08
    # Лепилов card renamed HIS profile 5 → 6. On an applied village that rename destroys the
    # live geni_profile and mints a new one, losing its Geni id. Appending keeps 1–5 fixed.
    wwi_record(
        person("Александръ", "Ивановичъ", "Гусевъ", residence="Нижняя Верея", occupation="чернорабочий"),
        source_url="https://gwar.mil.ru/heroes/chelovek_gospital770654/",
        rank="рядовой",
        military_unit="166-й пехотный Ровненский полк",
        marital_status=MARRIED,
        age=29,  # → birth year derived: 1917 − 29 = 1888
        casualty_reason="болен, цынга",
        place_of_casualty="заболел 20.05.1917 в д. Новоселки; спец. госпиталь № 35 В.З.С., Орёл",
        date=EventDate(1917, Month.JUNE, 7),
        document_type=WwiDocumentType.WOUNDED_NOTICE,
        archive="РГВИА",
        fund="Картотека бюро учёта потерь в Первой мировой войне (офицеров и солдат)",
        archive_location="Шкаф без номера, ящик 714-Г",
        scan_file="scans/wwi_gusev_aleksandr_1917.jpg",
        # Found via a familio «Совпадения» candidate scored at 2% — gwar's indexed fields stop
        # at «Волость Шиморская», and only the SCAN names the village: «Мѣстожительство
        # (передъ войной): д. Вереи», уѣздъ — «родина».
        # «Возрастъ 29» → b. ~1888, which CORROBORATES rather than contradicts: the same man
        # is 7 in the 1897 census (→1890) and baptised at 11 in Feb 1900 (→1889), so all three
        # approximate ages drift by a year apiece — 1890/1889/1888 — the ordinary pattern for
        # self-reported ages. Remaining limit: «Вереи» alone does not say WHICH Верея (Нижняя /
        # Старая / Верхняя all sit in Шиморская вол.), so the attribution to Нижняя Верея
        # rests on the family (son of Иван Семенович and Александра Филипповна), not the card.
        comment="Уведомление о приёме (Форма Б, Всероссийский Земский Союз); грамотный, женатый, православный, русский.",
    ),
)
