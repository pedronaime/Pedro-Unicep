import random


def search_in_list(m_list, m_number):
    m_list.sort()
    half_way = int(len(m_list) / 2)
    lower_limit = 0
    upper_limit = int(0)
    last_number = int(0)
    while half_way != last_number:
        last_number = half_way

        if m_list[half_way] == m_number:
            return half_way
        elif m_list[half_way] > m_number:
            half_way -= half_way

    for elem in range(100):
        half_way = int(half_way + (len(m_list) - half_way) / 2)
        print(half_way)
    #for element in range(len(m_list)):
        #if m_list[element] == m_number:
            #return element

    #raise Exception("Sorry, number not in list")


if __name__ == "__main__":
    numbers_list = []

    for i in range(100000):
        numbers_list.append(random.randint(1, 10000000))

    try:
        #number = int(input("Type a integer"))
        print("The number is in the", search_in_list(numbers_list, 10), "index")
    except Exception as exp:
        print(exp)
