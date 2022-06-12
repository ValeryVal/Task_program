file = "10m.txt" #here you can enter your file name as a string
import time
start_time = time.time()

list_of_numbers = []

with open(file, 'r') as f:
    lines = f.readlines()

    for i in lines:
        i = i.replace("\n", "")
        list_of_numbers.append(int(i))



def max_number_in_file(some_list):
    current_max = some_list[0]
    for num in some_list:
        if num > current_max:
            current_max = num
    return current_max

print(max_number_in_file(list_of_numbers), "it's a maximum number in file")

def min_number_in_file(some_list):
    current_min = some_list[0]
    for num in some_list:
        if num < current_min:
            current_min = num
    return current_min

print(min_number_in_file(list_of_numbers), "it's a minimum number in file")

def median(some_list):
    sorted_list = sorted(some_list)
    if len(sorted_list) % 2 == 0:
        median_num = (sorted_list[len(sorted_list)//2-1] + sorted_list[len(sorted_list)//2])/2
    else:
        median_num = sorted_list[len(sorted_list)//2]
    return median_num

def arithmetic_mean(some_list):
    counter = 0

    for i in some_list:
        counter += i
    result = counter / len(some_list)
    return result

# print(median(list_of_numbers), "it's median")
#
# print(arithmetic_mean(list_of_numbers), "it's arithmetic mean")


def the_largest_up_numbers_sequence(some_list):
    sequence_list = []
    sequences_dict = {}

    for index in range(len(some_list)):

        if index+1 == len(some_list):
            if some_list[index] > some_list[index-1]:
                sequence_list.append(some_list[index])
                sequences_dict[len(sequence_list)] = sequence_list

        elif some_list[index] < some_list[index+1]:

            sequence_list.append(some_list[index])

        else:
            sequence_list.append(some_list[index])

            sequences_dict[len(sequence_list[:])] = sequence_list[:]

            sequence_list.clear()
    f = sequences_dict.keys()
    value = sequences_dict[max(f)]

    return value


def the_largest_down_numbers_sequence(some_list):
    sequence_list = []
    sequences_dict = {}

    for index in range(len(some_list)):

        if index+1 == len(some_list):
            if some_list[index] < some_list[index-1]:
                sequence_list.append(some_list[index])
                sequences_dict[len(sequence_list)] = sequence_list

        elif some_list[index] > some_list[index+1]:
            sequence_list.append(some_list[index])

        else:
            sequence_list.append(some_list[index])
            sequences_dict[len(sequence_list[:])] = sequence_list[:]

            sequence_list.clear()
    f = sequences_dict.keys()
    value = sequences_dict[max(f)]

    return value

print(the_largest_up_numbers_sequence(list_of_numbers), "it's the largest ascending sequence of numbers")
print(the_largest_down_numbers_sequence(list_of_numbers), "it's the largest descending sequence of numbers")

print("--- %s seconds ---" % (time.time() - start_time))











