from AddAlternativesWindow import AddAlternativesWindow

if __name__ == "__main__":
    calculations_matrix = dict()
    #normalnie alternatives array byłoby puste, ale w tym przypadku chcę mieć kilka gotowych opcji
    alternatives_array = [['SONY', 'no', 'earphones', 'no', '123', 'no', '10', '20'],
               ['JBL', 'no', 'earphones', 'no', '400', 'no', '15', '5'],
                ['Beats', 'yes', 'headphones', 'yes', '500', 'yes', '15', '5'],
               ['Other', 'yes', 'in-ear', 'no', '200', 'no', '20', '10']]
    AddAlternativesWindow(calculations_matrix, alternatives_array).run()