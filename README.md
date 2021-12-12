# EnglishBooksAnalysis

Приложение для анализа книг на английском языке

## Описание

Программа позволить понять что за книга перед потенциальным читателем, какого она жанра, какие слова наиболее 
встречаемые, сколько из них не относятся к наиболее распространенным, сложность книги и другое.
## Запуск

Для начала работы необходимо указать путь к книге, которая предварительно должна быть конвертирована в txt. 
Также книга может быть в формате pdf, но это может снизить скорость работы из-за конвертации внутри.
Для дальнейшей работы с другой книгой необходимо повторить действия.

## Особенности

После анализа книги будет выдаваться диаграмма распределения жанров из которой можно будет делать выводы.
В выборке жанров представлены не все, а основные: бизнес, наука, история, учебники, художественная, 
искусство, компьютеры, религия.
Также будет выдаваться список самых встречаемых слов с их переводом, а также тот же список, 
но без самых распространенных слов.
Еще будет показываться сложность книги, а точнее 3 оценки сложности. 

Сложность 1 рассчитывается как отношение количества уникальных "сложных" к общему количеству уникальных слов,
встретившихся в книге

Сложность 2 рассчитывается как отношение количества "сложных" к общему количеству слов,
встретившихся в книге

Сложность 3 рассчитывается как отношение количества уникальных "простых", встретившихся в книге,
к общему количеству "простых" слов, заранее известных

## Примеры запуска

![alt text](https://github.com/Spyke09/EnglishBooksAnalysis/blob/master/src/1.png)
![alt text](https://github.com/Spyke09/EnglishBooksAnalysis/blob/master/src/2.png)
![alt text](https://github.com/Spyke09/EnglishBooksAnalysis/blob/master/src/3.png)
