from verso.ru.dsl import (Gender, Month, RecordDefaults, birth, birth_month, birth_records, page,
                          person)
from verso.ru.dsl.statuses import (KAZENNYJ_PEASANT_FEMALE, KAZENNYJ_PEASANT_MALE,
                                   KAZENNYJ_PEASANT_WIFE)

# Метрическая книга Николаевской церкви с. Степанькова за 1824 г., часть первая.
# **ГАВО ф. 556 оп. 106 д. 453, л. 537** (альбом «Степаньково 1824 (ГАВО 556-106-453)»);
# книга «подана генваря 9 дня 1825», священники Михаилъ Казанскій и Иванъ Тимоѳеевъ.
# НВ в начале XIX в. — приход Степанькова (см. `../ARCHIVES.md`). Взята одна запись — рода Гусевых.
# ⛔ Венчанія Ипполита и Аксиньи нет ни в Степаньковѣ 1822–1824 гг., ни в Шиморскомъ 1822–1823
# (05.10.2026) ⇒ брак раньше 1822 г.
#
# reviewed=False: найдено при сплошном чтении года (агент), запись перечитана по скану.

DEFAULTS = RecordDefaults(residence="Нижняя Верея", status_male=KAZENNYJ_PEASANT_MALE,
                          status_female=KAZENNYJ_PEASANT_FEMALE, status_mother=KAZENNYJ_PEASANT_WIFE)

nizhnyaya_vereya_births_1824 = birth_records(
    "ГАВО", "556", "106", "453", "Нижняя Верея", "Николаевская",
    1824,
    *page("537",
          *birth_month(Month.JANUARY,
                       # 🏆 **МЕТРИКА ГРИГОРІЯ ИППОЛИТОВА** — старшего брата Семёна Ипполитова (линия Гусевых),
                       # РС-10 1857 г. двор 17 («33 л. 5 мѣс» ⇒ ок. 1824 — сходится). «…Казеннаго Вѣдомства
                       # деревни Нижней Вѣри у крестьянина Ипполита Ефимова отъ жены его Аксиньи Леонтьевой
                       # родился сынъ Григорій, молитвованъ и крещенъ въ домѣ… воспріемники были Никита Андреевъ
                       # да жена Марѳа Филипова тоя деревни крестьяне». Первая метрическая запись Ипполита Ефимова
                       # с женой. ⓘ Кумъ «Никита Андреевъ» — ещё один Никита деревни, не Никита-отец Савватея
                       birth(2, Gender.MALE, 18, 18,
                             child=person("Григорій"),
                             father=person("Ипполитъ", "Ефимовъ"),
                             mother=person("Аксинья", "Леонтьева"),
                             god_parent1=person("Никита", "Андреевъ"),
                             god_parent2=person("Марѳа", "Филипова", status=KAZENNYJ_PEASANT_WIFE)),
                       ),
          ),
    defaults=DEFAULTS,
    reviewed=False,
)
