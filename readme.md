# Шаблон проекта на fastapi

Позволяет не тратить время на настройку инфраструктуры и позвоялет сразу
перейти к разработке на стеке
- fastapi
- postgres + pgmigrate
- pytest

В контейнерах поднимается сервис, postgres, интеграционные тесты.
Автоматически накатываются миграции и версионируется схема.

## Run

```
    make build-testsuite
    make run-testsuite
```

