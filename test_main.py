import json
from collections import OrderedDict

def main():

    #Open and read file Json
    json_file = open('source_file_2.json')
    json_str = json_file.read()
    json_data = json.loads(json_str)


    #Sorting dictionary by priority
    list_sorted = json_data
    sorting_dictionary(list_sorted, "priority")


    #Creating a list of all managers
    list_managers = []
    for i in range(len(list_sorted)):
        for manager in list_sorted[i]['managers']:
            if manager not in list_managers:
                list_managers.append(manager)


    #Creating a dictionary list of all managers and their projects
    list_dict_managers = []
    projects_manager = []
    for i in list_managers:
        for j in range(len(list_sorted)):
            if i in list_sorted[j]['managers']:
                projects_manager.append(list_sorted[j]['name'])
        dict_manager = {i: projects_manager}
        list_dict_managers.append(dict_manager)
        projects_manager = []


    # Creating a list of all watchers
    list_watchers = []
    for i in range(len(list_sorted)):
        for watcher in list_sorted[i]['watchers']:
            if watcher not in list_watchers:
                list_watchers.append(watcher)


    # Creating a dictionary list of all watchers and their projects
    list_dict_watchers = []
    projects_watcher = []
    for i in list_watchers:
        for j in range(len(list_sorted)):
            if i in list_sorted[j]['watchers']:
                projects_watcher.append(list_sorted[j]['name'])
        dict_watcher = {i: projects_watcher}
        list_dict_watchers.append(dict_watcher)
        projects_watcher = []


    #Creating export of Json files
    with open('watchers.json', 'w', encoding='utf-8') as f:
        json.dump(list_dict_watchers, f, ensure_ascii=False, indent=4)


    with open('managers.json', 'w', encoding='utf-8') as x:
        json.dump(list_dict_managers, x, ensure_ascii=False, indent=4)


# Bubble sort to order a dictionary by its value
def sorting_dictionary(dictionary, value):
    for i in range(len(dictionary),0, -1):
        ordered = False
        for f in range(0, i-1):
            if dictionary[f][value] > dictionary[f + 1][value]:
                dictionary[f], dictionary[f + 1] = dictionary[f + 1], dictionary[f]
                ordered = True

        if not ordered:
            break


if __name__ == '__main__':
    main()