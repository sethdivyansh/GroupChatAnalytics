import matplotlib.pyplot as plt 
import re  # added for regex date matching

file_name = input("Enter the name of the file(without .txt): ")

file = open(file_name+'.txt', 'r')

count = {}

for line in file:
    line = line.strip()  # trim whitespace
    # continue if line not start with date

    date = line.split(",")[0]
    if re.match(r'\d{1,2}/\d{1,2}/\d{2,4}', date):  # updated date check

        # check if line contain the word "joined" or "added"
        # remove those that contain these words
        if 'joined' in line or 'added' in line or 'pinned' in line or 'left' in line or 'removed' in line or 'changed' in line or 'created' in line or 'admin approval' in line or 'changed this group' in line or 'changed the subject' in line or 'changed the group description' in line or "Only messages that mention @Meta AI are sent to Meta. Meta can't read any other messages in this chat. Some responses may be inaccurate or inappropriate. Tap to learn more." in line or ' message timer.' in line or 'turned off disappearing messages' in line or "Messages and calls are end" in line or "eleted this group's icon" in line or "arted a video call" in line or "lows like a stagnant pond. Where the faculty" in line or "reset this group's invite link" in line or "requested to join" in line or "Only messages that mention or people share with @Meta AI can be read by Meta. Meta can t read any other messages in this chat, as your personal messages remain end" in line:
            continue
        else:
            name_or_number = line.split("-")
            if len(name_or_number) > 1:
                name_or_number = name_or_number[1].split(":")[0].strip()
                if (name_or_number in count):
                    count[name_or_number] += 1
                else:
                    count[name_or_number] = 1
    else:
        continue

x_axis = list(count.keys())
y_axis = list(count.values())

bar_colors = [
    '#3498db',  # Blue
    '#e74c3c',  # Red
    '#2ecc71',  # Green
    '#f1c40f',  # Yellow
    '#9b59b6',  # Purple
    '#1abc9c',  # Teal
    '#e67e22',  # Orange
    '#34495e'   # Dark Blue
]

# bar_color = '#3498db' 


plt.figure(figsize=(30, 10))



bars = plt.bar(x_axis, y_axis, align = 'center', color = [bar_colors[i % len(bar_colors)] for i in range(len(x_axis))], width=1)
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
