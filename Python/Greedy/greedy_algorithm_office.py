def count_meeting(meeting_list):
    prev_end = 0
    count = 0
    for begin, end in meeting_list:
        if begin >= prev_end:
            prev_end = end
            count += 1

    return count


def main():
    n = int(input())
    meeting = []
    for i in range(n):
        begin, end = map(int, input().split())
        meeting.append((begin, end))

    meeting.sort(key=lambda x: (x[1], x[0]))
    print(count_meeting(meeting))


if __name__ == '__main__':
    main()