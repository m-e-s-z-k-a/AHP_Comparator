import numpy as np
import copy

class CalculationsClass:

    def __init__(self, headphone_models, criteria):
        self.ri_values =  [0, 0, 0, 0.546, 0.83, 1.08, 1.26, 1.33, 1.41, 1.45, 1.47]
        self.headphone_models = headphone_models
        self.priority_vectors = dict()
        self.criteria_map_unmodified = copy.deepcopy(criteria)
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

    def consistency_ratio(self, matrix, priority_vector):
        largest_eigenvalue = (np.sum(np.array(matrix), axis=0) @
                              np.array(priority_vector).reshape(-1, 1))[0]
        n = np.array(matrix).shape[0]
        return ((largest_eigenvalue - n) / (n - 1) / self.ri_values[np.array(matrix).shape[0]])

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
        results_array = []
        for i in range(len(weights)):
            results_array.append((weights[i], self.headphone_models[i][0]))
        sorted(results_array)
        consistency_ratios = dict()
        for criteria_key, criteria_value in self.criteria_map_unmodified.items():
            if isinstance(criteria_value, dict):
                consistency_ratios[criteria_key] = dict()
                for subcriteria_key, subcriteria_value in criteria_value.items():
                    if len(subcriteria_value) > 3:
                        consistency_ratios[criteria_key][subcriteria_key] = self.consistency_ratio(subcriteria_value, self.priority_vectors[criteria_key][subcriteria_key])
            elif len(criteria_value) > 3:
                consistency_ratios[criteria_key] = self.consistency_ratio(criteria_value, self.priority_vectors[criteria_key])
        return results_array, consistency_ratios