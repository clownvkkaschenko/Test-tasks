# Тестовые задания с собеседований
<details><summary># Courier_service_API</summary>
Необходимо разработать прототип API сервиса курьерской доставки
 
#### Что должен включать в себя сервис:
 
- API методы
  - Метод расчета стоимости доставки
  - Метод создания заказа
  - Метод получения информации о заказе
  - Метод получение списка заказов
- Сервис должен уметь взаимодействовать с клиентом при помощи REST API или JSON RPC запросов
- В сервисе должен быть реализован RateLimit с ограничением 10 RPM
 
#### Дополнительная информация:
 
- Логику логистики реализовывать не обязательно. На усмотрение разработчика можно использовать mock ответов.  Цель разработать API сервис, а не полноценный сервис курьерской доставки.
-	Сервис разрабатывается для “Внутригородской доставки”
- Приветствуется покрытие кода тестами
- Приветствуется наличие документации с описанием работы API сервиса
- Приветствуется использования систем хранения данных Redis, PostgreSQL, mongoDB
 
#### Контекст задачи:
 
В процессе работы с API будут участвовать 3 основных лица:
 
- Покупатель. Для него важно рассчитать стоимость доставки от адреса отправки до адреса получения (при этом адрес отправки у нас занесен в систему продавцом), для этого он использует метод "Расчет стоимостей доставки". После расчета стоимости, покупатель принимает решение об оформлении заказа с доставкой. Когда пользователь оформляет заказ, вызывается метод "Создать заказ". После чего, покупатель ожидает доставки своего товара.
- Продавец. Должен иметь возможность видеть весь список заказов, оформленных покупателями. Для этого доступен метод "Получить список заказов". Также для продавца важно иметь возможность посмотреть детальную информацию по заказу, чтобы передать заказ курьеру для доставки. Для этого доступен метод “Получить информацию о заказе”.
- Курьер с мобильным приложением. Должен иметь возможность просматривать информацию о заказе: какой товар, куда и когда нужно доставить. Для этого мобильное приложение будет вызывать метод "Получить информацию о заказе".
</details>
