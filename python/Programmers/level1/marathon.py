def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if not completion[i] == participant[i]:
            return participant[i]
    return participant[len(participant)-1]