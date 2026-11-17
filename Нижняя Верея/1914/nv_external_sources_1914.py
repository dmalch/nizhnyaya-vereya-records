from verso.ru.dsl import (EventDate, Month, WwiDocumentType, external_source_records, person,
                          wwi_record)
from verso.ru.dsl.marital_status import MARRIED
from verso.ru.dsl.statuses import PEASANT_MALE

# WWI participant records from gwar.mil.ru («Памяти героев Великой войны»).
nv_external_sources_1914 = external_source_records(
    "Нижняя Верея",
    wwi_record(
        person("Иванъ", "Васильевъ", "Гусевъ", residence="Нижняя Верея"),
        source_url="https://gwar.mil.ru/heroes/chelovek_donesenie13638130/",
        rank="рядовой",
        military_unit="294-й пехотный Березинский полк",
        casualty_reason="пропал без вести",
        # «Дата события» is a range: 21.11.1914 – 23.12.1914.
        date=EventDate(1914, Month.NOVEMBER, 21, day_end=23, month_end=Month.DECEMBER),
        document_type=WwiDocumentType.CASUALTY_LISTS,
        archive="РГВИА",
        fund="Ф. 16196 — Особое делопроизводство по сбору и регистрации сведений о выбывших за смертью, ранами и без вести (1914–1918)",
        inventory="Оп. 1, Именные списки потерь солдат и офицеров 1914–1918 (по полкам и бригадам)",
        case="Д. 483, Списки потерь 294-го пехотного Березинского полка",
        # Re-host the actual scanned casualty-list page (РГВИА Ф.16196 Оп.1
        # Д.483, л.117 — gwar CDN SpiskiPoter/16196/1/483/00000117.jpg) as the
        # document body via a local base64 upload. This is the only reliable
        # route: pointing source_url straight at that CDN image was tested and
        # FAILS — Geni's snapshotter hits gwar's Incapsula anti-bot page
        # (content_type came back text/html, i.e. the block page, not the JPEG).
        # The JPEG lives under terraform/scans/ and is committed via Git LFS
        # (.gitattributes), so filebase64() resolves after a `git lfs pull`.
        scan_file="scans/wwi_ivan_gusev_1914.jpg",
    ),
    wwi_record(
        person("Петръ", "Осиповичъ", "Ладугинъ", residence="Нижняя Верея", status=PEASANT_MALE),
        source_url="https://gwar.mil.ru/heroes/chelovek_gospital22640806/",
        rank="ефрейтор",
        military_unit="105-й пехотный Оренбургский полк",
        age=38,  # → birth year derived: 1914 − 38 = 1876
        marital_status=MARRIED,
        casualty_reason="тяжелое ранение, огнестрельное, шрапнельное, с повреждением костей верхних конечностей",
        date=EventDate(1914, Month.NOVEMBER, 2),
        document_type=WwiDocumentType.WOUNDED_NOTICE,
        archive="РГВИА",
        fund="Картотека бюро учёта потерь в Первой мировой войне (офицеров и солдат)",
        archive_location="Шкаф без номера, ящик 1922-Л",
        scan_file="scans/wwi_ladugin_petr_1914.jpg",
        comment="",
    ),
)
