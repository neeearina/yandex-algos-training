1. Попытка пересчитать все комбинации слова потерпит фиаско, 
   потому что таких перестановок будет n!, где n – длина слова.
   Для n = 10, это 3628800
2. Если сдаёте задачу на python, то используйте PyPy.
   На обычном интерпретаторе эту задачу не сдать, 
   ну или по крайней мере, мне это не удалось
3. Подумайте о том, сколько символов из текста надо сопоставлять с искомым словом в каждый момент времени
4. Подумайте о переходе от проверки одного подмножества текста к следующему,
   можно ли сохранить какую-нибудь полезную информацию с предыдущего шага и делать это итеративно
5. Погуглите подход решения алгоритмов "скользящее окно" или "sliding window"