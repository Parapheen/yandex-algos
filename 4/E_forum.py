n_msgs = int(input())

topic_msgs = {}
topics = []
res = {}
for i in range(n_msgs):
    msg_id = int(input())
    if msg_id == 0: # new topic
        topic = input().strip()
        topics.append(topic)
        msg_text = input().strip()
        topic_msgs[i + 1] = topic
        res[topic] = 1
    else:
        msg_text = input().strip()
        reply_topic = topic_msgs[msg_id]
        topic_msgs[i + 1] = reply_topic
        res[reply_topic] += 1

max_msgs = max(res.values())
res = sorted([(i, res[i]) for i in res], key=lambda x: -x[1])
topic_res = [(i[0], topics.index(i[0])) for i in res if i[1] == max_msgs]
print(topic_res[0][0])
