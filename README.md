## Project Description 
Guiding light app for Destiny 2 LFG or assistance with activities in game. I wanted to build a site that fellow player/guardians could go to and find help with activities in game. I also wanted a way for Clans in game who like to help/sherpa to get recognition for all the help they give to solo players.   


## Link to the DEstiny 2 API
https://bungie-net.github.io/


## Technology Used
- Python
- Django backend
- Bootstrap (was Tailwinds but due to time whas changed)
- Heroku
- 

## Getting Started
   

## Contributions
Thanks to:



## Example data response you plan to use
```
{
  "Response": {
    "searchResults": [
      {
        "bungieGlobalDisplayName": "FrogFist12",
        "bungieGlobalDisplayNameCode": 3730,
        "bungieNetMembershipId": "19649397",
        "destinyMemberships": [
          {
            "iconPath": "/img/theme/bungienet/icons/steamLogo.png",
            "crossSaveOverride": 3,
            "applicableMembershipTypes": [
              1,
              2,
              3
            ],
            "isPublic": true,
            "membershipType": 3,
            "membershipId": "4611686018483839447",
            "displayName": "FrogFist12",
            "bungieGlobalDisplayName": "FrogFist12",
            "bungieGlobalDisplayNameCode": 3730
          },
          {
            "iconPath": "/img/theme/bungienet/icons/xboxLiveLogo.png",
            "crossSaveOverride": 3,
            "applicableMembershipTypes": [],
            "isPublic": true,
            "membershipType": 1,
            "membershipId": "4611686018496966158",
            "displayName": "FrogFist25",
            "bungieGlobalDisplayName": "FrogFist12",
            "bungieGlobalDisplayNameCode": 3730
          },
          {
            "iconPath": "/img/theme/bungienet/icons/psnLogo.png",
            "crossSaveOverride": 3,
            "applicableMembershipTypes": [],
            "isPublic": true,
            "membershipType": 2,
            "membershipId": "4611686018428799592",
            "displayName": "alphadog54",
            "bungieGlobalDisplayName": "FrogFist12",
            "bungieGlobalDisplayNameCode": 3730
          }
        ]
      }
    ],
    "page": 0,
    "hasMore": false
  },
  "ErrorCode": 1,
  "ThrottleSeconds": 0,
  "ErrorStatus": "Success",
  "Message": "Ok",
  "MessageData": {}
}

```

## Visual of your ERD hierarchy

![Screen Shot 2022-03-14 at 9 48 14 AM](https://user-images.githubusercontent.com/54593320/158197143-d642c025-7881-48c3-aa0c-061ac20c167b.png)



## Wire Frames

![GuidingLightWF3](https://user-images.githubusercontent.com/54593320/158200726-4c3dd29a-45e0-47f8-aaa1-bba9a4c9fab9.png)
![GuidingLightWF2](https://user-images.githubusercontent.com/54593320/158200733-866a4b93-60a4-4518-a9e7-f87a06f50543.png)
![GuidingLightWF1](https://user-images.githubusercontent.com/54593320/158200737-f864b00e-e595-4fa5-af5d-be86a8c6663e.png)




## User Stories
-As a user I want to be able create a post so that I can get help with either higher level content or group content inside of Destiny 2.

-As a user I want to be able to find post related to activities I want to play.

-When I find a post I want to know more about the most like whoe made and a description of what they need help with and the rank of the activity.

-I would like to be able sign up for an account. then login and create post. I should be the only one to edit my post or delete them after I make them.

- As a User I would like to make a comment on the post so that I can reply to the OP saying I can help.

### MVP Goals
Have the ability to sign up create an account and create their Guardian Profile.
have the ability to create job post/bounties and have them display on the main board list.
have the ability to filter out bounties by activity type.
Have the ability to make post and comments on the post.



### Stretch Goals
use the bungie api to get more information on the user to display on thier Profile page.
Have Clan pages and where user can rate clans after they have helped them.

## Future Improvements



