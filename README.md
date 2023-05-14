Условия домашки
‍💻 Данные, которые передает пользователь для сохранения, а также данные, которые пользователь хочет получать в ответ на обращение в веб-приложению, должны быть динамически изменяемые, поэтому для работы с ними, используются базы данных.

В любом веб-приложении разработчик должен уметь подключить базу данных и создать модели для тех данных, с которыми будет работать пользователь.

Задание 1
Подключите СУБД PostgreSQL для работы в проекте, для этого:

создайте базу данных в ручном режиме
внесите изменения в настройки подключения
Задание 2
В приложении каталога создайте модели:

Product
Category
и опишите для них начальные настройки.

Задание 3
Для каждой модели опишите следующие поля:

Product
Наименование
Описание
Изображение (превью)
Категория
Цена за покупку
Дата создания
Дата последнего изменения
Category
Наименование
Описание
ℹ️ Примечание

Для поля с изображением необходимо добавить соответсвующие настройки в проект, а также установить библиотеку для работы с изображениями 
Pillow

Задание 4
Перенесите отображение моделей в базу данных с помощью инструмента миграций, для этого:

создайте миграции для новых моделей;
примените миграции;
внесите изменения в модель категорий, добавьте поле 
created_at
, примените обновление структуры с помощью миграций;
откатите миграцию до состояния, когда поле 
created_at
 для модели категории еще не существовало и удалите лишнюю миграцию.
Задание 5
Для моделей категории и продукта настройте отображение в административной панели. Для категорий выведите id и наименование в список отображения, а для продуктов выведите в список id, название, цену и категорию.

При этом интерфейс вывода продуктов настройте так, чтобы можно было результат отображения фильтровать по категории, а также осуществлять поиск по названию и полю описания.

Задание 6
Через инструмент shell заполните список категорий, а также выберите список категорий, применив произвольные рассмотренные фильтры. В качестве решения приложите скриншот.
Сформируйте фикстуры для заполнения базы данных.
Напишите кастомную команду, которая умеет заполнять данные в базу данных, при этом предварительно ее зачищать от старых данных.
ℹ️ Примечание

Последний пункт можно реализовать связке с инструментом работы с фикстурами, можно описать вставку данных отдельными запросами.

 
⭐ Дополнительное задание

В контроллер отображения главной страницы добавить выборку последних 5 товаров и вывод их в консоль
Создать модель для хранения контактных данных и попробовать вывести данные, заполненные через админку, на страницу с контактами
Критерии решения:
Результаты работы по первому пункту в 6 задании прикреплены в виде скриншотов терминала
Результат выполнения всего задания залит в github.com и сдан в виде ссылки на репозиторий
Примечание: дополнительные задания помеченные звездочкой желательны, но не обязательны к выполнению.
