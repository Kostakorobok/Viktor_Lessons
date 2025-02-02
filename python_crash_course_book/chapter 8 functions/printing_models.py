

# unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
# completed_models = []

# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)

# print("\nThe following models have been printed:")
# for i in completed_models:
#     print(i)

def ft_print_models(unfinished, finished):
    while unfinished:
        current = unfinished.pop()
        print(f"Printing: {current}")
        finished.append(current)

def ft_show_completed(finished):
    print("The following been completed:")
    for i in finished:
        print(i.title())

unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

ft_print_models(unprinted_designs, completed_models)
ft_show_completed(completed_models)
