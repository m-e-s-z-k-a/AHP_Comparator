from AddAlternativesWindow import AddAlternativesWindow
from CalculationsClass import CalculationsClass

def main():
    calculations_matrix = dict()
    #normalnie alternatives array byłoby puste, ale w tym przypadku chcę mieć uzupełnione
    alternatives_array = [['SONY', 'no', 'earphones', 'no', '123', 'no', '10', '20'],
               ['JBL', 'no', 'earphones', 'no', '400', 'no', '15', '5'],
                ['Beats', 'yes', 'headphones', 'yes', '500', 'yes', '15', '5'],
               ['Other', 'yes', 'in-ear', 'no', '200', 'no', '20', '10']]
    AddAlternativesWindow(calculations_matrix, alternatives_array).run()

    """
    cars = ["car1", "car2", "car3", "car4"]
    matrices = dict()
    matrices["cost"] = dict()
    matrices["safety"] = [[1, 2/5, 1/9, 1/7], [5/2, 1, 1/9, 1/4], [9, 9, 1, 5], [7, 4, 1/5, 1]]
    matrices["design"] = [[1, 1/9, 1/9, 1/9], [9, 1, 5, 9/8], [9, 1/5, 1, 7/9], [9, 8/9, 9/7, 1]]
    matrices["capacity"] = dict()
    matrices["warranty"] = [[1, 9, 4/3, 7/5], [1/9, 1, 1/9, 1/9], [3/4, 9, 1, 1/2], [5/7, 9, 2, 1]]
    matrices["cost"]["purchase price"] = [[1, 7/5, 4/9, 4/5], [5/7, 1, 6/7, 7/6], [9/4, 7/6, 1, 3/2], [5/4, 6/7, 2/3, 1]]
    matrices["cost"]["fuel costs"] = [[1, 7/3, 9/5, 2], [3/7, 1, 8/5, 8/5], [5/9, 5/8, 1, 2], [1/2, 5/8, 1/2, 1]]
    matrices["cost"]["maintenance cost"] = [[1, 7/5, 4/3, 5/9], [5/7, 1, 2, 6/5], [3/4, 1/2, 1, 3/2], [9/5, 5/6, 2/3, 1]]
    matrices["capacity"]["trunk size"] = [[1, 6/5, 2/3, 5/2], [5/6, 1, 5/9, 7/5], [3/2, 9/5, 1, 1], [2/5, 5/7, 1, 1]]
    matrices["capacity"]["passenger capacity"] = [[1, 9, 9, 3/8], [1/9, 1, 2/3, 1/9], [1/9, 3/2, 1, 1/9], [8/3, 9, 9, 1]]
    matrices["capacity"]["subcriteria_between_eo"] = [[3/4, 3/4], [1/4, 1/4]]
    matrices["cost"]["subcriteria_between_eo"] = [[1, 7, 8], [1/7, 1, 3], [1/8, 1/3, 1]]
    matrices["criteria_between_eo"] = [[1, 7/5, 5, 9/5, 8], [5/7, 1, 9/5, 7/5, 5/4], [1/5, 5/9, 1, 3/7, 3/4], [5/9, 5/7, 7/3, 1, 7/9], [1/8, 4/5, 4/3, 9/7, 1]]
    myclass = CalculationsClass(cars, matrices)"""

main()