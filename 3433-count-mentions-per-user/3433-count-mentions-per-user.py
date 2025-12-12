class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        mentions = [0] * numberOfUsers
        offline_until = [0] * numberOfUsers   
        events.sort(key=lambda e: (int(e[1]), e[0] != "OFFLINE"))

        for event in events:
            typ, t_str = event[0], event[1]
            t = int(t_str)

            if typ == "OFFLINE":
                user = int(event[2])
                offline_until[user] = max(offline_until[user], t + 60)
                continue
            msg = event[2]
            tokens = msg.split()

            for token in tokens:
                if token == "ALL":
                    for u in range(numberOfUsers):
                        mentions[u] += 1

                elif token == "HERE":
                    for u in range(numberOfUsers):
                        if offline_until[u] <= t:
                            mentions[u] += 1

                elif token.startswith("id"):
                    user = int(token[2:])
                    mentions[user] += 1

        return mentions