import digitalocean

DO_TOKEN = ''
uptime_threshold = ''

manager = digitalocean.Manager(token=DO_TOKEN)

droplets = []
for droplet in manager.get_all_droplets():
    droplets.append(droplet)

def check_uptime():
    for droplet in droplets:
    start_date = droplet.created_at()
    if start_date < uptime_thresold
        print "Oh no Mr Bill!"
    else:
        return True
    