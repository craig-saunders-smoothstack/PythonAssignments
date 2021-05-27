def crowd_test(names):
  if len(names) > 3:
    print("The room is crowded")
list_of_names = ["Tom","Dick","Harry","Jane"]
crowd_test(list_of_names)
list_of_names.pop()
crowd_test(list_of_names)

