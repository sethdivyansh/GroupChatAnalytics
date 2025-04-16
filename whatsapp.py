from collections import defaultdict

import matplotlib.pyplot as plt 
def is_valid_message(line):
    # List of phrases to ignore
    ignore_phrases = [
        'joined', 'added', 'pinned', 'left', 'removed', 'changed', 'created',
        'admin approval', 'changed this group', 'changed the subject',
        'changed the group description',
        "Only messages that mention @Meta AI are sent to Meta. Meta can't read any other messages in this chat. Some responses may be inaccurate or inappropriate. Tap to learn more.",
        'message timer.', 'turned off disappearing messages',
        "Messages and calls are end", "eleted this group's icon",
        "arted a video call", "lows like a stagnant pond. Where the faculty",
        "reset this group's invite link", "requested to join",
        "Only messages that mention or people share with @Meta AI",
        "Join other topic-based groups in this community and get admin announcements",
        "*Learn, lead, and leave your mark*"
    ]
    return not any(phrase in line for phrase in ignore_phrases)

def extract_sender(line):
    try:
        # Format: date, time - sender: message
        parts = line.split("-", 1)
        if len(parts) > 1:
            sender = parts[1].split(":", 1)[0].strip()
            return sender
    except Exception:
        pass
    return None

file_name = input("Enter the name of the file (without .txt): ").strip()
with open(file_name + '.txt', 'r', encoding='utf-8') as file:
    count = defaultdict(int)
    for line in file:
        date_part = line.split(",", 1)[0]
        if len(date_part) in (8, 10) and is_valid_message(line):
            sender = extract_sender(line)
            if sender:
                count[sender] += 1
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

# Add spacing by modifying x-axis positions
x_positions = [i * 1.5 for i in range(len(x_axis))]

bars = plt.bar(
    x_positions, y_axis, align='center', 
    color=[bar_colors[i % len(bar_colors)] for i in range(len(x_axis))], 
    width=0.8  # Keep the width unchanged
)

plt.xticks(x_positions, x_axis, rotation='vertical', fontsize=8, ha='center')

title = input("Enter the title of the graph: ")

plt.xlabel('Phone Number/Name')
plt.ylabel('Messages Sent')
plt.title(title)
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
