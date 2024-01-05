# Сайт для синтеза речи из текста


## Данный проект позволит переводить текстовую информацию в аудио формат, прослушать и скачать.
## Основан на модуле tts [cilero](https://silero.ai/tag/text-to-speech/)

##Инструкция по установке и запуску
Шаг 1. Clone this repository:
```
git clone
```

Шаг 2. Переход в папку проекта .\web_tts:
```
cd .\web_tts
```

Шаг 3. Установка модулей:
```
pip install -r requirements.txt
В случае ошибки python py -m pip install --upgrade pip
```

Шаг 4. Запустить локальный сервер:
```
streamlit run main.py   
```
## Доступен только русский язык, символы и иностранные слова будут пропущены.
## Для внимательного изучения и настройки tts обращайтесь к официальному источнику: [silero colab](https://colab.research.google.com/github/snakers4/silero-models/blob/master/examples_tts.ipynb)

