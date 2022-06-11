CLUSTER_URL = "mongodb+srv://xvass:OzdSeiuXWFCZMLJU@cluster0.cd2r7.mongodb.net/?retryWrites=true&w=majority"


#site info

SITE_INFO = {
    "site_title": "whatever",
    "site_icon": "https://cdn.discordapp.com/attachments/875052335951384627/977648994945732628/kito.ico"
}


#embed stuff

META_EMBED_INFO = {
    
    "og_site_title": "og title",
    "og_site_description": "og description",
    "og_site_theme_color": "#ffffff",
    "og_site_url": "https://cdn.discordapp.com/attachments/875052335951384627/977648994945732628/kito.ico",
    "og_site_image": "",
    "og_large_summary_card": False

}

def getSiteInfo():
    return SITE_INFO

def getClusterUrl():
    return CLUSTER_URL

def getEmbedInfo():
    return META_EMBED_INFO