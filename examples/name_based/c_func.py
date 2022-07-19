#!/usr/bin/env python
# Created by "Thieu" at 20:18, 19/07/2022 ----------%                                                                               
#       Email: nguyenthieu2102@gmail.com            %                                                    
#       Github: https://github.com/thieu1995        %                         
# --------------------------------------------------%

import opfunu
import numpy as np
from mealpy.swarm_based import WOA


print("====================Test CamelThreeHump")
ndim = 2
problem = opfunu.name_based.CamelThreeHump(ndim=ndim)
x = np.ones(ndim)
print(problem.evaluate(x))
print(problem.x_global)

print(problem.evaluate(problem.x_global))
print(problem.is_succeed(x))
print(problem.is_succeed(problem.x_global))


print("====================Test CamelSixHump")
ndim = 2
problem = opfunu.name_based.CamelSixHump(ndim=ndim)
x = np.ones(ndim)
print(problem.evaluate(x))
print(problem.x_global)

print(problem.evaluate(problem.x_global))
print(problem.is_succeed(x))
print(problem.is_succeed(problem.x_global))


print("====================Test ChenBird")
ndim = 2
problem = opfunu.name_based.ChenBird(ndim=ndim)
x = np.ones(ndim)
print(problem.evaluate(x))
print(problem.x_global)

print(problem.evaluate(problem.x_global))
print(problem.is_succeed(x))
print(problem.is_succeed(problem.x_global))


print("====================Test ChenV")
ndim = 2
problem = opfunu.name_based.ChenV(ndim=ndim)
x = np.ones(ndim)
print(problem.evaluate(x))
print(problem.x_global)

print(problem.evaluate(problem.x_global))
print(problem.is_succeed(x))
print(problem.is_succeed(problem.x_global))


# problem_dict = {
#     "fit_func": problem.evaluate,
#     "lb": problem.lb.tolist(),
#     "ub": problem.ub.tolist(),
#     "minmax": "min",
#     "log_to": "None",
# }
#
# model = WOA.BaseWOA(problem_dict, epoch=500, pop_size=50)
# best_position, best_fitness_value = model.solve()
# print(best_position, best_fitness_value)


