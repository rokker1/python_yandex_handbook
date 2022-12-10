def month(m, lang="ru"):
    ru_year =   [
                "январь", "февраль", "март", "апрель", "май",
                "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"
                ]
    en_year =   [
                "january", "february", "march", "april", "may",
                "june", "july", "august", "september", "october", "november", "december"
                ]
    match lang:
        case "ru":
            return ru_year[m - 1].capitalize()
        case "en":
            return en_year[m - 1].capitalize()


print(month(1, "en"))