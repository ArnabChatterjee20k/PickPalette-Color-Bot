import urllib.parse

def get_url_encoded_querystring(color_palette):

  filtered_palette = {k: v for k, v in color_palette.items() if v is not None}

  query_string = urllib.parse.urlencode(filtered_palette)

  return query_string

def get_livepreview_link(color_palette):
  return "https://pickpalette.netlify.app/preview?"+get_url_encoded_querystring(color_palette)