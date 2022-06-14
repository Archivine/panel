CLUSTER_URL = "mongodb+srv://user:password@clusterUrl"


#site info

SITE_INFO = {
    "site_title": "site-title",
    "site_icon": "site-icon-here",
    "site_theme_color": "#ffffff",
}


#embed stuff

META_EMBED_INFO = {
    
    "og_site_title": "og-title",
    "og_site_description": "og-description",
    "og_site_url": "og-site-url",
    "og_site_image": "og-site-image",
    "og_large_summary_card": False

}

def getSiteInfo():
    return SITE_INFO

def getClusterUrl():
    return CLUSTER_URL

def getEmbedInfo():
    return META_EMBED_INFO