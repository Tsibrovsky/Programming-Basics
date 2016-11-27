Клас: Паяльник
Характеристика( жало, нагрівальний елемент, потужність)

Об'єкт: Паяльник з керамічним нагрівальним елементом

Інкапсуляція: Для роботи не потрібно знати як працює нагрівальний елемент в середині, достатньо того що коли паяльник нагрівся, то можна паяти.
Наслідування: Паяльна станція, за основу взято основні елементи паяльника( жало, нагрівальний елемент) і розширено функціонал, додано індикацію температури, фен тощо.
Поліморфізм: Паяльники із різними жалами, нагрівальними елементами( керамічними, ніхромовими, індукційними)  - різна реалізація, а використовують для одного і того ж - паяння


Принцип єдиної відповідальності: Головна задача паяти.
Принцип вдкритості/закритості: Можна замінити жало, але це не вплине на роботу нагрівального елемента.
Принцип підстановки Барбари Лісков: Базові властивості лишаються незмінними і для потомків, якби не ускладнилася реалізація паяльника, основні характеристики лишаться незмінними.
Принцип розділення інтерфейсу: Для простих робіт достатньо звичайного паяльника, а для складніших потрібно щось серйозніше(контороль температури, відведення диму тощо)
Принцип інверсії залежності: Паяльник з керамічним нагрівальм елементом  не залежить від паяльника з індукційним, але обоє залежать від класу Паяльник, оскільки від нього залежать основні деталі реалізації