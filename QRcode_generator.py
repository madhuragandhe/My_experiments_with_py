#Python program to make a QRcode for a website
import pyqrcode
import requests
s='www.YourWebsiteName.com'
url=pyqrcode.QRCode.create(s)
url.svg('qr1.svg',scale=18)
