def include(m_list, m_value):
    m_list.append(m_value)


def list_values(m_list):
    for element in m_list:
        print(element)


def alter(m_list, m_value, m_position):
    try:
        m_list[m_position] = m_value
    except IndexError:
        print("Impossible to alter [Index Error]")
    except Exception as exp:
        print(type(exp).__name__)


if __name__ == '__main__':

    this_is_a_list = []
    this_is_another_list =[]

    include(this_is_a_list, 45)
    include(this_is_another_list, 75)

    list_values(this_is_a_list)
    list_values(this_is_another_list)
