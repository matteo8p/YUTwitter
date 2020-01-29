def findNewFollowers(before, after):
    newFollowersList = []

    for user in after:
        if user not in before:
            newFollowersList.append(user)

    return newFollowersList

def findUnfollowers(before, after):
    unfollowersList = []

    for user in before:
        if user not in after:
            unfollowersList.append(user)

    return unfollowersList