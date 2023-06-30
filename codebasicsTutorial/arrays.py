# excersice https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/2_arrays_exercise.md

class ExcersiceList:

    def listExamples(self):
        expense_of_each_month = [2200,2350,2600,2130,2190]
        #1. In Feb, how many dollars you spent extra compare to January?
        febMinusJan = expense_of_each_month[1] - expense_of_each_month[0]
        print(febMinusJan)

        #2. Find out your total expense in first quarter (first three months) of the year.
        firstQuaterExpense = 0
        for month in range(4):
            firstQuaterExpense += expense_of_each_month[month]
        print(firstQuaterExpense)

        #3. Find out if you spent exactly 2000 dollars in any month
        isExpense2000 = False
        for month_expense in expense_of_each_month:
            if(month_expense == 2000):
                isExpense2000 = True
                break
        print(isExpense2000)
        #4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
        expense_of_each_month.append(1980)
        print("After adding june expense in list : ",expense_of_each_month)
        """
        5. You returned an item that you bought in a month of April and
        got a refund of 200$. Make a correction to your monthly expense list
        based on this
        """
        expense_of_each_month[3] = expense_of_each_month[3]-200
        print("update April expense in list : ",expense_of_each_month)

list = ExcersiceList()
list.listExamples()