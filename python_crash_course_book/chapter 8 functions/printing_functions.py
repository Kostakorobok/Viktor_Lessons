def ft_print_models(unfinished, finished):
    while unfinished:
        current = unfinished.pop()
        print(f"Printing: {current}")
        finished.append(current)

def ft_show_completed(finished):
    print("The following been completed:")
    for i in finished:
        print(i.title())