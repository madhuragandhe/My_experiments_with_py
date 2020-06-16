#Python program to make a QRcode for a website
import pyqrcode

s='www.geeksforgeeks.org'
url=pyqrcode.QRCode.create(s)
url.svg('qr1.svg',scale=18)