#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import time

from InstagramAPI import InstagramAPI


def any_follower_with_same_pk_as_following(following, followers):
    return any(follower['pk'] == following['pk'] for follower in followers)


def main():
    api = InstagramAPI("username", "password")
    login_successfully = api.login()
    if login_successfully:
        followers = api.getTotalSelfFollowers()
        followings = api.getTotalSelfFollowings()
        counter = 0
        total_users_unfollowed = 0
        for following in followings:
            if counter < 195:
                if not any_follower_with_same_pk_as_following(following, followers):
                    print('Dejando de seguir a: ' + following['username'] + '. Contador: ' + str(counter))
                    result = api.unfollow(following['pk'])
                    if result:
                        counter += 1
                        total_users_unfollowed += 1
                    else:
                        print('Total de usuarios unfollowed: ' + str(total_users_unfollowed))
                        time.sleep(100)
            else:
                counter = 0
                time.sleep(100)
        api.logout()
        print('Total de usuarios unfollowed: ' + total_users_unfollowed)
    else:
        print('Falló el login.')


if __name__ == "__main__":
    main()
