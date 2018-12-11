import sys
import os


# information for matching the length of multipliers.
# works for answer length till 10.
know = { "0" : [0] ,
        "1" : [ 2 ],
         "2" : [2 , 4] ,
         "3" : [3 , 4 ,5 , 6] ,
         "4" : [4 , 6 , 7],
         "5" : [ 5 , 8 , 9 ] , # 4,4 4,1 ,
         "6" : [6 , 9 ,  10] ,
         "7" :[7 , 12] ,
         "8" : [8 , 14] ,
         "9" :[9 , 16] ,
         "10" :[10 , 18]
}


def intt(array):
    # print(array)
    return int("".join(array).replace(" " , ""))


def main(seq , sum_term):

    for idx in range(1 , len(seq)):

        first_slice_len = len(seq[:idx])
        second_slice_len = len(seq[idx:])
        term1 = intt(seq[:idx])
        term2 = intt(seq[idx:])
        # print("terms" , term1 , term2)

        if first_slice_len + second_slice_len == len(seq):
            if term1+term2 == sum_term:
                return True

    return False



def verify(input_number):
    a =  [ str(digt) for digt in str(input_number) ]
    # print("ground truth -->" , a)
    result_list = []
    for idx in range(len(a)):
        # print( idx ,  a[:len(a)-idx] , a[len(a)-idx:] , len(a[:len(a)-idx])  , len(a[len(a)-idx:]) )
        if len(a[:len(a)-idx]) != 0 :
            try:
                # print( len( a[len(a)-idx:] ) )
                for length in know[ str( len( a[len(a)-idx:] )) ]:
                    # for length in range(1,20):
                    # print("length" , length , len(a[:len(a)-idx]) )
                    if len(a[:len(a)-idx]) == length and a[len(a)-idx:]:
                        arr = a[:len(a)-idx]
                        result_list.append( main(seq = arr , sum_term = intt(a[len(a)-idx:]) ) )

                    # print("result_list" , result_list)
            except Exception as e:
                print("error combination" , arr , a[len(a)-idx:])
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                print("--->", e)
                continue

    return(any(result_list))


##########################################################################################################
""""
Usage Example:
"""
number = 9991100
print( verify(input_number = number ) )
