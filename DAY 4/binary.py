class BinarySearch(list):

    count = 0
    array = []
    limits = 0
    length = 0

    def __init__(self,a,b):
        self.a = a
        self.b = b
        count = 0
        array = []
        limits = 0
        length = 0


        limits = (self.a*self.b)

        for num in range(0,limits):        
            
            array.append(num)                   #appends every number in the range to the array list

        array = array[::self.b]                 #slices the array list to leave only the values with specified consecutive value difference

        self.array = array

        length = len(self.array)                #initializes length to the length of the array
        
        self.length = length

    def search(self,x):
        array = self.array
        count = 0
        end_result = {}
        low = 0;
        high = self.length-1                    #sets the high point of the array

        if x==0:
            return array.index(0)               #returns an in index of 1 if the value added is 0
        else:

            while high>=low:                    #iterates under the condition that high point is greater that the low point   

                mid = (low + high)//2           #sets the mid to the current half of (low + high index)
                middle_value= array[mid]        # sets the middle value to value at the middle index

                count +=1                       #increments count by 1
            

                if middle_value < x:            #compares the middle value to the input 
                    high = mid - 1

                elif middle_value > x:
                    high = mid + 1
                else:
                     return mid

            end_result["Count"]=count
            end_result["Index"]=array.index(x)          
        

            return end_result                   #returns the end result