def crowd_test(names):
  if len(names) > 5:
    print("There's a mob in the room")
  elif len(names) >= 3:
    print("The room is crowded")
  elif len(names) > 0:
    print("The room is not very crowded")
  else:
    print("The room is empty")
list_of_names = ["Tom","Dick","Harry","Richard","Jane","Shaniqua"]
crowd_test(list_of_names)
list_of_names.pop()
list_of_names.pop()
list_of_names.pop()
crowd_test(list_of_names)
list_of_names.pop()
crowd_test(list_of_names)
list_of_names.pop()
list_of_names.pop()
crowd_test(list_of_names)