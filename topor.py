print("Фильмы 2000-2017")
films = {
    "2000": ("Гладиатор","Большой куш"),
    "2001": ("Другие","Властелин колец:Братство кольца"),
    "2002": ("Гарри Поттер и философский камень"),
    "2003": ("Индентификация Борна"),
    "2004": ("Возвращение", "Пираты Карибского моря"),
    "2005": ("Гарри Поттер и узник Азкабана","Вечное сияние чистого разума"),
    "2006": ("Бетмен: Начало"),
    "2007": ("Я- легенда", "Пираты Карибского моря","Рататуй","Пока не сыграл в ящик"),
    "2008": ("Валли", "Темный рыцарь","Загадочная история Бенджамина Баттона"),
    "2009": ("Аватар","Список", "Шерлок Холмс",),
    "2010": ("Начало", "Скайлайн", "Неудержимые"),
    "2011": ("1+1", "Гарри Поттер и Дары Смерти", "Исходный код"),
    "2012": ("Мстители", "Хоббит: Нежданное приключение", "Джанго освобожденный"),
    "2013": ("Железный человек 3", "Гравитация", "Тихоокеанский рубеж", "Иллюзия обмана"),
    "2014": ("Интерстеллар", "Стражи Галактики", "Грань будущего"),
    "2015": ("Звездные войны", "Марсианин"),
    "2016": ("Дедпул","Доктор Стрэндж", "Прибытие"),
    "2017": ("Бегущий по лезвию 2049", "Оно","Планета обезьян: Война")
}
pit = films[input("Введите год  ")]
print(pit)