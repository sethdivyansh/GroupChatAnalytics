import matplotlib.pyplot as plt 

file = open('FRESHERS_FORUM_2K24.txt', 'r')

count = {}

for each in file:
    
    # continue if each not start with date

    date = each.split(",")[0]
    if len(date) != 10:
        continue

    # check if each contain the word "joined" or "added"
    # remove those that contain these words
    if 'joined' in each or 'added' in each or 'pinned' in each or 'left' in each or 'removed' in each or 'changed' in each or 'created' in each or 'deleted' in each or 'admin approval' in each or 'changed this group' in each or 'changed the subject' in each or 'changed the group description' in each or "Only messages that mention @Meta AI are sent to Meta. Meta can't read any other messages in this chat. Some responses may be inaccurate or inappropriate. Tap to learn more." in each or ' message timer.' in each or 'turned off disappearing messages' in each or "Messages and calls are end" in each:
        continue
    else:
        name_or_number = each.split("-")
        if len(name_or_number) > 1:
            name_or_number = name_or_number[1].split(":")[0].strip()
            if (name_or_number in count):
                count[name_or_number] += 1
            else:
                count[name_or_number] = 1

x_axis = list(count.keys())
y_axis = list(count.values())
bar_color = '#3498db' 


plt.figure(figsize=(30, 10))



bars = plt.bar(x_axis, y_axis, align = 'center', color = bar_color, width=1)
# plt.bar(courses, values, color ='maroon', width = 0.4)

title = input("Enter the title of the graph: ")

plt.xlabel('Phone Number/Name')
plt.ylabel('Messages Sent')
plt.title(title)
plt.xticks(rotation='vertical', fontsize=8, ha='center')
# plt.show()
# plt.savefig('student_messages_bar_graph.png', bbox_inches='tight')

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom', fontsize=8)

plt.savefig(title+'.pdf', bbox_inches='tight')

mx = 0
cnt = 0
cnt_msg = 0
for key, value in count.items():
    # print(f"{key} : {value}")
    cnt += 1
    cnt_msg += value
    if value > mx:
        mx = value
        name = key
    
print(f"Most active student: {name}")
print(f"Maximum number of messages: {mx}")
print(f"Total number of students: {cnt}")
print(f"Total number of messages: {cnt_msg}")
file.close()
