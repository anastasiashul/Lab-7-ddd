# Лабораторная работа 7 - Архитектура, слои и DDD-lite

Проект реализует небольшую систему оплаты заказа с разделением по слоям и доменной моделью.

## Структура проекта:
- Domain/ - доменная модель и бизнес-правила
- Application/ - use-case и интерфейсы
- Infrastructure/ - реализации интерфейсов
- tests/ - тесты use-case без базы данных

## Слои архитектуры: 
### Domain
- Order - сущность 
- OrderLine - часть агрегата
- Money - value object 
- OrderStatus - перечисление статусов заказа
### Application
- PayOrderUseCase - use-case оплаты заказа
- OrderRepository - интерфейс репозитория заказов
- PaymentGateway - интерфейс платежного шлюза
### Infrastructure
- InMemoryOrderRepository - реализация репозитория в памяти без реальной БД
- FakePaymentGateway - фейковый платежный шлюз

## Запуск тестов:

  python -m pytest tests/
