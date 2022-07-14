#we are fingding mean,median,mode,standard_Deviation,confidence interval for aplha =0.05 using zscore,variance


def get_statistics(input_list):
    sorted_input=sorted(input_list)#while finding the median we need to first sort the input
    input_length=len(sorted_input)#there are two cases for median depening on odd lenght and even lenght array
    mean=sum(input_list)/input_length#mean is basically the average of the numbers
    #we need to find the middle lement for the median
    middle_index=(len(sorted_input)-1)//2
    #for odd lenght array median equals the middle element of the arrya
    median=sorted_input[middle_index]
    
    
    
    
    
    if(input_length%2==0):
        middle_number1=sorted_input[middle_index]
        middle_number2=sorted_input[middle_index+1]
        average_middle=(middle_number1+middle_number2)/2
        median=average_middle
        
    #mode is the most frequent ocurring number in the list
    number_counts={x:sorted_input.count(x)for x in set(sorted_input)}
        #here we first convert the list to a new set so that we can pass the individual elements in the unique set then count the number of those unique element in the sorted_list
        #typecasting does not change the original list a new list is created
        #we are then storing it in a dictionary key will be unique numbers
        #value will be the number of occurrences
    mode=max(number_counts.keys(),key=lambda unique_number:number_counts[unique_number])
    sample_variance=sum([(number-mean)**2/(input_length-1)for number in sorted_input])
    standard_deviation=sample_variance**0.5
    standard_error=standard_deviation/len(sorted_input)**0.5
    z_score=1.96*standard_error  #aplha is 0.05 
    confidence_interval=[mean-z_score,mean+z_score]
    
