import os
import json
import facebook

if __name__ == '__main__':
    token = "EAADlZCi32wJQBAF2tUqzb723fq3BiaZCs2SRtaY3UZC08Y3BtP7wna6U5UaIxLRJoJ737Lr7iTw76T3ZBBZB5zeS8ymnkKxfcTJk5utzoMt8pNVFLohnzdgYjyA5bc3iZBgPE0nFk4q8NuzjPXmXRJ4g0ZAvprvYjAmhvmjmSoHk2NjSwHrKu6yEL5fkqPr0OrxHUZC7gp9ZCQ5TzWGvpTyCm"

    graph = facebook.GraphAPI(token)
    #profile = graph.get_object("me", fields='name,location{general_info,location},languages{name,description}')
    profile = graph.get_object("me", fields='about,address,age_range,birthday,can_review_measurement_request,context,education,email,favorite_athletes,favorite_teams,first_name,gender,hometown,id,inspirational_people,install_type,installed,interested_in,is_famedeeplinkinguser,is_shared_login,languages,last_name,link,location,meeting_for,middle_name,name,name_format,political,public_key,quotes,relationship_status,religion,security_settings,shared_login_upgrade_required_by,short_name,significant_other,sports,test_group,video_upload_limits,viewer_can_send_gift,website,work,friends{about,address,age_range,birthday,can_review_measurement_request,context,education,email,favorite_athletes,favorite_teams,first_name,gender,hometown,id,inspirational_people,install_type,installed,interested_in,is_famedeeplinkinguser,is_shared_login,languages,last_name,link,location,meeting_for,middle_name,name,name_format,political,public_key,quotes,relationship_status,religion,security_settings,shared_login_upgrade_required_by,short_name,significant_other,sports,test_group,video_upload_limits,viewer_can_send_gift,website,work}')


    print(json.dumps(profile, indent=4))
