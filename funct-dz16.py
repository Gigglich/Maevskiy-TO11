#16 Написати функцію, яка приймає список кортежів та повертає список, у якому елементи - сума елементів з кожного кортежу за відповідним індексом

def sum_tuples(tuples_list):
    
    result = [0] * len(tuples_list[0])

   
    for tuple in tuples_list:

        for i in range(len(tuple)):

            result[i] += tuple[i]

    return result


tuples_list = [(1, 9, 3, 9), (1, 9, 4, 5), (1, 1, 0, 9)]
print(sum_tuples(tuples_list))  