def parse_logs():
    history = {}

    with open("data/matt.log") as f:
        log = f.readlines()

    for line in log:
        question = line.split("=")[0][14:-1]
        answer = line.strip()[-1]
        if question in history.keys():
            history[question].append(answer)
        else:
            history[question] = [answer]

    return history
