
import re
import logging
import json

import instaloader

def lambda_handler(event, context):
    # getting info
    logging.info(event)
    logging.info(context)
    query = json.loads(event['body'])
    posturl = query['url']

    # loading instagram loader instance
    L = instaloader.Instaloader()

    # get shortcode
    matcher = re.match('https://www.instagram.com/p/([A-Za-z0-9\_\-]+)', posturl)
    if matcher is None:
        return {
            'isBase64Encoded': False,
            'statusCode': 401,
            'body': 'Invalid URL!'
        }
    shortcode = matcher.group(1)

    # retrieve post
    post_info = {
        'url': posturl,
        'shortcode': shortcode
    }
    try:
        post = instaloader.Post.from_shortcode(L.context, shortcode)
    except instaloader.BadResponseException:
        return {
            'isBase64Encoded': False,
            'statusCode': 401,
            'body': 'Unable to retrieve!'
        }
    try:
        profile_name = post.owner_profile.full_name
        profile_bib = post.owner_profile.biography
        post_info['profile'] = {'name': profile_name, 'biography': profile_bib}
    except instaloader.exceptions.LoginRequiredException:
        logging.warning('Profile not available. Login required!')
        post_info['profile'] = {'name': None, 'biography': None}

    post_info['caption'] = post.caption
    post_info['items'] = []

    nodes = post.get_sidecar_nodes()
    check_direct_url = True

    # multiple items
    for node in nodes:
        check_direct_url = False
        if node.is_video:
            item_info = {'type': 'video', 'url': node.video_url}
        else:
            item_info = {'type': 'picture', 'url': node.display_url}
        post_info['items'].append(item_info)

    # single item
    if check_direct_url:
        if post.is_video:
            item_info = {'type': 'video', 'url': post.video_url}
        else:
            item_info = {'type': 'picture', 'url': post.display_url}
        post_info['items'].append(item_info)

    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'body': json.dumps(post_info)
    }
