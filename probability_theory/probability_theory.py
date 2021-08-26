import pt_math
import fractions

# 1. Элементарная теория вероятностей: случайные величины

def pt_1_2_6():

    '''
    11      10 кругов и 1 промах
    216     6**3
    28      28 костяшек в домино
    '''

    return '11, 216, 28'

def pt_1_2_7():

    result = 0

    for i in range(11):
        result = result + 6**i
   
    return result 

def pt_1_2_8():

    '''
    4       [6,9], [7,8], [8,7], [9,6]
    7       [0,0], [1,1], [2,2], [3,3], [4,4], [5,5], [6,6]
    11      кроме февраля
    '''

    return '4, 7, 11'

def pt_1_3_5():

    '''
    1. 59/365

    6, 12, 18, 24, 30 - дни, удовлетворяющие условию "кратные 6"

    4 [6, 12, 18, 24] - февраль
    5*11 [6, 12, 18, 24, 30] - все остальные месяцы
    59 - всего

    365 - 2018 год - не високосный


    2. 11/365

    '''

    return '59/365, 11/365'

def pt_1_3_6():

    '''

    Вероятности выпадения граней

    1*x + 2*x + 3*x + 4*x + 5*x + 6*x = 1; x = 1/21

    1. А и B: 1/21 + 3/21 = 4/21
    2. А или B: 1/21 + 2/21 + 3/21 + 4/21 + 5/21 = 15/21 = 5/7
    3. А и не B: 2/21 + 4/21 = 6/21 = 2/7

    '''

    return '4/21, 5/7, 2/7'

def pt_1_3_7():

    return '''
            1. 1, если A и B "максимально не пересекаются"
            2. 0.7, если A включено в B
            3. 0.5, если А включено в B
            4. 0.2, если A и B "максимально не пересекаются"
            '''

def pt_1_3_8():
    
    return '''
            ИСТИНА      если A⊂B, то P(A)⩽P(B)
            ЛОЖЬ        P(A∩B) может быть больше, чем P(A)P(A)
            ИСТИНА      P(A∪B)=P(A)+P(B)-P(A∩B)
            ЛОЖЬ        Если P(A)>1/2 и P(B)>1/2, P(A∪B)=1
            ЛОЖЬ        P(A∩B)=P(A)P(B)
            ИСТИНА      P(A∩B)⩾P(A)+P(B)−1
            ЛОЖЬ        Событие A∪B означает, что произошло ровно одно из событий A и B
            ЛОЖЬ        P(A)<1
            '''

def pt_1_4_6():

    '''
    (9/14)*(8/13) два черных
    (5/15)*(4/13) два белых

    (9/14)*(8/13) + (5/15)*(4/13) = 46/91 два черных или белых

    1 - (46/91) = 45/91 - ни два черных, ни два белых
    '''

    b = 9
    w = 5

    numerator = b*(b-1) + w*(w-1)
    denominator = (b+w)*(b+w-1)

    probability_1 = fractions.simple_fraction(numerator, denominator)
    probability_2 = fractions.diff(1, fractions.simple_fraction(numerator, denominator))

    return probability_1.to_string() + ', ' + probability_2.to_string()

def pt_1_4_7():

    '''
    900     количество трехзначных чисел [100, 900]

    Сумма будет четной если
    - все три числа будут 
    - два числа нечетные и одно четное

    (450!)/(3!*(450-3)!) + (450!/((450-2)!*2!))*450
    '''   

    return int(
                pt_math.combination(450,3) + 
                pt_math.combination(450,2)*pt_math.combination(450,1))

def pt_1_4_8():

    return int(pt_math.combination(16,1)*
               pt_math.combination(15,1)*
               pt_math.combination(14,1)*
               pt_math.combination(13,1)*
               pt_math.combination(12,1)*
               pt_math.combination(11,1)*
               pt_math.combination(10,2)
               )

def pt_1_4_9():

    # общее количество билетов
    denominator = pt_math.combination(75,3)

    # количество билетов, в которых студент не знает ни одного вопроса
    numerator_0 = pt_math.combination(25,3)

    # количество билетов, в которых студент не знает один вопрос
    numerator_1 = pt_math.combination(25,2)*50

    # вероятность неблагооприятного исхода
    probability_negative = fractions.simple_fraction(numerator_0 + numerator_1, denominator)

    # вероятность благоприятного исхода
    probability = fractions.diff(1, probability_negative)
    
    return probability.to_string()

def pt_1_4_10():

    '''
        Способ 1.

        - один ящик будет пустым, количество способов выбрать пустой ящик - n
        - один ящик будет с двумя шарами, количество способов выбрать пустой ящик - (n-1)
        - количество способов выбрать шары в ящик с двумя шарами (сочетение 2 по n) - n!/(2!*(n-2)!)
        - количество способов разместить остальные шары по пустым ящикам - это перестановки из (n-2) элементов - (n-2)!

        Перемножив, получим

        (n*(n-1)*n!)/2

        Способ 2.

        - размещаем все шары по ящикам - n!
        - выбираем любой из шаров - n
        - перемещаем в другой ящик - (n-1)
        - когда в урне оказалось два шара, это могло получится двумя способами (a положили к b или b - к a), поэтому делим все на 2
        
    '''
    return 'n*(n-1)*factorial(n)/2'

def pt_1_4_11():

   # количество способов выбрать три карты из одной масти
   combination_1 = pt_math.combination(13,3)

   # количество способов выбрать две масти
   combination_2 = pt_math.combination(4,2)

   # количество способов выбрать 6 карт из колоды
   combination_3 = pt_math.combination(52,6)

   # вероятность выбрать по три карты двух мастей
   probability = fractions.simple_fraction(combination_1 * combination_1 * combination_2, combination_3)

   # количество комбинаций, где одна или две карты бубновые, или ни одной
   combination_4 = pt_math.combination(13,1) * pt_math.combination(39,5) + pt_math.combination(13,2) * pt_math.combination(39,4) + pt_math.combination(39,6)

   # вероятность, что одна или две карты бубновые
   probability_2 = fractions.simple_fraction(combination_4, combination_3)

   return probability.to_string() + ', ' + probability_2.to_string()

def pt_1_5_3():



    return ''


# 2. Элементарная теория вероятностей: случайные события

print(pt_1_4_11())
input()
