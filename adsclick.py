# Import các thư viện cần dùng cho class
from requests_html import HTMLSession

class AdsGet:
	noi_dung = HTMLSession()
	url = "https://www.google.com/search?q=toyota+vung+tau"
	data_url = noi_dung.get(url)
	r = data_url.html.find("#tads .ads-ad cite", first=False)
	print('--------CÁC TRANG ĐANG HIỂN THỊ TOP ---------')
	for i in r:
		print(i.text)
	print('Lựa chọn trang bạn muốn autoclick:')
