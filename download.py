import urllib.request

# request.urlretrieve(url,fileName)

url_img = 'https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'
urllib.request.urlretrieve(url_img, 'baidu.png')

url_video = 'https://vd2.bdstatic.com/mda-mjqef46brirfpnzz/sc/cae_h264_clips/1635157635132011655/mda-mjqef46brirfpnzz.mp4?auth_key=1635170700-0-0-629a0bc163cfddf852cbc3daaee16a42&bcevod_channel=searchbox_feed&pd=1&pt=3&abtest=3000186_3'
urllib.request.urlretrieve(url_video, 'cat.mp4')
