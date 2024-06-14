# Модуль выявления психических отклонений
Этот проект представляет собой комплексное приложение, использующее модель RoBERTa для обработки текстов и бэкенд на Python.
В проекте используется Google Colab для обучения и тестирования модели, а FastAPI для реализации API. 
В будущем планируется доработать клиентскую часть, используя Quasar Framework.

## Основные технологии
**RoBERTa (Robustly optimized BERT approach)** — это улучшенная версия BERT, созданная компанией Facebook AI, которая достигает высоких результатов в задачах обработки естественного языка (NLP).
RoBERTa обучена на больших объемах данных и оптимизирована для повышения производительности.

**Google Colab** — это бесплатный онлайн-инструмент от Google, предоставляющий окружение для выполнения кода на Python в облаке.
Colab позволяет запускать ноутбуки Jupyter, что делает его идеальным для обучения и тестирования моделей машинного обучения.

Для бэкенда используется **FastAPI** — современный, быстрый (high-performance) веб-фреймворк для создания API на Python.
FastAPI позволяет быстро разрабатывать и легко масштабировать веб-приложения.

**Quasar Framework** — это Vue.js фреймворк для создания кроссплатформенных приложений с использованием одного и того же кода.
Quasar позволяет создавать веб-приложения, мобильные приложения и настольные приложения.

## Запуск проекта
### Запуск backenda
```bash
# Переход в директорию
cd .\backend\
# Активация виртуального окружения
venv\Scripts\Activate
# Запуск сервера
uvicorn main:app --reload
```

### Запуск frontenda
```bash
# Переход в директорию
cd .\client\
# Установка зависимостей
npm i
# Запуск клиента
npm run dev
```
