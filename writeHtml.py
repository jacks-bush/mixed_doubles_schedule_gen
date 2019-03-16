import json


def main():
    jsonObj = json.loads(open('matches.json', 'r').read())

    # jsonObj will be a list of all the matches
    # each match consists of a list of the females, followed by a list of the males
    rows = ''
    for day in jsonObj:
        matchStr = ''
        for match in day:
            for pair in match:
                for person in pair:
                    matchStr += wrapTag(person, ['td'])
        rows += wrapTag(matchStr, ['tr'])

    
    with open('matches.html', 'w') as f:
        f.write(wrapTag(rows, ['table', 'body', 'html']))


def wrapTag(text, tagList):
    if (len(tagList) == 1):
        return '<{0}>{1}</{0}>'.format(tagList[0], text)
    return wrapTag('<{0}>{1}</{0}>'.format(tagList.pop(0), text), tagList)


main()
