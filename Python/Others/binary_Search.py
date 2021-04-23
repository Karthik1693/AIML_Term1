def(binary_search(input_list,search_number))

input_list = [2,4,6,8]
search_number = 1
higher_index = len(input_list) 
lower_index = 0


for i in range(higher_index):
    mid_index = int(lower_index +(higher_index-lower_index )/2)   

    if input_list[mid_index] < search_number:
        lower_index = mid_index + 1
        if IndexError:
            break

    if input_list[mid_index] > search_number:
        higher_index = mid_index - 1 

    if input_list[mid_index] == search_number: 
        print("Number",search_number,"indetified at the index -",mid_index,"in the iteration",i+1,".")
        break
    
print("Number not present.Please check the input")