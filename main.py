import numpy as np

class MyClass:

    def __init__(self, headphone_models, criteria):
        self.headphone_models = headphone_models
        self.priority_vectors = dict()
        self.criteria_map = criteria
        for key, value in criteria.items():
            if isinstance(value, dict):
                self.priority_vectors[key] = dict()
                for subcriteria_key, subcriteria_value in value.items():
                    if subcriteria_key != "subcriteria_between_eo":
                        self.priority_vectors[key][subcriteria_key] = self.eig_val(subcriteria_value)
                    else:
                        self.priority_vectors[key]["subcriteria_between_eo"] = self.eig_val(subcriteria_value)
            elif key == "criteria_between_eo":
                self.priority_vectors["criteria_between_eo"] = self.eig_val(value)
            else:
                self.priority_vectors[key] = self.eig_val(value)

    def eig_val(self, matrix):
        sums = np.sum(matrix, axis=0)
        x = len(matrix)
        w = []
        for i in range(x):
            for j in range(x):
                matrix[i][j] = matrix[i][j] / sums[j]
        for i in range(x):
            temporary_sum = 0
            for j in range(x):
                temporary_sum += matrix[i][j]
            w.append(temporary_sum * (1/ x))
        return w

    def has_subcriteria(self, element):
        return isinstance(element, dict)

    def comparison(self):
        weights = np.zeros(len(self.headphone_models))
        model_counter = 0
        for headphone_model in self.headphone_models:
            weight = 0
            j = 0
            for criteria_key, criteria_value in self.criteria_map.items():
                if isinstance(criteria_value, dict):
                    temp_weight = 0
                    i = 0
                    for subcriteria_key, subcriteria_value in criteria_value.items():
                        if subcriteria_key != "subcriteria_between_eo":
                            temp_weight += self.priority_vectors[criteria_key][subcriteria_key][model_counter] \
                                           * self.priority_vectors[criteria_key]["subcriteria_between_eo"][i]
                            i += 1
                    weight += temp_weight * self.priority_vectors["criteria_between_eo"][j]
                elif criteria_key != "criteria_between_eo":
                    weight += self.priority_vectors["criteria_between_eo"][j] * self.priority_vectors[criteria_key][model_counter]
                j += 1
            weights[model_counter] = weight
            model_counter += 1
        index_of_max_weight = np.argmax(weights)
        print(weights)
        print("Your best option is: ", self.headphone_models[index_of_max_weight])


def main():
    c1 = [[1, 1 / 7, 1 / 5], [7, 1, 3], [5, 1 / 3, 1]]
    c2 = [[1, 5, 9], [1 / 5, 1, 4], [1 / 9, 1 / 4, 1]]
    c3 = [[1, 4, 1 / 5], [1 / 4, 1, 1 / 9], [5, 9, 1]]
    c4 = [[1, 9, 4], [1 / 9, 1, 1 / 4], [1 / 4, 4, 1]]
    c5 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    c6 = [[1, 6, 4], [1 / 6, 1, 1 / 3], [1 / 4, 3, 1]]
    c7 = [[1, 9, 6], [1 / 9, 1, 1 / 3], [1 / 6, 3, 1]]
    c8 = [[1, 1 / 2, 1 / 2], [2, 1, 1], [2, 1, 1]]
    c12 = [[1, 4, 7, 5, 8, 6, 6, 2],
           [1 / 4, 1, 5, 3, 7, 6, 6, 1 / 3],
           [1 / 7, 1 / 5, 1, 1 / 3, 5, 3, 3, 1 / 5],
           [1 / 5, 1 / 3, 3, 1, 6, 3, 4, 1 / 2],
           [1 / 8, 1 / 7, 1 / 5, 1 / 6, 1, 1 / 3, 1 / 4, 1 / 7],
           [1 / 6, 1 / 6, 1 / 3, 1 / 3, 3, 1, 1 / 2, 1 / 5],
           [1 / 6, 1 / 6, 1 / 3, 1 / 4, 4, 2, 1, 1 / 5],
           [1 / 2, 3, 5, 2, 7, 5, 5, 1]]


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
    myclass = MyClass(cars, matrices)
    myclass.comparison()

main()